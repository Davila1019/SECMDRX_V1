import errno
from tkinter import messagebox as mb

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from indice.Cubo import Cubo
import os

class Indice:
    def __init__(self, indices,opc):
        self.plt = None
        self.plt_dif = None
        self.datos = 0
        self.indices = indices
        self.cubo = Cubo(opc)

    def crearGrafico(self):
        self.plt = Figure(figsize=(6, 6), dpi=100)
        self.plt_dif = self.plt.add_subplot(111, projection='3d')
        self.cubo.crearCubo(self.plt, self.plt_dif)
        self.plt_dif.set_zlim(0, 1)
        self.plt_dif.set_xlim(0, 1)
        self.plt_dif.set_ylim(0, 1)

    def crearIndices(self):
        # -----------------------------------------------------------------------
        self.crearGrafico()
        for self.datos in self.indices:
            if self.datos == "111":  # 111
                # pass
                x = np.array([[1, 0, 0, 1]])
                y = np.array([[0, 1, 0, 0]])
                z = np.array([[0, 0, 1, 0]])
                self.plt_dif.scatter(x, y, z, marker='o')
                self.plt_dif.plot_wireframe(x, y, z)
            elif self.datos == "222":
                x = np.array([[1 / 2, 0, 0, 1 / 2]])
                y = np.array([[0, 1 / 2, 0, 0]])
                z = np.array([[0, 0, 1 / 2, 0]])
                self.plt_dif.scatter(x, y, z, marker='o')
                self.plt_dif.plot_wireframe(x, y, z, color='red')
            elif self.datos == "311":
                x = np.array([[1 / 3, 0, 0, 1 / 3]])
                y = np.array([[0, 1, 0, 0]])
                z = np.array([[0, 0, 1, 0]])
                self.plt_dif.scatter(x, y, z, marker='o')
                self.plt_dif.plot_wireframe(x, y, z, color='yellow')
            elif self.datos == "113":
                x = np.array([[1, 0, 0, 1]])
                y = np.array([[0, 1, 0, 0]])
                z = np.array([[0, 0, 1 / 3, 0]])
                self.plt_dif.scatter(x, y, z, marker='o')
                self.plt_dif.plot_wireframe(x, y, z, color='red')
            elif self.datos == "221":
                x = np.array([[1 / 2, 0, 0, 1 / 2]])
                y = np.array([[0, 1 / 2, 0, 0]])
                z = np.array([[0, 0, 1, 0]])
                self.plt_dif.scatter(x, y, z, marker='o')
                self.plt_dif.plot_wireframe(x, y, z, color='red')
            elif self.datos == "110":
                x = np.array([1, 0, 0])
                y = np.array([0, 1, 0])

                x1 = np.array([1, 0, 1])
                y1 = np.array([0, 1, 1])
                np.array([1 / 2, 1 / 2, 1])

                self.plot_vector3dXY([x, y], color='b')
                self.plot_vector3dZ([x1, y1], color='b')
                self.plot_vector3dXZ([x, y], color='b')
            elif self.datos == "310":
                x = np.array([1 / 3, 0, 0])
                y = np.array([0, 1, 0])

                x1 = np.array([1 / 3, 0, 1])
                y1 = np.array([0, 1, 1])

                plt.ylabel("Y")
                plt.xlabel("X")
                self.plot_vector3dXY2([x, y], color='b')

                self.plot_vector3dXZ2([x, y], color='b')
                self.plot_vector3dZ([x1, y1], color='b')
                # pass
            elif self.datos == "101":
                x = np.array([0, 0, 1])
                # y = np.array([1, 0, 0])
                z = np.array([0, 1, 1])

                x1 = np.array([1, 0, 0])
                # y1 = np.array([0, 1, 0])
                z1 = np.array([1, 1, 0])

                # z = np.array([1 / 2, 1 / 2, 1])
                plt.ylabel("Y")
                plt.xlabel("X")
                # self.plot_vector3dXY([x, z], color='b')
                # self.plot_vector3dZ([x,z], color='b')
                # self.plot_vector3dZ([x1, z1], color='g')
                self.plot_vector3dXZ3([x, z], color='r')
                self.plot_vector3dXZ3([x1, z1], color='g')
                self.plot_vector3dXY3([x, z], color='r')
                self.plot_vector3dXY3([x1, z1], color='g')
            elif self.datos == "102":
                x = np.array([0, 0, 1 / 2])
                # y = np.array([1, 0, 0])
                z = np.array([0, 1, 1 / 2])

                x1 = np.array([1, 0, 0])
                # y1 = np.array([0, 1, 0])
                z1 = np.array([1, 1, 0])

                # z = np.array([1 / 2, 1 / 2, 1])
                plt.ylabel("Y")
                plt.xlabel("X")
                # self.plot_vector3dXY([x, z], color='b')
                # self.plot_vector3dZ([x,z], color='b')
                # self.plot_vector3dZ([x1, z1], color='g')
                self.plot_vector3dXZ4([x, z], color='r')
                self.plot_vector3dXZ4([x1, z1], color='g')
                self.plot_vector3dXY3([x, z], color='r')
                self.plot_vector3dXY3([x1, z1], color='g')
            elif self.datos == "200":
                # Decirle a Lalo que se debe cambiar
                x = np.array([1 / 2, 1, 0])
                y = np.array([1/2, 0, 0])
                z1= np.array([1 / 2, 1, 1])

                x1 = np.array([1 / 2, 0, 1])
                z = np.array([1 / 2, 0, 1])
                self.plot_vector3dZ([x, y, z, z1,x1], color='b')
                self.plot_vector3dY([x, y, z, z1,x1], color='b')
            elif self.datos == "220":
                x = np.array([1 / 2, 0, 0])
                y = np.array([0, 1 / 2, 0])

                x1 = np.array([1 / 2, 0, 1])
                y1 = np.array([0, 1 / 2, 1])
                z = np.array([1 / 2, 0, 1])

                # w = np.array([1/2, 1/2, 1])
                # self.plot_vector3dX([x, y, z], color='b')
                # self.plot_vector3dY([x, y, z], color='b')
                self.plot_vector3dXY([x, y], color='b')
                self.plot_vector3dZ([x1, y1], color='b')
                self.plot_vector3dXZ([x, y, z], color='b')
            elif self.datos == "103":
                x = np.array([0, 0, 1 / 3])
                # y = np.array([1, 0, 0])
                z = np.array([0, 1, 1 / 3])

                x1 = np.array([1, 0, 0])
                # y1 = np.array([0, 1, 0])
                z1 = np.array([1, 1, 0])

                # z = np.array([1 / 2, 1 / 2, 1])
                plt.ylabel("Y")
                plt.xlabel("X")
                # self.plot_vector3dXY([x, z], color='b')
                # self.plot_vector3dZ([x,z], color='b')
                # self.plot_vector3dZ([x1, z1], color='g')
                self.plot_vector3dXZ5([x, z], color='r')
                self.plot_vector3dXZ5([x1, z1], color='g')
                self.plot_vector3dXY3([x, z], color='r')
                self.plot_vector3dXY3([x1, z1], color='g')
            elif self.datos == "001":
                x = np.array([1, 0, 1])
                y = np.array([0, 1, 1])
                z = np.array([0, 0, 1])
                w = np.array([1, 1, 1])

                # w = np.array([1/2, 1/2, 1])
                # self.plot_vector3dZ([x, y, z, w], color='b')
                self.plot_vector3dX([x, y, z, w], color='b')
                self.plot_vector3dY([x, y, z, w], color='b')
            elif self.datos == "002":
                x = np.array([1, 0, 1 / 2])
                y = np.array([0, 1, 1 / 2])
                z = np.array([0, 0, 1 / 2])
                w = np.array([1, 1, 1 / 2])

                # w = np.array([1/2, 1/2, 1])
                # self.plot_vector3dZ([x, y, z, w], color='b')
                self.plot_vector3dX([x, y, z, w], color='b')
                self.plot_vector3dY([x, y, z, w], color='b')
            elif self.datos == "011":
                y = np.array([0, 0, 1])
                x = np.array([0, 1, 0])

                y1 = np.array([1, 0, 1])
                z1 = np.array([1, 1, 0])
                plt.ylabel("Y")
                plt.xlabel("X")
                self.plot_vector3dXZ7([y, x], color='r')
                self.plot_vector3dXZ7([y1, z1], color='g')

                self.plot_vector3dXY4([y, x], color='r')
                self.plot_vector3dXY4([y1,z1], color='r')
            elif self.datos == "022":
                y = np.array([0, 0, 1 / 2])
                z = np.array([1, 0, 1 / 2])

                y1 = np.array([1, 1/2, 0])
                z1 = np.array([0, 1/2, 0])

                self.plot_vector3dXZ6([y, z], color='r')
                self.plot_vector3dXZ6([y1, z1], color='g')
                self.plot_vector3dXY4([y, z], color='r')
                self.plot_vector3dXY4([y1, z1], color='r')

        self.guardarFigura()
        # plt.show()

    def plot_vector3dXY4(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([y, x], [y,y], [z, z],
                              linestyle='solid', marker=' ', color= "green")

    def plot_vector3dXZ7(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([x, x], [3/4, y], [1 / 4, z],
                              linestyle='solid', marker=' ',color= "green")
    def plot_vector3dXZ6(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([x, x], [1 / 4, y], [1 / 4, z], color='red',
                              linestyle='solid', marker=' ')

    def plot_vector3dXZ5(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([1 / 4, x], [y, y], [1 / 4, z], color='orange',
                              linestyle='solid', marker=' ')

    def plot_vector3dXZ4(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([1 / 2, x], [y, y], [1 / 4, z], color='red',
                              linestyle='solid', marker=' ')

    def plot_vector3dXY3(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([x, x], [y, x], [z, z],
                              linestyle='solid', marker=' ',color='orange')

    def plot_vector3dXZ3(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([x, z], [y, y], [z, x],
                              linestyle='solid', marker=' ',color='green')

    def plot_vector3dXZ2(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([1 / 4, x], [1 / 4, y], [1, 1],
                              linestyle='solid', marker=' ',color='pink')

    def plot_vector3dXY2(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([1 / 4, x], [1 / 4, y], [0, 0], linestyle='solid', marker=' ',color='blue')

    def plot_vector3dXY(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([x, y], [y, x], [0, 0],
                              linestyle='solid', marker=' ',color='yellow')

    def plot_vector3dXZ(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([x, y], [y, x], [1, 1],
                              linestyle='solid', marker=' ',color='yellow')

    def plot_vector3dZ(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for v in vector_3d:
            x, y, z = v
            self.plt_dif.plot([x, x], [y, y], [0, z],
                              linestyle='solid', marker=' ',color='black')

    def plot_vector3dY(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)

        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for u in vector_3d:
            x, y, z = u
            self.plt_dif.plot([x, x], [0, y], [z, z],
                              linestyle='solid', marker=' ',color='gray')

    def plot_vector3dX(self, vector_3d, **kwords):
        x_coords, y_coords, z_coords = zip(*vector_3d)
        self.plt_dif.scatter(x_coords, y_coords, z_coords, **kwords)
        for w in vector_3d:
            x, y, z = w
            self.plt_dif.plot([0, x], [y, y], [z, z],
                              linestyle='solid', marker=' ', color='gray')

    def guardarFigura(self):
        try:
            self.plt.savefig('C:/SECMDRX/reports/frames/crystallographic_planes.png', bbox_inches='tight')
        except OSError:
            mb.showerror('Error','Ocurrio un error en el sistema')
