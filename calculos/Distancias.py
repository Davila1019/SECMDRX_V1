import math

import numpy as np


class Distancias:

    def __int__(self):
        self.angulos = []
        self.angstrom = 0

    def angulos(self, ang):
        self.angulos = ang

    def calcularDistancia(self):
        dis = []
        for i in self.angulos:
            angulo = math.radians(float(i) / 2)
            dist = self.angstrom / (2 * math.sin(angulo))
            dis.append(round(dist,4))
        return dis
