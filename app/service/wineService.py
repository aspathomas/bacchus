
import datetime
import uuid
from hashlib import sha1
from random import random
from models.users import Users
from models.wine import Wine
from models.model import db
import jwt
from flask import jsonify

class WineService:

    def getWines(self):
        db_wines = Wine.query.all()
        wines = []
        for i, db_wine in enumerate(db_wines) :
            wines.append(db_wine.to_dict())

        return wines

    def putDescription(self, data: dict):
        if data["user"].is_admin is False:
            return "acces interdit"

        wine = Wine.query.filter_by(id=data["wine_id"]).first()
        wine.description = data["description"]
        db.session.commit()

        return wine.to_dict()
    
    def insert(self, data: dict):
        if data["user"].is_admin is False:
            return "acces interdit"

        if data["nom"] is None or data["region"] is None or data["couleur"] is None or data["est_petillant"] is None or data["prix_moyen"] is None or data["description"] is None :
            return "paramètre manquant"

        wine = Wine(data["nom"], data["region"], data["couleur"], data["description"], data["est_petillant"], data["prix_moyen"])
        db.session.add(wine)
        db.session.commit()

        return wine.to_dict()