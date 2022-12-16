import math
#
#       Implementación del algoritmo de clasificación supervisada Knn
#
#              (Clasificación mediante distancia euclidiana)
#
#       Se determinó que el valor de K sería igual al total de elementos dentro de las diferentes
#       listas de indices, esto para que la clasficación tenga un mayor porcentaje de acertación.
#
#

class Knn:
    def __init__(self):
        self._etiquetas = ['Aluminio', 'Cobre', 'Hierro', 'Titanio', 'Metal no reconocido']
        self._distancias = {self._etiquetas[0]: math.inf, self._etiquetas[1]: math.inf, self._etiquetas[2]: math.inf, self._etiquetas[3]: math.inf}
        # self._data = {}
        self._resultados = {}

    def entrenar(self):
        # Índices de miller de Aluminio (Al)
        self._indicesAl = {38.769: '111', 44.716: '002', 65.090: '022', 78.220: '113',
                           82.427: '222'}
        # Índices de miller de Cobre (Cu)
        self._indicesCu = {37: '111', 43: '200', 64: '220', 77: '311'}
        # Índices de miller de Hierro (Fe)
        self._indicesFe = {44.5: '110', 54.954: '200', 82.245: '211', 98.958: '220',
                           116.521: '310'}
        #Indices de miller de Titanio (Ti)
        self._indicesTi = {36.7226:'101', 47.995: '102', 52.7762: '110', 66.42: '103'}

        self._resultados[self._etiquetas[0]] = list(self._indicesAl.values())
        self._resultados[self._etiquetas[1]] = list(self._indicesCu.values())
        self._resultados[self._etiquetas[2]] = list(self._indicesFe.values())
        self._resultados[self._etiquetas[3]] = list(self._indicesTi.values())


    def clasificar(self, picos:list):
        tam = len(picos)
        aux = 0
        if tam == 5:
            aux = 0
            j = 0
            for i in picos:
                aux += math.pow(i - list(self._indicesAl.keys())[j], 2) #Calcular distancias a Aluminio
                j += 1
            aux = math.sqrt(aux)
            self._distancias[self._etiquetas[0]] = aux
            aux = 0
            j = 0
            for i in picos:
                aux += math.pow(i - list(self._indicesFe.keys())[j], 2)#Calcular distancias a Hierro
                j += 1
            aux = math.sqrt(aux)
            self._distancias[self._etiquetas[2]] = aux
        elif tam == 4:
            j = 0
            for i in picos:
                aux += math.pow(i - list(self._indicesCu.keys())[j], 2)#Calcular distancias a Cobre
                j += 1
            aux = math.sqrt(aux)
            self._distancias[self._etiquetas[1]] = aux
            j = 0
            for i in picos:
                aux += math.pow(i - list(self._indicesTi.keys())[j], 2)#Calcular distancias a Titanio
                j += 1
            aux = math.sqrt(aux)
            self._distancias[self._etiquetas[3]] = aux
        else:
            return self._etiquetas[4]

        return self.agregarClase()



    def agregarClase(self):
        distancia_corta = None
        res = {}
        for dist in list(self._distancias.values()):
            if distancia_corta is None or dist < distancia_corta:
                distancia_corta = dist

        if distancia_corta in self._distancias.values():
                clas = list(self._distancias.keys())[list(self._distancias.values()).index(distancia_corta)]
                if clas in self._resultados:
                    res[clas] = self._resultados.get(clas)
        return res
