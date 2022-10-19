from sqlalchemy import Column, Integer, Text
from models.model import ModelTemplate

class User(ModelTemplate):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    email = Column(Text)

    def getUser(self, userId : int):
        sql = f"""
            SELECT *
            FROM users
            WHERE id = {userId}
        """
        return self.executeSQL(sql)
