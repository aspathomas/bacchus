from repositories.Repository import Repo

class UserRepository(Repo):
    
    def insertUser(self, nom : str, prenom : str) -> bool :
        print ("test")
        sql = f"""
            INSERT INTO wine
                (prenom, nom)
            VALUES
                ('{nom}', '{prenom}');
        """
        return self.executeInsert(sql)
