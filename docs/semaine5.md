# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

L'interface Streamlit ne charge jamais directement le modèle afin de séparer les responsabilités entre les composants. Elle communique uniquement avec l'API FastAPI à travers le client HTTP (ui/client.py). C'est l'API qui utilise le modèle pour effectuer les prédictions. Cette architecture facilite la maintenance, les tests et le remplacement du modèle sans modifier l'interface.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Lorsque le score de confiance est inférieur au seuil d'abstention de 70 %, l'interface affiche « Je ne sais pas : à faire vérifier par un humain ». Cette solution évite de présenter une prédiction incertaine comme une décision certaine. Elle permet donc de limiter les erreurs et de faire intervenir un humain lorsque cela est nécessaire.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Lorsque l'API devient inaccessible, l'interface affiche un message indiquant que l'API est injoignable et qu'il faut démarrer le serveur. Lors de notre test du fichier CSV, deux avis sur six ont été classés comme indéterminés et nécessitent donc une vérification humaine.
