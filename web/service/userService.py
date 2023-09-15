
import datetime
import uuid
from hashlib import sha1
from models.users import Users
from models.model import db
import jwt
from flask import jsonify


class UserService:

    def login(self, data : dict):
        if data["email"] is None or data["mdp"] is None:
            return "information manquante"
        mdp = data["mdp"]
        mdp = mdp.encode()
        mdp = sha1(mdp).hexdigest()

        user = Users.query.filter_by(email=data["email"], mdp=mdp).first()

        if user is None: 
           return "echec"

        token = jwt.encode({'uuid' : user.uuid, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, '004f2af45d3a4e161a7dd2d17fdae47f')
        
        return jsonify({'token' : token})
        

    def insertUser(self, data : dict):
        db_users = Users.query.all()
        for db_user in db_users :
            if (db_user.email == data["email"]):
                return "utilisateur déjà présent"

        if data["nom"] is None or data["prenom"] is None or data["email"] is None or data["mdp"] is None:
            return "information manquante"

        mdp = data["mdp"]
        mdp = mdp.encode()
        mdp = sha1(mdp).hexdigest()
        userUuid = uuid.uuid4()

        user = Users(userUuid, data["nom"], data["prenom"], data["email"], mdp)
        db.session.add(user)
        db.session.commit()

        return "reussi"