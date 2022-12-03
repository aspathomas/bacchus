from sqlalchemy import (Column, Integer, Float, String,
                        Boolean, DateTime, ForeignKey, Text)
from models.model import db

class Note(db.Model):
   __tablename__ = 'note'
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   wine_id = db.Column(db.Integer, db.ForeignKey('wine.id'), nullable=False)
   note = db.Column(db.Integer)

   def __init__(self, user_id, wine_id, note):
      self.user_id = user_id
      self.wine_id = wine_id
      self.note = note