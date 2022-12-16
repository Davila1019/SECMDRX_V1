
from pymongo import MongoClient
from bson.objectid import ObjectId


class ModelMongoDB:
    def __init__(self):
        self.__MONGO_CLUSTER__ = "mongodb+srv://IPN_SECMDRX:Lckh53Nru76Y75VB@secmdrxbd.4imuyid.mongodb.net/?retryWrites=true&w=majority"

    def conectarDB(self):
        try:
            self.__cliente__ = MongoClient(self.__MONGO_CLUSTER__) #Conexión al cluster de mongo db
            self.__db__ = self.__cliente__['SECMDRX']
            return True
        except BaseException:
            return False


    def insertarDocumento(self,data):
        if self.conectarDB() == True:
            print("Insertando documento")
            baseDatos = self.__db__['Simulaciones']
            baseDatos.insert_one(data)
            return True
        else:
            print('Existe un problema al insertar un documento en la Base de Datos')
            return False

    def borrarDocumento(self,id):
        if self.conectarDB() == True:
            print("Borrando documento")
            id = ObjectId(id)
            baseDatos = self.__db__['Simulaciones']
            try:
                data = baseDatos.find_one({"_id": id})
                if data['estado'] != "BORRADO":
                    elim = baseDatos.find_one_and_update({"_id": id},{'$set': {'estado':"BORRADO" }})
                    print(f'Borrado exitoso {elim}')
                    return True
                else:
                    return False
            except BaseException:
                print(Exception.__traceback__)
                return False
        else:
            print('Existe un problema de conexión con la Base de Datos al intentar borrar el documento')

    def listarDocumentos(self):
        datos = []
        if self.conectarDB() == True:
            print("Listando documentos")
            baseDatos = self.__db__['Simulaciones']
            datos = baseDatos.find({'estado': "CREADO" })
            return datos
        else:
            print('Existe un problema de conexión con la Base de Datos al listar los documentos')
            #Generar ventana indicando que no se pudo conectar a la bd
            return datos

if __name__ == '__main__':
    c = ModelMongoDB()
    c.listarDocumentos()
    #c.borrarDocumento("636c1d9705a1247743ebf8e7")

   


