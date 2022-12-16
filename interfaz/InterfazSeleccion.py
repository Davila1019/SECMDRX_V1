from tkinter import ttk
from tkinter import *
import tkinter as tk
from interfaz.InterfazCargaArchivos import VentanaCargaArchivos
from interfaz.InterfazCargaDatos import VentanaDatos


class VentanaSeleccion:
    def __init__(self):
        self.ventana_selec = Tk()
        self.ventana_selec.withdraw()
        self.ventana_selec.title('SECMDRX')
        self.ventana_selec.iconbitmap("./resourses/images/logo_secmdrx.ico")
        self.ventana_selec.resizable(False, False)
        self.width_of_window = 250
        self.height_of_window = 150
        self.screen_width = self.ventana_selec.winfo_screenwidth()
        self.screen_height = self.ventana_selec.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.ventana_selec.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.ventana_selec.configure(background='white')
        
        self.bg_azul = '#249794' #Azul
        self.common_fg = '#ffffff'

        self.titulo = tk.Label(self.ventana_selec, text="Datos con los que cuenta: ", background="white", foreground="#249794")
        
        self.btnPad= tk.Button(self.ventana_selec, text="Patrón de difracción", command=self.evento_Pad, width=15, height=1,
                                background="#249794", foreground="white")
        
        self.btnPid= tk.Button(self.ventana_selec, text="Picos de difracción", command=self.evento_Pid, width=15, height=1,
                                background="#249794", foreground="white")
        self.btn_cancelar = tk.Button(self.ventana_selec, text="Cancelar", command=self.ventana_selec.destroy, width=12, height=1,
                                      background="#249794", foreground="white")

        self.titulo.place(x=10, y=10)
        self.btnPad.place(x=70, y=40)
        self.btnPid.place(x=70, y=80)
        self.btn_cancelar.place(x=10, y=120)
        self.ventana_selec.deiconify()
        #self.ventana_selec.mainloop()

    def evento_Pid(self):
        self.ventana_selec.destroy()
        self.data = VentanaDatos()
        
    def evento_Pad(self):
        self.ventana_selec.destroy()
        self.load=VentanaCargaArchivos()
        



