from bd_cloud.model.ModelMongoDB import ModelMongoDB

class ControllerMongoDB:

    def __init__(self):
        self.__Connect__ = ModelMongoDB()
    
    def borrarDocumento(self,id):
        return self.__Connect__.borrarDocumento(id)

    def insertarDocumento(self,nombre,angulos,indices,angstrom,difractorgrama,estructura_cristalina):
        data = {
                "nombre": nombre,
                "angulos":angulos,
                "indices":indices,
                "angstrom":angstrom,
                "difractograma":difractorgrama,
                "estructura_cristalina": estructura_cristalina,
                "estado": "CREADO"}
        return self.__Connect__.insertarDocumento(data)

    
    def leerDocumentos(self):
        return self.__Connect__.listarDocumentos()

