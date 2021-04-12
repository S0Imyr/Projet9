# Projet9

### Principe :
Il s'agit de créer un site internet qui met en relation des utilisateurs pour échanger leurs avis sur des livres. Il est réalisé dans le cadre d'une formation. 

## Installation
### Fichiers du site
Sur le terminal se placer sur un dossier cible.

**Copier les fichiers :**
Sur le terminal tapper successivement :
1. Cloner le dépôt ici présent en tapant: `$ git clone https://github.com/S0Imyr/Projet9.git`
2. Accéder au dossier ainsi créé avec la commande : `$ cd Projet9`
3. Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `$ source env/Scripts/activate` sous windows ou `$ source env/bin/activate` sous MacOS ou Linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`
6. Créer et alimenter la base de données avec la commande `$ python manage.py create_db`
7. Démarrer le serveur avec `$ python manage.py runserver`

Lorsque le serveur fonctionne, après l'étape 7 de la procédure, le site internet est accessible à l'adresse : [http://localhost:8000/home/](http://localhost:8000/home/).

Les étapes 1 à 6 ne sont requises que pout l'installation initiale. Pour les lancements ultérieurs du serveur de l'API, il suffit d'exécuter les étapes 4 et 7 à partir du répertoire racine du projet.

## Arrêter le serveur

Pour arrêter le serveur aller dans le terminal où il a été lancé, puis appuyer sur les touches Ctrl+C.