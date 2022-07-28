from . import ma
from .models import Utilisateur

class UtilisateurSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Utilisateur
    id=ma.auto_field(required=True, dump_only=True)
    nom=ma.auto_field(required=True)
    prenom=ma.auto_field(required=True)
    telephone = ma.auto_field(required=True)
    motPasse = ma.auto_field(required=True)