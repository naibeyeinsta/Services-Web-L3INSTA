from . import db
class Updateable:

    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)
class Utilisateur(db.Model, Updateable):
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(100), nullable=False)
    prenom=db.Column(db.String(50))
    telephone=db.Column(db.String(12), nullable=False,unique=True)
    motPasse=db.Column(db.String(50), nullable=False)