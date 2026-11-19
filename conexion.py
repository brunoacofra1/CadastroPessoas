import pymysql

class Conexion:
    
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            charset="utf8mb4"
        )

        

