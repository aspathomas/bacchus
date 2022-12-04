from sqlalchemy import (Column, Integer, Float, String,
                        Boolean, DateTime, ForeignKey, Text)
from models.model import db

class Wine(db.Model):
   __tablename__ = 'wine'
   id = db.Column(db.Integer, primary_key=True)
   nom = db.Column(db.String(50))
   region = db.Column(db.String(50))
   couleur = db.Column(db.String(50))
   description = db.Column(db.String(250))
   est_petillant = db.Column(db.Boolean)
   prix_moyen = db.Column(db.Integer)

   def to_dict(self) :
      return {
         "id" : self.id,
         "nom" : self.nom,
         "region" : self.region,
         "couleur" : self.couleur,
         "description" : self.description,
         "est_petillant" : self.est_petillant,
         "prix_moyen" : self.prix_moyen
      }