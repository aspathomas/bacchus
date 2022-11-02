from repositories.Repository import Repo

class WineRepository(Repo):
    
    def insertWine(self, nom : str, prenom : str) -> bool :
        print ("test")
        sql = f"""
            INSERT INTO wine
                (prenom, nom)
            VALUES
                ('{nom}', '{prenom}');
        """
        return self.executeInsert(sql)
