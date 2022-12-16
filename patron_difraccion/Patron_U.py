import errno

import os
from tkinter import messagebox as mb

import pandas as pd
from matplotlib.figure import Figure
from scipy.signal import find_peaks, savgol_filter

from archivos.Archivos import Archivos
from clasificador.Knn import Knn


class Patron_U:
    def __init__(self):
        self._angulos_2Theta = []
        self._intensidades = []
        self._indice_picos = []
        self._picos_finales = []
        self._indices_finales = []  # Lista que contiene los indices de miller
        self._clase = {}
        self.nombre_clase = ''
        self._angulos_dpicos = []
        self.plt = None
        self.plt_dif = None
        self._datos_suavizados = []
        self.path = ''

    @property
    def angulos(self):
        return self._angulos_2Theta

    @property
    def angulos_dpicos(self):
        return self._angulos_dpicos

    @angulos.setter
    def angulos(self, angulo):
        self._angulos_2Theta.append(angulo)

    @property
    def intensidad(self):
        return self._intensidades

    @property
    def indices_finales(self):
        return self._indices_finales

    @intensidad.setter
    def intensidad(self, intensidad):
        self._intensidades.append(intensidad)

    def cargarDatos(self):
        a = Archivos()
        try:
            data = a.abrirArchivo()
            self.path = a.archivo
        except KeyError:
            mb.showwarning("Formato invalido", "El archivo seleccionado no tiene el formato valido")
            return self.cargarDatos()
        except FileNotFoundError:
            pass
        try:
            self._angulos_2Theta = data[0]
            self._intensidades = data[1]
        except UnboundLocalError:
            return 0

    def agregar_Picos(self, plt):
        i = 0
        while i < len(self._datos_suavizados):
            j = 0
            while j < len(self._indice_picos):
                if (i == self._indice_picos[j]):
                    plt.text(self._angulos_2Theta[i] + 1, self._intensidades[i] + 50, f'({self._indices_finales[j]})',
                             rotation=45)
                    j += 1
                else:
                    j += 1
            i += 1

    def suavizar_Patron(self):
        data = list(self._intensidades)
        suav_1 = savgol_filter(data, 51, 1)  # Filtro de savitzky–golay X6 (suavizado de señal)
        suav_2 = savgol_filter(suav_1, 51, 1)
        suav_3 = savgol_filter(suav_2, 51, 1)
        suav_4 = savgol_filter(suav_3, 51, 1)
        suaV_5 = savgol_filter(suav_4, 51, 1)
        data_suav = savgol_filter(suaV_5, 51, 1)
        return data_suav

    def detectar_Picos(self):
        try:
            clas = Knn()
            clas.entrenar()
            self._datos_suavizados = self.suavizar_Patron()
            dat_p = pd.DataFrame(self._datos_suavizados)
            des = list(dat_p.std())
            picos_encontrados = find_peaks(self._datos_suavizados, height=(des[0]))
            self._indice_picos = list(picos_encontrados.__getitem__(0))
            self.obtner_Angulos_Picos(self._indice_picos)
            self._clase = clas.clasificar(self._angulos_dpicos)
            self._indices_finales = list(self._clase.values())[0]
            self.nombre_clase = list(self._clase.keys())[0]
            self.graficar_Difractograma()
        except:
            mb.showerror("Error","El archivo que has ingresado tiene un formato inválido o no corresponde a ningún metal conocido")
        # self.plt.show()

    def obtner_Angulos_Picos(self, index_peaks: list):
        tam = len(index_peaks)
        i = 0
        while i < tam:
            self._angulos_dpicos.append(self._angulos_2Theta[self._indice_picos[i]])
            i += 1

    # Función para graficar (pruebas unitarias)
    def graficar_Difractograma(self):
        self.plt = Figure(figsize=(4, 4), dpi=100)
        self.plt_dif = self.plt.add_subplot(111)
        self.plt_dif.plot(self._angulos_2Theta, self._intensidades, c='maroon')
        self.agregar_Picos(self.plt_dif)
        self.plt_dif.set_ylabel('Intensidad(u.a.)')
        self.plt_dif.set_xlabel('2'r'$\theta$(grados)')
        self.plt_dif.set_title(self.nombre_clase)
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

# p = Patron_U()
# p.load_data()
# p.detectar_Picos()
