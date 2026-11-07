# Semaine 2 — Observations sur le modèle de sentiment

Le modèle a commis 7 erreurs sur les 58 avis de test, dont 2 avis négatifs classés positifs et 5 avis positifs classés négatifs.

Ces erreurs concernent principalement les avis mitigés, car TF-IDF avec une approche Bag of Words prend en compte les mots présents sans comprendre suffisamment leur ordre ni les retournements de sentiment.

Pour améliorer les résultats, il serait intéressant d'utiliser des embeddings ou des modèles de langage capables de mieux comprendre le contexte et l'ordre des mots, comme étudié en semaine 9.
