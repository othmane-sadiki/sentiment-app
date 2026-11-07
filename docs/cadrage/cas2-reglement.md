# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Créer une application permettant aux employés de poser des questions sur le règlement intérieur et d'obtenir des réponses basées sur le document officiel.

## Utilisateur final (obligatoire)

Les employés de l'entreprise sont les utilisateurs principaux. Ils peuvent rechercher rapidement des informations concernant les congés, les horaires, les absences et les procédures internes.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

L'approche RAG est adaptée grâce à la vérifiabilité des réponses (b) et au coût par requête maîtrisable (c). Le système recherche les passages pertinents du règlement intérieur et utilise ces informations pour produire des réponses fondées sur le document.

## Données nécessaires et leur origine (obligatoire)

Les données nécessaires sont le règlement intérieur, ses différentes sections et ses éventuelles mises à jour. Elles proviennent des documents officiels validés et fournis par le service des ressources humaines.

## Métrique de succès et seuil d'acceptation (obligatoire)

La qualité sera mesurée par le taux de réponses correctes et conformes au document officiel. Le seuil d'acceptation visé est de 90 % de réponses correctes sur un jeu de questions de test.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une réponse incorrecte peut induire un employé en erreur concernant ses droits ou ses obligations. Les réponses doivent être vérifiées à partir des documents sources et les situations importantes confirmées par le service des ressources humaines.

## Risques éthiques ou de confidentialité (obligatoire)

Les questions peuvent contenir des informations personnelles concernant les employés. Il faut protéger les échanges, limiter la collecte des données et contrôler l'accès aux documents internes.

## Approche écartée et pourquoi (facultatif)

Un modèle génératif seul est écarté car il peut produire des informations incorrectes ou inventer des règles qui ne figurent pas dans le règlement intérieur.