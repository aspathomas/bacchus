
import datetime
import uuid
from hashlib import sha1
from random import random
from models.users import Users
from models.wine import Wine
from models.commentaire import Commentaire
from models.model import db
import jwt
from flask import jsonify

class CommentaireService:

    def getFromUser(self, user_id : int):
        db_commentaires = Commentaire.query.filter_by(user_id=user_id)
        user = Users.query.filter_by(id=user_id).first

        if user is None:
            return "utilisateur introuvable"

        commentaires = {}
        for i, db_commentaire in enumerate(db_commentaires) :
            wine = Wine.query.filter_by(id=db_commentaire.wine_id).first
            commentaires[f"""commentaire_{i}"""] = {
                "wine" : wine.to_dict(),
                "note" : db_commentaire.commentaire
            }

        return commentaires

    def getFromWine(self, wine_id : int):
        db_commentaires = Commentaire.query.filter_by(wine_id=wine_id)
        wine = Wine.query.filter_by(id=wine_id).first

        if wine is None:
            return "vin introuvable"

        commentaires = {}
        for i, db_commentaire in enumerate(db_commentaires) :
            user = Users.query.filter_by(id=db_note.user_id).first
            commentaires[f"""commentaire_{i}"""] = {
                "user" : user.to_short_dict(),
                "commentaire" : db_commentaire.note
            }

        return db_commentaire

    def insert(self, data : dict):
        if data["user_id"] is None or data["wine_id"] is None or data["commentaire"] is None:
            return "information manquante"

        user = Users.query.filter_by(id=data["user_id"]).first
        if user is None:
            return "utilisateur introuvable"

        wine = Wine.query.filter_by(id=data["wine_id"]).first
        if wine is None:
            return "vin introuvable"

        commentaire = Commentaire(data["user_id"], data["wine_id"], data["commentaire"])
        db.session.add(commentaire)
        db.session.commit()

        return "reussi"