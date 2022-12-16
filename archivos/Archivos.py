from tkinter import filedialog
import pandas as pd

class Archivos:
    def __init__(self):
        self.archivo = []
        self._angulos_2Theta = []
        self._intensidad = []
        self._data = []

    def abrirArchivo(self):
        self.archivo = filedialog.askopenfilename(title="Abrir archivo",
                                        initialdir="C:Documents/",
                                        filetypes=(("Valores separados por comas", "*.csv"),))
        df = pd.read_csv(self.archivo)
        self._angulos_2Theta = df['Angle'].tolist()
        self._intensidad = df['PSD'].tolist()
        self._data.append(self._angulos_2Theta)
        self._data.append(self._intensidad)
        return self._data




