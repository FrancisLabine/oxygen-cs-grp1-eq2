# Documentation du pipeline pour la publication d'une image Docker :

Ce pipeline YAML automatise la publication d'une image Docker sur Docker Hub lors d'un push sur la branche "main" du dépôt.

### Aperçu du pipeline :

- **Nom :** Publish Docker image
- **Déclencheur :** [push: branches: [main]]

### Détails de la tâche :

- **Tâche :** push_to_registry
- **Exécution :** ubuntu-latest

### Étapes :

1. **Checkout du dépôt**
2. **Connexion à Docker Hub**
3. **Extraction des métadonnées pour Docker**
4. **Construction et publication de l'image Docker**

Justification des choix du pipeline :

- Déclenchement uniquement sur la branche "main"
- Utilisation d'actions officielles Docker pour la fiabilité
- Utilisation de secrets pour les informations d'identification
- Extraction des métadonnées pour fournir des informations supplémentaires
- Publication de l'image Docker sur Docker Hub

En utilisant ce pipeline, vous pouvez automatiser la publication de votre image Docker, ce qui facilite la diffusion de vos applications ou services via Docker Hub.

## Déploiement des images sur dockerhub

Chacun des déploiement dépose 2 images, une avec le tag du `run_id` de la pipeline qui la déployé et une avec le tag `latest`.
##### Images python
![](image/DockerHub_Python.png)

<br><br>
##### Images node
![](image/DockerHub_Node.png)
