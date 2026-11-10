
# Semaine 4 : tests approfondis et qualité

## 1. Couverture

- Avant (étape A) : 91 %, avec 6 lignes jamais exécutées.
- Les lignes non couvertes se trouvaient dans `api/main.py`. Les tests initiaux ne vérifiaient pas suffisamment les différents scénarios de démarrage, d'indisponibilité et de panne de l'API.
- Après (étape D) : 97,26 %, avec seulement 2 lignes non couvertes (94-96 dans `api/main.py`). Elles correspondent au bloc de lancement direct avec Uvicorn (`if __name__ == "__main__"`), qui n'est pas exécuté par les tests HTTP.
- Couverture finale après l'étape E : 96,34 %.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Un texte composé uniquement d'espaces était accepté. | Tests de limites et propriétés Hypothesis. | Ajout de `strip_whitespace=True` et `min_length=1` dans `api/schemas.py`. |
| Le modèle pouvait retourner un résultat avec une confiance insuffisante. | Tests de prédiction et courbe de seuil. | Ajout du seuil d'abstention dans `api/model.py`. |
| Une exception interne du modèle pouvait être interprétée comme une erreur de validation 422. | Tests d'intégration des pannes. | Gestion des exceptions internes avec une réponse 500 générique, sans exposer les détails. |
| L'API devait gérer explicitement l'absence ou l'indisponibilité du modèle. | Tests d'intégration du démarrage et des routes. | Vérification du chargement du modèle et réponse 503 lorsque le modèle n'est pas chargé. |

## 3. Seuil d'abstention

Quelques points de la courbe obtenue avec `python src/courbe_seuil.py` :

| Seuil | Part des avis traités | Exactitude | Erreurs | Vers un humain |
| --- | ---: | ---: | ---: | ---: |
| 0,50 | 100 % | 87,9 % | 7 | 0 |
| 0,60 | 72 % | 95,2 % | 2 | 16 |
| 0,70 | 64 % | 100 % | 0 | 21 |

- Seuil retenu : 0,70.
- Part des avis envoyés à un humain : 36 % (21 sur 58).
- Justification : ce seuil permet d'obtenir 100 % d'exactitude sur le jeu de démonstration évalué, sans erreur parmi les prédictions automatiques. Il privilégie la prudence plutôt que le nombre de réponses automatiques.

## 4. Jeu d'or

- Bilan obtenu avec `python src/bilan_jeu_or.py` : 3 justes, 17 abstentions, 0 erreur franche.
- Le jeu contient 20 avis, dont 8 avis difficiles.
- Ces résultats montrent que le modèle préfère s'abstenir lorsque sa confiance est insuffisante. Il évite ainsi les erreurs franches sur ce jeu, mais son taux d'abstention reste élevé : il doit donc être utilisé avec une validation humaine pour les cas incertains.

## 5. Outils statiques

- Au départ : Ruff signalait 11 problèmes de qualité du code, notamment des imports mal organisés, des imports inutilisés, des variables ambiguës et des constructions à risque. Mypy ne signalait aucune erreur.
- Les corrections ont concerné notamment `api/main.py`, `api/model.py`, `src/evaluate.py` et plusieurs fichiers de tests.
- À la fin : `ruff check .` affiche `All checks passed!`.
- Mypy : `Success: no issues found in 3 source files`. Le contrôle Mypy du hook Pre-commit sur `api` passe également.
- Ruff a détecté des problèmes de qualité statique, mais les défauts fonctionnels liés à la validation des textes et à la gestion des pannes ont nécessité des tests spécifiques.

## 6. Automatisation et intégration continue

- Pre-commit a été installé avec `python -m pre_commit install`.
- La commande `python -m pre_commit run --all-files` a validé Ruff et Mypy.
- Un commit volontairement incorrect contenant `import os` a été refusé par Ruff. Le commit n'a donc pas été créé.
- Le workflow GitHub Actions `.github/workflows/ci.yml` a été complété avec quatre étapes : installation des outils de qualité, Ruff, Mypy et tests avec couverture minimale de 95 %.
- Vérification locale finale : 84 tests réussis, 0 échec et 96,34 % de couverture.
- Un avertissement de dépréciation provenant de Starlette/AnyIO subsiste, sans incidence sur la réussite des tests.
