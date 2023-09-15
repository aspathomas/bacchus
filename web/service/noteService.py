from models.users import Users
from models.wine import Wine
from models.note import Note
from models.model import db
from flask import jsonify

class NoteService:

    def getFromUser(self, user_id : int):
        user = Users.query.filter_by(id=user_id).first

        if user is None:
            return "utilisateur introuvable"

        db_notes = Note.query.filter_by(user_id=user_id)

        notes = []
        for i, db_note in enumerate(db_notes) :
            wine = Wine.query.filter_by(id=db_note.wine_id).first()
            notes.append({
                "wine" : wine.to_dict(),
                "note" : db_note.note
            })

        return notes

    def getFromWine(self, wine_id : int):
        db_notes = Note.query.filter_by(wine_id=wine_id)
        wine = Wine.query.filter_by(id=wine_id).first()

        if wine is None:
            return "vin introuvable"

        notes = []
        for i, db_note in enumerate(db_notes) :
            user = Users.query.filter_by(id=db_note.user_id).first()
            notes.append({
                "user" : user.to_short_dict(),
                "note" : db_note.note
            })

        return notes

    def insert(self, data : dict):
        print(data)
        if data["user"] is None or data["wine_id"] is None or data["note"] is None:
            return "information manquante"

        wine = Wine.query.filter_by(id=data["wine_id"]).first()
        if wine is None:
            return "vin introuvable"

        note = Note(data["user"].id, data["wine_id"], data["note"])
        db.session.add(note)
        db.session.commit()

        return "reussi"

    def delete(self, data : dict):
        if data["user"].is_admin is False:
            return "acces interdit"

        note = Note.query.filter_by(id=data["note_id"]).first()

        db.session.delete(note)
        db.session.commit()

        return "reussi"