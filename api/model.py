
"""Raccord entre l'API et le modèle TP2."""

import sys
from pathlib import Path
from typing import Literal, TypedDict, cast

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from predict import charger_modele  # noqa: E402
from predict import predict as _predict  # noqa: E402

SEUIL_ABSTENTION = 0.70


class SentimentResult(TypedDict):
    """Structure du résultat retourné par le classifier."""

    label: Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec seuil d'abstention."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        pipeline = charger_modele()

        classes = set(pipeline.classes_)
        if classes != {"positive", "negative"}:
            raise ValueError(
                f"Classes du modèle invalides : {classes}"
            )

    def predict(self, text: str) -> SentimentResult:
        """Renvoie POSITIVE, NEGATIVE ou INDETERMINE."""
        r = _predict(text)

        label = cast(
            Literal["POSITIVE", "NEGATIVE", "INDETERMINE"],
            r["label"].upper(),
        )

        if r["score"] < SEUIL_ABSTENTION:
            label = "INDETERMINE"

        return {
            "label": label,
            "score": r["score"],
            "text": text[:100],
        }


def load_model() -> SentimentClassifier:
    """Construit le classifier."""
    return SentimentClassifier()
