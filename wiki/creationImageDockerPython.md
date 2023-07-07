# Creation image docker pour Oxygen-CS

Ce Dockerfile a deux étapes : la première construit l'image et la deuxième l'exécute.

**Étape 1: Construction**
- Image : python:3.9 (étiquetée "builder").
- Répertoire : /app.
- Copie requirements.txt.
- Installation des dépendances avec pip install.
- Copie du code source.

**Étape 2: Exécution**
- Image : python:3.9-alpine.
- Répertoire : /app.
- Copie des fichiers depuis l'étape 1.
- Exécution de main.py.

Ce Dockerfile permet de construire une image légère pour exécuter une application Python en installant les dépendances et en copiant les fichiers nécessaires.