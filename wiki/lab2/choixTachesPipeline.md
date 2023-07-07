# Choix des tâches de pipeline
Documentation du pipeline pour package Python :

Ce fichier YAML de pipeline automatise le processus de construction, de vérification de style et de test d'un package Python. Il est déclenché à chaque événement de push dans le dépôt.

## Aperçu du pipeline :

- **Nom :** Package Python
- **Déclencheur :** [push]

## Détails de la tâche :

Le pipeline se compose d'une seule tâche appelée "build". Cette tâche s'exécute sur la dernière version d'Ubuntu et utilise une matrice de stratégie pour définir la version de Python. Ici, la matrice spécifie la version 3.9 de Python.

## Étapes :

1. **Checkout :** Le pipeline récupère le dépôt à l'aide de l'action `actions/checkout`, qui garantit que le pipeline a accès au code le plus récent.

2. **Configuration de l'environnement Python :** Le pipeline utilise l'action `actions/setup-python` pour configurer l'environnement Python. Il spécifie la version de Python en fonction de la configuration de la matrice.

3. **Installation des dépendances :** Cette étape installe les dépendances du projet en exécutant la commande `pip install`. Elle met à jour la version de pip vers la dernière et installe les packages répertoriés dans le fichier `requirements.txt`.

4. **Vérification du style avec pylint :** À cette étape, le pipeline effectue une vérification du style à l'aide de `pylint`, un outil populaire d'analyse de code Python. Il exécute `pylint` sur tous les fichiers Python du dépôt en utilisant la commande `pylint $(git ls-files '*.py')`. Cela garantit que le code respecte des normes de codage et des directives de style spécifiques.

5. **Tests avec unittest :** Le pipeline exécute les tests unitaires à l'aide du framework `unittest`. Il exécute la commande `python -m unittest discover -s test -p "*test.py"` pour découvrir et exécuter tous les fichiers de test correspondant au motif `*test.py` dans le répertoire `test`.

## Justification des choix du pipeline :

1. **Stratégie de matrice :** La stratégie de matrice permet une mise à l'échelle et une flexibilité faciles pour tester le package Python avec différentes versions de Python. En spécifiant `python-version: ["3.9"]` dans la matrice, le pipeline garantit que le package est testé spécifiquement avec Python 3.9.

2. **Vérification du style avec pylint :** L'intégration d'un vérificateur de style comme pylint contribue à maintenir la qualité et la cohérence du code en détectant les problèmes potentiels et en appliquant des normes de codage. Cela encourage les bonnes pratiques, réduit les erreurs et améliore la qualité générale du code.

3. **Tests avec unittest :** En utilisant le framework `unittest`, on dispose d'une solution de test standardisée et intégrée pour Python. Cela permet de créer et d'exécuter des tests unitaires pour valider la fonctionnalité du package.

4. **Installation des dépendances :** En installant les dépendances du projet à partir du fichier `requirements.txt`, le pipeline garantit que les dépendances requises par le package sont correctement installées avant d'exécuter les processus de vérification du style et de test.

Dans l'ensemble, ce pipeline automatise le processus de construction, de vérification du style et de test d'un package Python, facilitant l'assurance qualité du code et garantissant que le package fonctionne comme prévu avec différentes versions de Python. Il favorise la maintenabilité, la fiabilité et le respect des normes de codage.