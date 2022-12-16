class ParametrosRed:
    def __init__(self):
        self._parametro = 0
        self._radioA = 0
        self._tipo_estructura = ""

    @property
    def parametro(self):
        return round(self._parametro,4)

    @parametro.setter
    def parametro(self, param):
        self._parametro = param

    @property
    def radioA(self):
        return self._radioA

    @radioA.setter
    def radioA(self, radio):
        self._radioA = radio

    @property
    def tipo_estructura(self):
        return self._tipo_estructura

    @tipo_estructura.setter
    def tipo_estructura(self, type):
        self._tipo_estructura = type

    def calcularParametrosRed(self, metal):
        if metal == 'Aluminio':
            print("Metal Aluminio")
            self._tipo_estructura = "Cúbico Centrado en Cara"
            self._radioA = 0.143
            self._parametro = (4 * self.radioA) / pow(2, 0.5)
        elif metal == 'Titanio':
            print("Metal Titanio")
            self._tipo_estructura = "Cúbico Centrado en Cuerpo"
            self._radioA = 0.144
            self._parametro = (4 * self.radioA) / pow(3, 0.5)
        elif metal == 'Cobre':
            print("Metal Cobre")
            self.tipo_estructura = "Cúbico Centrado en Cara"
            self.radioA = 0.128
            self.parametro = (4 * self.radioA) / pow(2, 0.5)
        elif metal == 'Hierro':
            print("Metal Hierro")
            self.tipo_estructura = "Cúbico Centrado en Cuerpo"
            self.radioA = 0.124
            self.parametro = (4 * self.radioA) / pow(3, 0.5)

