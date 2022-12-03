from sqlalchemy import (Column, Integer, Float, String,
                        Boolean, DateTime, ForeignKey, Text)
from models.model import db

class Commentaire(db.Model):
   __tablename__ = 'commentaire'
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   wine_id = db.Column(db.Integer, db.ForeignKey('wine.id'), nullable=False)
   commentaire = db.Column(db.Integer)

   def __init__(self, user_id, wine_id, commentaire):
      self.user_id = user_id
      self.wine_id = wine_id
      self.commentaire = commentaire