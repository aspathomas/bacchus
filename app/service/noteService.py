
import datetime
import uuid
from hashlib import sha1
from random import random
from models.users import Users
from models.wine import Wine
from models.note import Note
from models.model import db
import jwt
from flask import jsonify

class NoteService:

    def getFromUser(self, user_id : int):
        db_notes = Note.query.filter_by(user_id=user_id)
        user = Users.query.filter_by(id=user_id).first

        if user is None:
            return "utilisateur introuvable"

        notes = {}
        for i, db_note in enumerate(db_notes) :
            wine = Wine.query.filter_by(id=db_note.wine_id).first
            notes[f"""note_{i}"""] = {
                "wine" : wine.to_dict(),
                "note" : db_note.note
            }

        return notes

    def getFromWine(self, wine_id : int):
        db_notes = Note.query.filter_by(wine_id=wine_id)
        wine = Wine.query.filter_by(id=wine_id).first

        if wine is None:
            return "vin introuvable"

        notes = {}
        for i, db_note in enumerate(db_notes) :
            user = Users.query.filter_by(id=db_note.user_id).first
            notes[f"""note_{i}"""] = {
                "user" : user.to_short_dict(),
                "note" : db_note.note
            }

        return notes

    def insert(self, data : dict):
        print(data)
        if data["user_id"] is None or data["wine_id"] is None or data["note"] is None:
            return "information manquante"

        user = Users.query.filter_by(id=data["user_id"]).first
        if user is None:
            return "utilisateur introuvable"

        wine = Wine.query.filter_by(id=data["wine_id"]).first
        if wine is None:
            return "vin introuvable"

        note = Note(data["user_id"], data["wine_id"], data["note"])
        db.session.add(note)
        db.session.commit()

        return "reussi"