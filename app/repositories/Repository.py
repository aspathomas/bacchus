from sqlalchemy import Column, Text
import psycopg2

class Repo:

    def executeSelect(self, SQL : str):
        print(SQL)
        try:
                conn = psycopg2.connect(
                
                        host="localhost",
                        database="urbanisation",
                        user="postgres",
                        password="admin2022"
                )
                cur = conn.cursor()
                cur.execute(SQL)

                data = cur.fetchall()
                conn.commit()

                cur.close()
                conn.close()
                print("test2")
                return data
        except Exception:
            return False