# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Développer une application capable d'analyser les avis clients et de détecter les avis négatifs afin de les prioriser pour un traitement rapide par l'équipe commerciale.

## Utilisateur final (obligatoire)

Le responsable du service client et les équipes commerciales sont les utilisateurs principaux. Ils souhaitent identifier rapidement les clients insatisfaits et traiter les réclamations les plus urgentes.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Le Machine Learning est adapté grâce à la disponibilité de données étiquetées (a) et au coût par requête raisonnable (c). Un modèle de classification supervisée peut apprendre à reconnaître les avis négatifs à partir d'exemples déjà classés.

## Données nécessaires et leur origine (obligatoire)

Les données nécessaires sont les avis des clients accompagnés de leurs sentiments : positif, neutre ou négatif. Elles peuvent provenir des enquêtes de satisfaction, des commentaires sur les produits et des plateformes d'évaluation.

## Métrique de succès et seuil d'acceptation (obligatoire)

La métrique principale est le rappel de la classe négative afin de limiter les avis négatifs non détectés. Le seuil d'acceptation visé est un rappel d'au moins 90 % sur un jeu de test représentatif.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis négatif non détecté peut retarder le traitement d'une réclamation et dégrader la satisfaction du client. Un responsable doit vérifier les avis prioritaires et décider des actions à entreprendre.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis peuvent contenir des données personnelles ou des informations sensibles sur les clients. Il faut protéger ces informations, limiter leur conservation et éviter les décisions automatiques injustifiées.

## Approche écartée et pourquoi (facultatif)

Les règles métier seules sont écartées car les avis peuvent exprimer leur insatisfaction de nombreuses manières, avec des formulations et des nuances difficiles à couvrir par des règles fixes.