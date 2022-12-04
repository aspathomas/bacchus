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

   def __init__(self, nom, region, couleur, description, est_petillant, prix_moyen):
      self.nom = nom
      self.region = region
      self.couleur = couleur
      self.description = description
      self.est_petillant = est_petillant
      self.prix_moyen = prix_moyen

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