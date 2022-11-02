
from random import random
from repositories.UserRepository import UserRepository
import hashlib


class UserService:

    def insertUser(self, data : dict):
        if data["nom"] is None or data["prenom"] is None or data["email"] is None or data["mdp"] is None:
            print(data)
            return "information manquante"
        
        mdp = data["mdp"]
        mdp = hashlib.md5(mdp.encode())
        print(mdp.hexdigest())

        id = int(random.randint(1,10000))
        UserRepo = UserRepository()
        isInsert = UserRepo.insertUser(id, data["nom"], data["prenom"], data["email"], mdp)
        if isInsert is True: 
            return "reussi"
        
        return "echec"