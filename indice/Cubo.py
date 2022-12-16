from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# Proyeccion cubo
class Cubo:

    def __init__(self,opc):
        self.opcion=opc

    def crearCubo(self, fig, Axes3D):
        self.fig=fig
        self.Axes3D = Axes3D
        a = []
        a.append([1, 1, 1])
        a.append([1, 1, 0])
        a.append([1, 0, 1])
        a.append([0, 1, 1])
        a.append([1, 0, 0])
        a.append([0, 1, 0])
        a.append([0, 0, 1])
        a.append([0, 0, 0])

        # Centrado en cuerpo
        a1 = np.array([1/2, 1/2, 1 / 2])
        # Centrado en caras
        b=[]
        b.append([1 / 2, 1 / 2, 1])
        b.append([0, 1 / 2, 1/2])
        b.append([1/2, 0, 1 / 2])
        b.append([1 / 2, 1/2, 0])
        b.append([1 / 2, 1, 1/2])
        b.append([1, 1/2, 1/2])
        if self.opcion == 1:
            # Cubo
            for i in zip(a):
                # print(f'{i[0]}')
                self.plot_vector3d([i[0]], color='gray')
            # Centrado en Caras
            for i in zip(b):
                # print(f'{i[0]}')
                self.plot_vectorCubo([i[0]])
        elif self.opcion==2:
            # Centrado en cuerpo
            self.plot_vectorCubo([a1])
            # Cubo
            for i in zip(a):
                # print(f'{i[0]}')
                self.plot_vector3d([i[0]], color='gray')
        elif self.opcion == 3:
            # Cubo
            for i in zip(a):
                # print(f'{i[0]}')
                self.plot_vector3d([i[0]], color='gray')
        else:
            print("Esta no es una opción, elija una de las opciones validaz (1,2,3)")

        # plt.show()

    def plot_vector3d(self,vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.Axes3D.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.Axes3D.plot([x, x], [y, y], [0, z],color="gray",
                    linestyle='solid', marker='o',  markersize=10)
        for u in vector_3d:
            x, y, z = u
            self.Axes3D.plot([x, x], [0, y], [z, z],color="gray",
                    linestyle='solid', marker='o', markersize=10)
        for w in vector_3d:
            x, y, z = w
            self.Axes3D.plot([0, x], [y, y], [z, z],color="gray",
                    linestyle='solid', marker='o', markersize=10)

    def plot_vectorCubo(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.Axes3D.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.Axes3D.plot([x, x], [y, y], [z, z],
                    linestyle='solid', marker='o', markersize=40)
# # opcion=1
# p=Cubo()
# print(p.cubo1())