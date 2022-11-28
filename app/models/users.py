from sqlalchemy import (Column, Integer, Float, String,
                        Boolean, DateTime, ForeignKey, Text)
from models.model import db

class Users(db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   uuid = db.Column(db.Integer)
   nom = db.Column(db.String(50))
   prenom = db.Column(db.String(50))
   email = db.Column(db.String(50))
   mdp = db.Column(db.String(250))
   is_admin = db.Column(db.Boolean)

   def afficher(self) :
      print(self.prenom)
      print(self.nom)

   def to_dict(self) :
      return {
         "id" : self.id,
         "uuid" : self.uuid,
         "nom" : self.nom,
         "prenom" : self.prenom,
         "email" : self.email,
         "mdp" : self.mdp,
         "is_admin" : self.is_admin
      }