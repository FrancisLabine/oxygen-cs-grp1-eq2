# Choix des variables d'environnements.

##### Variables locales
| Variable              | Description                                      | Exemple                   |
|-----------------------|--------------------------------------------------|---------------------------|
| TOKEN                 | Jeton d'authentification                          | 'fHtJqgMACx'             |
| HOST                  | Adresse hôte                                     | "HTTP://34.95.34.5"      |
| TICKETS               | Nombre de tickets                                | '3'                       |
| T_MAX                 | Température maximale                             | '28'                      |
| T_MIN                 | Température minimale                             | '19'                      |
| DATABASE              | Nom de la base de données                        | 'OxygenDB'               |
<br>
##### Variables GitHub

| Variable              | Description                                      | Exemple                   |
|-----------------------|--------------------------------------------------|---------------------------|
| TOKEN                 | Jeton secret utilisé pour GitHub                 | ${{secrets.TOKEN}}        |
| HOST                  | Adresse hôte secrète utilisée pour GitHub        | ${{secrets.HOST}}         |
| T_MAX                 | Température maximale secrète utilisée pour GitHub| ${{secrets.T_MAX}}        |
| T_MIN                 | Température minimale secrète utilisée pour GitHub| ${{secrets.T_MIN}}        |
| TICKETS               | Nombre de tickets secret utilisé pour GitHub     | ${{secrets.TICKETS}}      |
| DATABASE              | Nom de la base de données secrète utilisée pour GitHub| ${{secrets.DATABASE}} |
<br>
Les variables d'environnement locales sont spécifiées avec leurs valeurs directement, tandis que les variables GitHub sont définies comme des secrets dans les paramètres de votre référentiel et sont référencées par leurs noms correspondants entre double accolades (par exemple, ${{secrets.TOKEN}}).