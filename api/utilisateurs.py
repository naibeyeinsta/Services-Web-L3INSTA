from flask import Flask,jsonify,request,make_response, Blueprint, abort
from . import bcrypt, db, app
from .models import Utilisateur
from .schemas import UtilisateurSchema
from apifairy import body, response, other_responses
import jwt

utilisateurs=Blueprint("utilisateurs", __name__)
utilisateurSchema=UtilisateurSchema()
utilisateursSchema=UtilisateurSchema(many=True)

@utilisateurs.route('/utilisateurs',methods=['POST'])
@body(utilisateurSchema)
@response(utilisateurSchema)
@other_responses({401:"telephone deja enregistre" })
def post(data):
    # data=request.get_json()
    utilisateurExist=Utilisateur.query.filter_by(telephone=data['telephone']).first()
    if utilisateurExist:
        abort(401)
    hashed=bcrypt.generate_password_hash(data['motPasse'])
    nouveauUtilisateur=Utilisateur(nom=data['nom'],prenom=data['prenom'],telephone=data['telephone'],motPasse=hashed)
    db.session.add(nouveauUtilisateur)
    db.session.commit()
    return nouveauUtilisateur
@utilisateurs.route('/utilisateurs',methods=['GET'])
@response(utilisateursSchema)
def getAll():
    utilisateurs= Utilisateur.query.all()
    return utilisateurs

@utilisateurs.route('/utilisateurs',methods=['PUT'])
@body(utilisateurSchema)
def update(utilisateur_actuel,data):
    utilisateur=utilisateur_actuel
    utilisateur.update(data)
    return jsonify({'message':'Utilisateur mise a jour avec succes','Utilisateur':{'id':utilisateur.id,'nom':utilisateur.nom,'prenom':utilisateur.prenom}})
@utilisateurs.route('/utilisateurs/<id>',methods=['DELETE'])
def delete(id):
    utilisateur=Utilisateur.query.get(id)
    db.session.delete(utilisateur)
    db.session.commit()
    return jsonify({'message':'utilisateur id='+ str(id)+'supprimer avec succes'})
@utilisateurs.route('/authentification',methods=['POST'])
def authentification():
    data=request.get_json()
    if not data['telephone'] or not data['motPasse']:
        return make_response("Authentification echoue")
    utilisateur=Utilisateur.query.filter_by(telephone=data['telephone']).first()
    if not utilisateur:
        return make_response('telephone non attribue',401)
    if not bcrypt.check_password_hash(utilisateur.motPasse,data['motPasse']):
        return jsonify({'message':'mot de passe incorrect'})
    token= jwt.encode({'nom': utilisateur.nom,'prenom': utilisateur.prenom,'telephone': utilisateur.telephone},app.config['secret'],algorithm='HS256')
    return jsonify({'message':'Utilisateur authentifie avec succes','token':token})

db.create_all()