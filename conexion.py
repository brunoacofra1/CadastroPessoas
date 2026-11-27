import pymysql

class Conexion:
   
    def __init__(self):
        self.conn = None
        try :
            self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            charset="utf8mb4",
            autocommit=False,
            ) 
        except pymysql.Error as e :
            print(f"[Erro] não foi possivel fazer a conexao {e}")
        self.database = ""
    def __selecionar_banco(self):
        self.conn.select_db(self.database)

    def criar_banco(self) -> bool:
        if not self.conn:
            return False
        try:
            with self.conn.cursor() as cursor:
                sql = "CREATE DATABASE IF NOT EXISTS pessoas"
                cursor.execute(sql)
                self.conn.commit()
                self.database = "pessoas"
                self.__selecionar_banco()
                if not self.__criar_tabelas():
                    return False
                return True
        except pymysql.Error as e:
            self.conn.rollback()
            print(f"Erro {e}")
            return False    
    def __criar_tabelas(self) -> bool:
        try:
            with self.conn.cursor() as cursor:
                sql = "CREATE TABLE IF NOT EXISTS cadastros(cad_codigo int not null AUTO_INCREMENT,cad_nome varchar(30),cad_altura decimal(4,2),cad_peso decimal(5,2),PRIMARY KEY(cad_codigo))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
                cursor.execute(sql)
                self.conn.commit()
                return True
        except pymysql.Error as e:
            self.conn.rollback()
            print(f"[Erro] {e} não foi possivel realizar a operação")
            return False
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
    def cadastrar_pessoas(self,nome,peso,altura)->bool:
        try:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO cadastros (cad_nome,cad_altura,cad_peso) VALUES(%s,%s,%s)"
                cursor.execute(sql,(nome,altura,peso))
                self.conn.commit()
                return True
        except pymysql.Error as e:
            print(f"[Erro] não foi possivel fazer o cadastro {e}")
            return False
    def listar(self,resultado):  
        for pessoa in resultado:
            print(f"|{pessoa['cad_codigo']:^10}"
                f"|{pessoa['cad_nome']:^15}"
                f"|{pessoa['cad_altura']:^10}"
                f"|{pessoa['cad_peso']:^10}|")
        print(f"Total cadastros: {pessoa['totalcadastros']}")  
    def ver_pessoas(self):
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = "SELECT *,COUNT(cad_codigo) OVER() AS totalcadastros FROM cadastros"
                cursor.execute(sql)
                resultado = cursor.fetchall()
                self.listar(resultado)
        except pymysql.error as e:
            print(f"[Erro ] não foi possivel, {e}")
            return None
    
