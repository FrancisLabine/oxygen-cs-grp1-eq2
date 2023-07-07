# Métrique de CI

Les 4 métriques sont relativement simple. Elles permettent de voir le temps des builds et du taux d'acceptation de ce ces derniers.
Ces métriques sont utile pour recevoir de la rétroaction qui permettera d'améliorer la facon de coder, tester et déployer.


##### Nouvelles Métriques :

- Temps d’exécution du pipeline de build pour un build donné.
  
    | ID | build | totalTime |
    | ----------- | ----------- | ---|
    |1         |12354|32|
    |...|...|...|


- Temps moyen pour l’ensemble des builds pour une période donnée.

    | ID | fromDate | toDate | avgTime |
    | ----------- | ----------- | ---| --- |
    |1         |2023-01-22T19:33:08Z|2023-01-22T19:33:08Z| 36
    |...|...|...|...|

- Quantité de builds réussis et échoués.
  
    | ID | timestamp | totalBuild |successBuild | failBuild | rateBuild |
    | ----------- | ----|--|------- | ---|--|
    |1         |2023-01-23T09:20:08Z|12|8|4|66.66|
    |...|...|...|...|...|...|
  
- Quantité de tests automatisés réussis et échoués.
  
     ID | timestamp | totalTests |successTests | failTests | rateTests |
    | ----------- | ----|--|------- | ---|--|
    |1         |2023-01-23T09:20:08Z|44|32|12|27.27|
    |...|...|...|...|...|...|
