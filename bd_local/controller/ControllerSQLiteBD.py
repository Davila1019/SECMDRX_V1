from bd_local.model.ModelSQLiteBD import ModelSQLiteBD

class ControllerSQLiteBD:

    def __init__(self):
        self.modelo = ModelSQLiteBD()

    def consultarSimulaciones(self):
        return self.modelo.consultar()

    def insertarSimulacion(self, nombre, angulos, indices, angstrom, difractograma, estructura):
        simulacion = (nombre, angulos, indices, angstrom, difractograma, estructura)
        self.modelo.insertar(simulacion)
    
    def borrarSimulacion(self,id_sim):
        return self.modelo.borrar(id_sim)

if __name__ == "__main__":
    controlador = ControllerSQLiteBD()
    controlador.insertar_Simulacion('Hola','20.5,34,25.4','111,122,233','1.5','sfjwkfwl','saklfdj')

