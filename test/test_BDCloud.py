import unittest
from bd_cloud.model.ModelMongoDB import Conection

class Test_BD_Cloud(unittest.TestCase):
    
    def test_conectionBD(self):
        bd = Conection()
        self.assertEquals(True,bd.conectarDB())

    def test_insertBD(self):
        bd = Conection()
        data = {
                "nombre": "Aluminio",
                "angulos": [23.43,34.83],
                "indices": [112,222],
                "angstrom":1.5,
                "difractograma":"siufhiweefief",
                "estructura_cristalina": "kdsufhhfdihfu",
                "estado": "CREADO"}
        self.assertEquals(True,bd.insertarDocumento(data))

    def test_borrarBD(self):
        bd = Conection()
        self.assertEquals(True,bd.borrarDocumento('636c21ee2ac537b7050e9773'))
    
    def test_listarBD(self):
        bd = Conection()
        self.assertIsNotNone(bd.listarDocumentos())

    

unittest.main(argv=['ignored', '-v'], exit=False)