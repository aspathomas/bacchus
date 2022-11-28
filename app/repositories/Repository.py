import psycopg2
from sqlalchemy import Column, Text, true


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
                return data
        except Exception:
            return False

    def executeInsert(self, SQL : str):
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
                conn.commit()

                cur.close()
                conn.close()
                return True
        except Exception:
            return False