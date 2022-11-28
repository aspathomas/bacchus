
import datetime
import uuid
from hashlib import sha1
from random import random

import jwt
from flask import jsonify
from repositories.UserRepository import UserRepository


class UserService:

    def login(self, data : dict):
        if data["email"] is None or data["mdp"] is None:
            return "information manquante"
        mdp = data["mdp"]
        mdp = mdp.encode()
        mdp = sha1(mdp).hexdigest()

        UserRepo = UserRepository()
        User = UserRepo.login(data["email"], mdp)
        if User is None: 
            return "echec"
        User = User[0]
        token = jwt.encode({'uuid' : User[2], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, '004f2af45d3a4e161a7dd2d17fdae47f')
 
        return jsonify({'token' : token})
        

    def insertUser(self, data : dict):
        if data["nom"] is None or data["prenom"] is None or data["email"] is None or data["mdp"] is None:
            return "information manquante"
        
        mdp = data["mdp"]
        mdp = mdp.encode()
        mdp = sha1(mdp).hexdigest()
        userUuid = uuid.uuid4()

        UserRepo = UserRepository()
        isInsert = UserRepo.insertUser(userUuid, data["nom"], data["prenom"], data["email"], mdp)
        if isInsert is True: 
            return "reussi"
        
        return "echec"