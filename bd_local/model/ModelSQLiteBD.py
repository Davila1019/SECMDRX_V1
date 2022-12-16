import sqlite3

class ModelSQLiteBD:
    def __init__(self):
        try:
            self._conexion = sqlite3.connect("C:\SECMDRX\SECMDRX.db")
            try:
                self.cursor = self._conexion.cursor()
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS simulaciones (
                                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                 nombre VARCHAR(30) NOT NULL,
                                                 angulos VARCHAR(20) NOT NULL,
                                                 indices_miller VARCHAR(25) NOT NULL,
                                                 angstrom INTEGER NOT NULL,
                                                 difractograma BLOB NOT NULL,
                                                 estructura_cristalina BLOB NOT NULL); """)
            except sqlite3.OperationalError:  # Excepción para una tabla ya existente
                print('La tabla ya existe')
        except sqlite3.DatabaseError:
            print('Ocurrió un problema con la base de datos')


    def insertar(self,simulacion):
         try:
            query_param = """INSERT INTO simulaciones (nombre, angulos,indices_miller,angstrom, difractograma, estructura_cristalina ) VALUES ( ?,?,?,?,?,?);"""
            self._conexion.execute(query_param,simulacion)
            self._conexion.commit()

         except sqlite3.OperationalError:
             print("Error en la base de datos")

    def consultar(self):
        self.cursor.execute("""SELECT * FROM simulaciones""")
        data = self.cursor.fetchall()
        return data

    def borrar(self,id_sim):
        try:
            query_param = """DELETE FROM simulaciones WHERE id = ?;"""
            self._conexion.execute(query_param,[id_sim])
            self._conexion.commit() 
            return True
        except:
            return False


if __name__ == "__main__":
    d = ModelSQLiteBD()
    img = open('C:/SECMDRX/reports/frames/crystallographic_planes.png','rb')
    data = ('Hola','20.5,34,25.4','111,122,233','1.5','sfjwkfwl',img)
    d.insertar(data)
    #d.consultar()
