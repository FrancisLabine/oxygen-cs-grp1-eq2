# Choix des tâches du pipeline pour Oxygen-OS
Ce fichier YAML de pipeline, nommé "Node.js CI", définit un processus continu d'intégration pour une application Node.js. Il est déclenché à chaque événement de push dans le dépôt.

## Aperçu du pipeline :

- **Nom :** Node.js CI
- **Déclencheur :** [push]

## Étapes :

1. **Checkout :** Le pipeline utilise l'action `actions/checkout@v3` pour récupérer le dépôt, assurant ainsi que le code le plus récent est utilisé.

2. **Configuration de l'environnement Node.js :** L'action `actions/setup-node@v3` est utilisée pour configurer l'environnement Node.js. La version de Node.js est spécifiée en utilisant la variable `matrix.node-version`, qui est configurée pour utiliser la version 16.x.

3. **Installation des dépendances :** Cette étape utilise la commande `npm ci` pour installer les dépendances du projet.

4. **Construction :** La commande `npm run build` est exécutée pour effectuer la construction de l'application.

5. **Tests :** La commande `npm test` est exécutée pour exécuter les tests de l'application.

## Justification du pipeline :

1. **Configuration de l'environnement Node.js :** En utilisant `actions/setup-node@v3`, le pipeline peut être configuré pour s'adapter à différentes versions de Node.js. Cela permet de garantir que l'application est testée et fonctionne correctement sur la version spécifiée.

2. **Installation des dépendances :** L'utilisation de `npm ci` assure une installation cohérente des dépendances, en s'assurant que seules les dépendances déclarées dans le fichier `package.json` sont installées. Cela garantit un environnement reproductible et évite les problèmes de compatibilité.

3. **Construction et tests :** Les étapes de construction et de tests permettent de s'assurer que l'application est construite correctement et que les tests sont exécutés pour valider son bon fonctionnement. Cela favorise la qualité du code et la fiabilité de l'application.

Dans l'ensemble, ce pipeline automatise le processus d'intégration continue pour une application Node.js, en incluant des étapes de configuration, d'installation des dépendances, de construction et de tests. Cela permet d'assurer la qualité et la fiabilité de l'application à chaque push effectué dans le dépôt.