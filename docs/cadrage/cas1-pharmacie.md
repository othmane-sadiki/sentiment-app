# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Développer une application capable de détecter automatiquement les informations manquantes dans une ordonnance afin d'aider le pharmacien à vérifier sa conformité.


## Utilisateur final (obligatoire)
Le pharmacien est l'utilisateur principal de cette application. Il utilise le système pour repérer rapidement les informations manquantes avant de valider une ordonnance.


## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

L'approche par règles métier est retenue en raison de la vérifiabilité des contrôles (b) et de la conséquence d'une erreur (d). Les informations obligatoires peuvent être contrôlées par des règles précises, puis confirmées par le pharmacien.

## Données nécessaires et leur origine (obligatoire)
Les données nécessaires sont les informations figurant sur les ordonnances : identité du patient, nom du médicament, dosage, date et signature. Elles proviennent des ordonnances fournies par les patients et des règles de vérification définies par la pharmacie.


## Métrique de succès et seuil d'acceptation (obligatoire)
La métrique principale est le taux de détection des informations obligatoires manquantes. Le seuil d'acceptation visé est d'au moins 95 % de détection sur un jeu de test validé par des pharmaciens.


## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une erreur de détection peut entraîner la validation d'une ordonnance incomplète et présenter un risque pour le patient. Le pharmacien doit obligatoirement vérifier les alertes et prendre la décision finale.


## Risques éthiques ou de confidentialité (obligatoire)
Les ordonnances contiennent des données personnelles et médicales sensibles. Leur traitement doit garantir la confidentialité, limiter l'accès aux personnes autorisées et protéger les données des patients.


## Approche écartée et pourquoi (facultatif)
Le Machine Learning est écarté car des règles explicites permettent de vérifier directement les informations obligatoires sans nécessiter un grand jeu de données étiquetées.
