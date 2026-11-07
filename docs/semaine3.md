# Semaine 3 : l'API, notes du binôme

## 1. Pourquoi l'API refuse-t-elle de démarrer sans `models/sentiment.joblib`, plutôt que de démarrer et de répondre 503 ?

L'API charge le modèle dès son démarrage grâce à la fonction `lifespan`. Si le fichier `models/sentiment.joblib` est absent, une erreur `FileNotFoundError` est déclenchée et le serveur refuse de démarrer. Ce comportement permet de détecter immédiatement un problème de configuration et d'éviter de lancer une API qui ne pourrait pas effectuer de prédictions.

## 2. Un texte vide est refusé deux fois : par Pydantic, puis par `predict()`. Est-ce redondant ?

Non, cette double validation est utile. Pydantic vérifie les données reçues par l'API avant leur traitement, notamment que le texte contient au moins un caractère. De son côté, la fonction `predict()` effectue également cette vérification pour protéger le modèle, même lorsqu'elle est appelée directement depuis un autre programme. Cette approche renforce la fiabilité de l'application.