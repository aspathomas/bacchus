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

    def getUsers(self):
        print ("test")
        sql = f"""
            SELECT *
            FROM users
        """
        return self.executeSelect(sql)

    def getUserFromUuid(self, uuid : str):
        print ("test")
        sql = f"""
            SELECT *
            FROM users
            WHERE uuid = {uuid}
            LIMIT 1;
        """
        return self.executeSelect(sql)

    def login(self, email : str, mdp : str):
        sql = f"""
            SELECT *
            FROM users
            WHERE email = '{email}'
            AND mdp = '{mdp}'
            LIMIT 1;
        """
        return self.executeSelect(sql)
    
    def insertUser(self,
        uuid : str,
        nom : str,
        prenom : str,
        email : str,
        mdp : str
    ) -> bool :

        sql = f"""
            INSERT INTO users
                (uuid, prenom, nom, email, mdp)
            VALUES
                ('{uuid}','{nom}', '{prenom}', '{email}', '{mdp}' );
        """
        return self.executeInsert(sql)
