import pymysql

class Conexion:

    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            charset="utf8mb4",
            autocommit="false"
        )

    def criar_banco(self) -> bool:
        try:
            with self.conn.cursor() as cursor:
                sql = "CREATE DATABASE IF NOT EXISTS pessoas"
                cursor.execute(sql)
                self.conn.commit()
                return True
        except pymysql.Error as e:
            self.conn.rollback()
            print(f"Erro {e}")
            return False    

