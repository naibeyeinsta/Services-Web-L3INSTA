from os import environ, path
from dotenv import load_dotenv
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class ConfigDev():
    FLASK_ENV="development"
    TESTING=True,
    DEBUG=True
    SECRET=environ.get("SECRET")
    SQLALCHEMY_DATABASE_URI=environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # Documentation
    APIFAIRY_TITLE="Services Web"
    APIFAIRY_VERSION="1.0"
    APIFAIRY_UI="elements"
class ConfigProd():
    FLASK_ENV="production"
    TESTING=False,
    DEBUG=False
    SECRET=environ.get("SECRET")
    SQLALCHEMY_DATABASE_URI=environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    APIFAIRY_TITLE = "Services Web"
    APIFAIRY_VERSION = "1.0"
    APIFAIRY_UI = "elements"

