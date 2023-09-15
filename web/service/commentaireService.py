from models.users import Users
from models.wine import Wine
from models.commentaire import Commentaire
from models.model import db

class CommentaireService:

    def getFromUser(self, user_id : int):
        user = Users.query.filter_by(id=user_id).first

        if user is None:
            return "utilisateur introuvable"

        db_commentaires = Commentaire.query.filter_by(user_id=user_id)
        commentaires = []
        for i, db_commentaire in enumerate(db_commentaires) :
            wine = Wine.query.filter_by(id=db_commentaire.wine_id).first()
            commentaires.append({
                "wine" : wine.to_dict(),
                "note" : db_commentaire.commentaire
            })

        return commentaires

    def getFromWine(self, wine_id : int):
        db_commentaires = Commentaire.query.filter_by(wine_id=wine_id)
        print(db_commentaires)
        wine = Wine.query.filter_by(id=wine_id).first()
        if wine is None :
            return "vin introuvable"

        commentaires = []
        for i, db_commentaire in enumerate(db_commentaires) :
            user = Users.query.filter_by(id=db_commentaire.user_id).first()
            commentaires.append({
                "user" : user.to_short_dict(),
                "commentaire" : db_commentaire.commentaire
            })
        return commentaires

    def insert(self, data : dict):
        if data["user"] is None or data["wine_id"] is None or data["commentaire"] is None:
            return "information manquante"

        wine = Wine.query.filter_by(id=data["wine_id"]).first()
        if wine is None:
            return "vin introuvable"

        commentaire = Commentaire(data["user_id"], data["wine_id"], data["commentaire"])
        db.session.add(commentaire)
        db.session.commit()

        return "reussi"

    def delete(self, data : dict):
    
        if data["user"].is_admin is False:
            return "acces interdit"

        commentaire = Commentaire.query.filter_by(id=data["commentaire_id"]).first()

        db.session.delete(commentaire)
        db.session.commit()

        return "reussi"