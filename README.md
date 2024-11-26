# Application de Critique de Livre avec Django

## Introduction
Cette application est un site web permettant aux utilisateurs de partager leurs avis sur des livres. Développée dans le cadre d'une formation, elle met en œuvre Django pour le backend et PostgreSQL pour la base de données. 

### Fonctionnalités principales
- Création, édition et suppression de critiques de livres.
- Authentification et gestion des utilisateurs.
- Données préremplies pour une exploration rapide.

---

## Prérequis
Avant de commencer, assurez-vous que les logiciels suivants sont installés :
- **Python 3.8+**
- **Django 4.2+**
- **PostgreSQL 15+**

---
## Installation
### 1. Cloner le dépôt
Dans le terminal, exécutez les commandes suivantes pour obtenir le projet :
```bash
git clone https://github.com/S0Imyr/Book_review_django.git
cd Book_review_django
```

### 2. Configurer un environnement virtuel

Créez et activez un environnement virtuel :

- Windows :
    
```bash
python -m venv env
./env/Scripts/activate
```
    
- MacOS/Linux :

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances

Avec l'environnement virtuel activé, installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

## Configuration des Variables d'Environnement

Créez un fichier `.env` dans le dossier racine du projet et ajoutez les variables suivantes :

```
SECRET_KEY = 'votre_cle_secrete'
DEBUG = True
ALLOWED_HOSTS = 'localhost 127.0.0.1'
POSTGRES_USER = 'votre_utilisateur_postgres'
POSTGRES_PASSWORD = 'votre_mot_de_passe_postgres'
POSTGRES_DB = 'nom_de_la_base'
POSTGRES_HOST = localhost

```

- **SECRET_KEY** : Généré depuis [Djecrety](https://djecrety.ir/).
- **POSTGRES_USER** et **POSTGRES_PASSWORD** : Identifiants PostgreSQL.
- **POSTGRES_DB** : Nom de votre base de données.
- **POSTGRES_HOST** : Host de votre base de données.


## Création de la Base de Données

1. **Créer la base de données** :
    
    ```bash
    createdb -O <POSTGRES_USER> <POSTGRES_DB>
    ```
    
2. **Appliquer les migrations** :
Depuis le dossier `src`, exécutez :
    
    ```bash
    cd src
    python manage.py migrate
    ```
    
3. **Alimenter la base de données avec des données initiales** :
    
    ```bash
    python manage.py loaddata authentification/fixtures/auth.json
    python manage.py loaddata review/fixtures/review.json
    ```
    
  - Vous devriez obtenir :
      - **10 utilisateurs créés**.
      - **26 critiques ajoutées**.

💡 *Si des problèmes d'encodage surviennent, vérifiez que les fichiers JSON utilisent l'encodage UTF-8.*

---

## Lancement du Serveur en Local

Pour démarrer l'application :

1. Activez l'environnement virtuel si ce n'est pas déjà fait :
    
    ```bash
    # Windows
    ./env/Scripts/activate
    
    # MacOS/Linux
    source env/bin/activate
    ```
    
2. Lancez le serveur Django :
    
    ```bash
    python manage.py runserver
    ```
    
3. Accédez à l'application à l'adresse : http://localhost:8000/api/

---

## Exploration Rapide

Utilisez les comptes ci-dessous pour tester l'application :

| Utilisateur | Mot de passe      |
|-------------|-------------------|
| johann      | goethegoethe      |
| leon        | tolstoitolstoi    |
| ernest      | hemingway         |

---

## Lancement Ultérieur

Pour les prochains lancements, il suffit de :

1. Activer l'environnement virtuel.
2. Démarrer le serveur :
    
```bash
python manage.py runserver
```

---

## Contributions

Les contributions sont les bienvenues. Pour soumettre vos modifications :

1. Forkez ce dépôt.
2. Créez une branche pour vos modifications :
    
    ```bash
    git checkout -b feature/nouvelle-fonctionnalite
    ```
    
3. Faites une pull request avec une description claire de vos changements.

---

## **Licence**

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
