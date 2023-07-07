# Création d'une image Docker pour Oxygen-OS

Ce Dockerfile suit un processus en deux étapes : la première étape construit l'image, tandis que la deuxième étape l'exécute.

**Étape 1: Construction**
- Image de base : node:16-alpine.
- Répertoire de travail : /app.
- Copie des fichiers package.json et package-lock.json dans le répertoire de travail.
- Installation des dépendances avec la commande npm ci --only=production.
- Copie du code construit depuis le répertoire dist/ vers le répertoire de travail.

**Étape 2: Exécution**
- Image de base : node:16-alpine.
- Répertoire de travail : /app.
- Copie des fichiers depuis l'étape 1 dans le répertoire de travail.
- Exposition du port souhaité (dans cet exemple, le port 3000).
- Commande de démarrage : node app.js.

Ce Dockerfile permet de créer une image Docker optimisée pour l'application Oxygen-CS, en installant les dépendances nécessaires et en copiant les fichiers appropriés.
