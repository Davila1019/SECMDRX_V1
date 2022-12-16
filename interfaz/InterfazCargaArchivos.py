import sys
from tkinter import *
import tkinter as tk
import os
from interfaz.InterfazGraficos import VentanaGraficos
from tkinter import messagebox as mb

class VentanaCargaArchivos:

    def __init__(self):
        self.ventana_Carga = Tk()
        self.ventana_Carga.withdraw()
        self.ventana_Carga.title('SECMDRX')
        self.ventana_Carga.iconbitmap("./resourses/images/logo_secmdrx.ico")
        self.ventana_Carga.resizable(False, False)
        width_of_window = 400
        height_of_window = 200
        screen_width = self.ventana_Carga.winfo_screenwidth()
        screen_height = self.ventana_Carga.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.ventana_Carga.geometry(
            "%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        self.bg_azul = "#12636A"
        self.ventana_Carga.configure(background='white')
        self.label_explorar = tk.Label(self.ventana_Carga, font="black", text='Archivo no seleccionado...',
                                       foreground=self.bg_azul, background="white")
        label_angstrom = tk.Label(self.ventana_Carga, font="black", text='Valor Ángstrom: ',
                                       foreground=self.bg_azul, background="white")
        self.angstrom = tk.Entry(self.ventana_Carga, width=10, font="black",
                                 foreground="white", background="#249794", border=False)
        btn_explorar = tk.Button(self.ventana_Carga, text='Abrir Archivo..', command=self.abrirArchivo, width=12,
                                      height=1, background="#249794", foreground="white")
        btn_cerrar = tk.Button(self.ventana_Carga, text="Cancelar", command=self.cancelar, width=12, height=1,
                                    background="#249794", foreground="white")
        btn_guardar = tk.Button(self.ventana_Carga, text="Guardar", command=self.guardarArchivo, width=12, height=1,
                                     background="#249794", foreground="white")
        self.label_explorar.place(x=5, y=20)
        label_angstrom.place(x=10, y=100)
        self.angstrom.place(x=285, y=100)
        btn_explorar.place(x=285, y=15)
        btn_cerrar.place(x=285, y=160)
        btn_guardar.place(x=10, y=160)
        self.ventana_Carga.deiconify()
        #self.ventana_Carga.mainloop()

       # Angstrom debe ser entre 0.1 y 2.5

    def abrirArchivo(self):
        self.v = VentanaGraficos(1, {})
        self.label_explorar.configure(text="Archivo abierto: \n \n" + os.path.split(self.v._pdifraccion.path)[1])


    def guardarArchivo(self):
        valor = self.angstrom.get()
        if validate(valor) == True:
            try:
                self.v.value = float(valor)
                self.ventana_Carga.withdraw()
                self.v.mostrarVentana()
            except AttributeError:
                mb.showinfo('Nota','No has seleccionado ningun archivo, por favor selecciona un archivo')
                self.ventana_Carga.deiconify()
        else:
            mb.showinfo('Nota', 'El valor de Ángstrom es invalido.\nDebe de ser entre .5 y 2.5')
        
    def cancelar(self):
        self.ventana_Carga.destroy()
        from interfaz.InterfazSeleccion import VentanaSeleccion
        self.vetana_Select = VentanaSeleccion()

def validate(valor):
    print(valor.__class__)
    if valor != '' and valor != ' ' and validar_float(valor):
        return True
    else:
        return False

def validar_float(valor):
    try:
        float(valor)
        if (float(valor) >= 0.5 and float(valor) <= 2.5):
            return True
        else:
            return False
    except:
        return False