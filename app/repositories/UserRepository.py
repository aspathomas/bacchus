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
    
    def insertUser(self, userId : int):
        print ("test")
        sql = f"""
            INSERT INTO
            FROM users
            WHERE id = {userId}
        """
        print(sql[0])
        return "e"
