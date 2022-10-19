from repositories.Repository import Repo

class UserRepository(Repo):

    def getUser(self, userId : int):
        print ("test")
        sql = f"""
            SELECT *
            FROM users
            WHERE id = {userId}
        """
        return self.executeSelect(sql)
    
    def insertUser(self, nom : str, prenom : str) -> bool :
        print ("test")
        sql = f"""
            INSERT INTO users
                (prenom, nom)
            VALUES
                ('{nom}', '{prenom}');
        """
        return self.executeInsert(sql)
