from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from apifairy import APIFairy

app = Flask('__name__')
app.config.from_object("config.ConfigDev")

bcrypt=Bcrypt(app)
db = SQLAlchemy(app)
ma=Marshmallow(app)
apifairy = APIFairy(app)


from api.utilisateurs import utilisateurs
app.register_blueprint(utilisateurs, url_prefix='/api')

@app.shell_context_processor
def shell_context():  # pragma: no cover
    ctx = {'db': db}
    for attr in dir(models):
        model = getattr(models, attr)
        if hasattr(model, '__bases__') and \
                db.Model in getattr(model, '__bases__'):
            ctx[attr] = model
    return ctx
@app.route("/", methods=["GET"])
def doc():
    return redirect(url_for('apifairy.docs'))

from . import models