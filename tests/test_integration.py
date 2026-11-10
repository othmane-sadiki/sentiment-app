"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D). À COMPLÉTER.

Les tests du TP3 vérifient des réponses ; ceux-ci vérifient le démarrage de l'API
et son comportement quand le modèle manque ou tombe en panne.
"""
from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 (donné en exemple) : un client ouvert par « with » exécute le lifespan."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


# À écrire (étape D) :
# D.2 modèle absent : chemin du modèle redirigé (monkeypatch), cache vidé
#     (charger_modele.cache_clear()), l'API refuse de démarrer (FileNotFoundError) ;
# D.3 modèle non chargé : l'API démarrée, modèle retiré de app.state, 503 sur /health et /predict ;
# D.4 modèle en panne : predict lève RuntimeError, puis ValueError("bug interne") :
#     500 dans les deux cas, sans le message interne dans la réponse.
# Utilisez monkeypatch.setattr pour toute modification : il restaure l'état à la fin du test.

def test_modele_absent_refuse_demarrage(monkeypatch, tmp_path):
    """L'API refuse de démarrer si le fichier du modèle est absent."""
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from fastapi.testclient import TestClient

    import predict
    from api.main import app

    chemin_absent = tmp_path / "sentiment-absent.joblib"

    monkeypatch.setattr(predict, "MODELE", chemin_absent)
    predict.charger_modele.cache_clear()

    try:
        with pytest.raises(FileNotFoundError):
            with TestClient(app):
                pass
    finally:
        predict.charger_modele.cache_clear()

def test_modele_non_charge_retourne_503(monkeypatch):
    """Les routes refusent les requêtes lorsque le modèle n'est pas chargé."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.delattr(app.state, "classifier")

        reponse_health = client.get("/health")
        reponse_predict = client.post(
            "/predict",
            json={"text": "Ce produit est excellent."},
        )

    assert reponse_health.status_code == 503
    assert reponse_predict.status_code == 503
    assert reponse_health.json()["detail"] == "Modèle non chargé"
    assert reponse_predict.json()["detail"] == "Modèle non chargé"

@pytest.mark.parametrize(
    "exception",
    [
        RuntimeError("panne du modèle"),
        ValueError("bug interne"),
    ],
)
def test_modele_en_panne_retourne_500_sans_details(monkeypatch, exception):
    """Les erreurs internes du modèle ne sont jamais exposées au client."""
    from fastapi.testclient import TestClient

    from api.main import app

    class FauxClassifier:
        model_name = "faux-modele"

        def predict(self, text):
            raise exception

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", FauxClassifier())

        reponse = client.post(
            "/predict",
            json={"text": "Ce produit est excellent."},
        )

    assert reponse.status_code == 500
    assert reponse.json()["detail"] == "Erreur interne du serveur"
    assert "bug interne" not in reponse.text
    assert "panne du modèle" not in reponse.text