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

    def getUsers(self, email : str):
        print ("test")
        sql = f"""
            SELECT *
            FROM users
        """
        return self.executeSelect(sql)
    
    def insertUser(self,
        id : int,
        nom : str,
        prenom : str,
        email : str,
        mdp : str
    ) -> bool :

        print ("test")

        sql = f"""
            INSERT INTO users
                (id, prenom, nom, email)
            VALUES
                ({id},'{nom}', '{prenom}', '{email}', '{mdp}' );
        """
        return self.executeInsert(sql)
