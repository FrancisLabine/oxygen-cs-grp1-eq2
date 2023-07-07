# Tests pour oxygenCS

Pour les tests, nous utilisons unittest. Nous testons d'abord les variables d'environnement.
Lorsque les variables sont pré-définies, il n'y a aucun action.
Lorsque les variables ne sont pas pré-définies, elles sont initialisé avec une valeur par défaut.
Seulement la variable TOKEN doit être existante, sinon l'application ne fonctionne pas.

Nous testons ensuite chacune des fonctions qui sont utilisé pour analyser les données sortit de oxygen-CS.
Nous nous assurons que les données sont bien analyser et que les appels soit respectés (augmenter/baisser température et ne rien faire).
Nous nous assurons que la fonction pour enregistrer l'évènement dans la BD spot appelée lorsqu'il y a une nouvelle action d'exécutée.