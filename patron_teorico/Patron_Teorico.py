import errno
import pprint
from matplotlib.figure import Figure
import os
from tkinter import messagebox as mb

class Patron_T:
    def __init__(self):
        self._pteorico = dict([])
        self._indices_miller = []
        self._angulos_2Theta = []
        self._intensidad = []
        self.contador = 0.0
        self.plt = None
        self.plt_dif = None

    @property
    def indicesM(self):
        return self._indices_miller

    @indicesM.setter
    def indicesM(self, indiceM):
        self._indices_miller = indiceM

    @property
    def angulos(self):
        return self._angulos_2Theta

    @angulos.setter
    def angulos(self, angulo):
        self._angulos_2Theta = angulo

    @property
    def intensidad(self):
        return self._intensidad

    @intensidad.setter
    def intensidad(self, intensidad):
        self._intensidad = intensidad

    @property
    def pteorico(self):
        return self._pteorico

    def imprimir_pteorico(self):
            pprint.pprint(self._pteorico)

    def definir_Pteorico(self): # definimos un supuesto patrón de difracción teorico
        while self.contador < 90:
            self._pteorico[self.contador] = 0
            self.contador = self.contador + 1

    def validar_Pteorico(self): #validamos la posicion del angulo e insertamos la intesidad
        for angulo in self._pteorico.keys():
            i=0
            while i < len(self._angulos_2Theta):
                if angulo == round(self._angulos_2Theta[i],0):
                    self._pteorico[angulo] = self._intensidad[i]
                    i += 1
                else:
                    i += 1

    def agregar_IndiceM(self,plt):
        for intensidad in self._pteorico.values():
            i=0
            while i < len(self._angulos_2Theta):
                plt.text(self._angulos_2Theta[i],self._intensidad[i], f'{self._indices_miller[i]}')
                i += 1

    def graficar_Pteorico(self): #metódo para la graficación del difractograma
        self.plt = Figure(figsize=(4, 4),dpi=100)
        self.plt_dif = self.plt.add_subplot(111)
        self.plt_dif.plot(self._pteorico.keys(),self._pteorico.values())
        self.plt_dif.set_ylabel('Intensidad(u.a.)')
        self.plt_dif.set_xlabel('2'r'$\theta$(grados)')
        self.plt_dif.set_title('Difractograma R-X')
        self.agregar_IndiceM(self.plt_dif)
        self.guardar_Difractograma()

    def guardar_Difractograma(self):
        try:
            os.makedirs('C:/SECMDRX/reports/frames')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        try:
            self.plt.savefig('C:/SECMDRX/reports/frames/difractogram.png', bbox_inches='tight')
        except OSError:
            mb.showerror('Error', 'Ocurrio un error en el sistema')




