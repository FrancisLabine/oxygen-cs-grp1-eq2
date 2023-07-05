# Choix de base de donnée

Nous avons décider d'utiliser une base de donnée relationnelle local puique l'utilisation qu'on doit en faire ne requiert pas d'avoir une base de donnée centralisé. 
Alors nous y sommes aller avec MySQL afin de rester dans la simplicité.

Il n'y a seulement qu'une table qui servira a contenir les différents snapshots faire par l'api.

##### Colonnes

| Colonne | Explication |
| ----------- | ----------- |
|id| identifiant de l'event|
|timestamp| Date et temps de l'évenement.|
|event| Type d'évenement. Air chaud ou froid.|
|temp| La température qui a causé l'évenement.|
