# Services Web avec Flask

##  Creation de l'environnement virtuel 
Utilisez un environnement virtuel pour gérer les dépendances de votre projet, tant en développement qu'en production.

#### Quel problème un environnement virtuel résout-il ? 

Plus vous avez de projets Python, plus il est probable que vous deviez travailler avec différentes versions des bibliothèques Python, voire de Python lui-même. Des versions plus récentes de bibliothèques pour un projet peuvent rompre la compatibilité dans un autre projet.

Les environnements virtuels sont des groupes indépendants de bibliothèques Python, un pour chaque projet. Les paquets installés pour un projet n'affecteront pas les autres projets ou les paquets du système d'exploitation.

Python est fourni avec le module venv pour créer des environnements virtuels.

Sous windows:

```py -3 -m venv venv```

Sous linux ou mac:

```python3 -m venv venv```

#### Activate the environment

Avant de travailler sur votre projet, activez l'environnement correspondant :

sous Windows:

```> venv\Scripts\activate```

sous mac ou linux

```$ . venv/bin/activate```

## Organisation du projet

Créer un dossier nommé api dans le dossier principal de votre projet:


```mkdir api```

Positionner vous dans le dossier api

```cd api```

Créer les fichiers: 

```__init__.py```

```models.py```


### Installation dotenv
``` $ pip install python-dotenv```


```from os import environ, path
from dotenv import load_dotenv
import os
import json
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))```


```class DevConfig():
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SECRET=environ.get('SECRET')
    SESSION_TYPE='sqlalchemy'
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

```app.config.from_object("config.DevConfig")```