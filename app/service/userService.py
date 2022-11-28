
import datetime
import uuid
from hashlib import sha1
from random import random
from models.users import Users
import jwt
from flask import jsonify
#from repositories.UserRepository import UserRepository


class UserService:

    def login(self, data : dict):
        if data["email"] is None or data["mdp"] is None:
            return "information manquante"
        mdp = data["mdp"]
        mdp = mdp.encode()
        mdp = sha1(mdp).hexdigest()

        user = Users.query.filter_by(email=data["email"], mdp=mdp).first()
        print(user)

        if user is None: 
           return "echec"
           
        print(user.uuid)
        token = jwt.encode({'uuid' : user.uuid, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, '004f2af45d3a4e161a7dd2d17fdae47f')
        
        return jsonify({'token' : token})
        

    def insertUser(self, data : dict):
        if data["nom"] is None or data["prenom"] is None or data["email"] is None or data["mdp"] is None:
            return "information manquante"
        
        mdp = data["mdp"]
        mdp = mdp.encode()
        mdp = sha1(mdp).hexdigest()
        userUuid = uuid.uuid4()

        #if isInsert is True: 
        #     return "reussi"
        
        # return "echec"