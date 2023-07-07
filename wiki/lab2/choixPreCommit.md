# Choix des tâches de pre-commits

Le fichier `pre-commit-config.yaml` configure les hooks utilisés dans le projet :

##### Nous avons 4 tâches distinctes

1. **Pylint**: https://github.com/PyCQA/pylint, v2.17.4, pylint, [--rcfile=.pylintrc]
2. **Flake8**: https://github.com/PyCQA/flake8, 5.0.4, flake8
3. **Black**: https://github.com/psf/black, 22.12.0, black
4. **Trailing Whitespace**: https://github.com/pre-commit/pre-commit-hooks, v4.4.0

Justification des choix :
1. Pylint : détection d'erreurs, formatage, qualité du code
2. Flake8 : vérification de style et qualité du code
3. Black : formatage automatique du code
4. Trailing Whitespace : détection et suppression des espaces inutiles en fin de ligne.

Ces hooks améliorent la qualité, le style et la maintenance du code Python du projet.