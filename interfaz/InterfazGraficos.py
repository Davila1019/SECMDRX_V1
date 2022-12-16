import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.tix import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import base64

from indice.IndicesMiller import Indice
from patron_difraccion.Patron_U import Patron_U
from calculos.Distancias import Distancias
from calculos.ParametrosRed import ParametrosRed
from patron_teorico.Patron_Teorico import Patron_T
from reportes.Report import Report
from bd_local.controller.ControllerSQLiteBD import ControllerSQLiteBD
from interfaz.InterfazBDCloud import VentanaBDCloud
from interfaz.InterfazBDLocal import VentanaBDLocal

class VentanaGraficos():
    def __init__(self, opc, data:dict):
        self._root = tk.Tk()
        self._root.withdraw()
        self.value = 0
        self.indices = []
        self.angulos = []
        self.intensidades = []
        self.figura = ''
        self.data = data
        self.opc = opc
        self.clas = ''
        

        if self.opc == 1:
            # Tipos de estructuras
            FCC = "Cúbico Centrado en Cara"
            CCC = "Cúbico Centrado en Cuerpo"
            # Instancia Patron Usuario
            self._pdifraccion = Patron_U()
            self._pdifraccion.cargarDatos()  # abrir archivo
            self._pdifraccion.detectar_Picos()
            self.indices = self._pdifraccion.indices_finales
            self.angulos = self._pdifraccion.angulos_dpicos
            self.figura = self._pdifraccion.plt
            self.clas = self._pdifraccion.nombre_clase

            # Instancia clase ParametrosRedRed
            self._param = ParametrosRed()
            self._param.calcularParametrosRed(self.clas)
            # Instancia clase Indice
            print(self._param.tipo_estructura)
            if(self._param.tipo_estructura == FCC):
                self._indice=Indice(self.indices,1)
            elif(self._param.tipo_estructura == CCC) :
                self._indice = Indice(self.indices, 2)
            else:
                self._indice = Indice(self.indices, 3)
            self._indice.crearIndices()




        elif self.opc == 2:
            #Instancia clase Patrón Teorico
            self._pdifraccion = Patron_T()
            print(self.data.__getitem__(1))
            self.angulos = list(self.data.__getitem__(0))
            self.indices = list(self.data.__getitem__(1))
            self.intensidades = list(self.data.__getitem__(2))
            self.value = float(self.data.__getitem__(3))

            self._pdifraccion.angulos = self.angulos
            self._pdifraccion.indicesM = self.indices
            self._pdifraccion.intensidad = self.intensidades
            self._pdifraccion.definir_Pteorico()
            self._pdifraccion.validar_Pteorico()
            self._pdifraccion.graficar_Pteorico()
            self.figura = self._pdifraccion.plt
            self._indice = Indice(self.indices,3)
            self._indice.crearIndices()


    def crearMenu(self):
        menubar = Menu(self._root)

        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label="Nueva simulación", command= self.crearNuevaSimulacion)
        if self.opc == 1:
            filemenu.add_command(label="Crear reporte",command= self.crearReporte)
        filemenu.add_separator()
        filemenu.add_command(label="Guardar simulación",command= self.guardarSimulacion)
        filemenu.add_separator()
        filemenu.add_command(label="Salir",command=self.destroy_window)

        datamenu = Menu(menubar,tearoff=0)
        datamenu.add_command(label="Consultar Simulaciones", command=self.abrirVenataLocal)
        datamenu.add_command(label="Consultar Simulaciones (Nube)", command=self.abrirVentanaNube)

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Consultar",menu=datamenu)
        menubar.add_command(label="Acerca de..", command=self.mostrarDatos)
        

        self._root.config(menu=menubar)



    def crearWidgets(self):

        self._root.iconbitmap("./resourses/images/logo_secmdrx.ico")
        x_ventana = self._root.winfo_screenwidth()
        y_ventana = self._root.winfo_screenheight()
        self._root.geometry("%dx%d" % (x_ventana-200, y_ventana-200))
        self._root.config(bg="#FFFFFF")
        self._root.title('SECMDRX')
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)
        self._disInter = Distancias()
        self._disInter.angstrom = self.value
        self._disInter.angulos = self.angulos
        self._dis = self._disInter.calcularDistancia()

        contador = 0

        figura_difractograma = FigureCanvasTkAgg(self.figura, self._root)
        figura_difractograma.draw()
        figura_difractograma.get_tk_widget().grid(row=0, column=0, rowspan=2, sticky='WENS')

        figura_cristal = FigureCanvasTkAgg(self._indice.plt, self._root)
        figura_cristal.draw()
        figura_cristal.get_tk_widget().grid(row=0, column=1, columnspan=2, sticky='WE')

        toolbarFrame2 = Frame(master=self._root)
        toolbarFrame2.grid(row=2, column=1,columnspan=2)
        toolbar2 = NavigationToolbar2Tk(figura_cristal, toolbarFrame2)
        toolbar2.configure(background='#deedec')
        toolbar2.configure(relief='raised')
        toolbar2.winfo_children()[-1].destroy()
        toolbar2.winfo_children()[6].destroy()
        toolbar2.winfo_children()[-1].configure(background='#deedec')

        toolbarFrame = Frame(master=self._root)
        toolbarFrame.grid(row=2,column=0,)
        toolbar = NavigationToolbar2Tk(figura_difractograma, toolbarFrame)
        toolbar.configure(background='#deedec')
        toolbar.configure(relief='raised')
        toolbar.winfo_children()[-1].destroy()
        toolbar.winfo_children()[6].destroy()
        toolbar.winfo_children()[-1].configure(background='#deedec')

        if self.opc == 1:

            label_struc = Label(master=self._root, borderwidth=1, background='#FFFFFF' ,text='Estructura Cristalina', font=('Times', 12, 'bold'), width=15)
            label_struc.grid(row=3,column=1, columnspan=2)
            frameEstructuras = Frame(master=self._root)
            frameEstructuras.grid(row=4, column=1, columnspan=2)
            frameEstructuras.columnconfigure(0, weight=1)
            frameEstructuras.rowconfigure(0, weight=1)
            label_metal = Label(master=frameEstructuras, borderwidth=1, background='#FFFFFF',
                                text='Material: '+self.clas, font=('Times', 12), width=50)
            label_metal.grid(row=0, column=0, sticky='W')
            label_struc = Label(master=frameEstructuras, borderwidth=1, background='#FFFFFF',
                                text='Tipo de estructura: '+self._param.tipo_estructura, font=('Times', 12), width=50)
            label_struc.grid(row=1, column=0, sticky='W')

            label_radio = Label(master=frameEstructuras, borderwidth=1, background='#FFFFFF',
                                text='Radio Atómico: ' + self._param.radioA.__str__(), font=('Times', 12), width=50)
            label_radio.grid(row=2, column=0, sticky='W')

            label_param = Label(master=frameEstructuras, borderwidth=1, background='#FFFFFF',
                                text='Parámetro de Red: ' + self._param.parametro.__str__(), font=('Times', 12), width=50)
            label_param.grid(row=3, column=0, sticky='W')


        label_listind= Label(master=self._root,height='2', borderwidth=1, background='#FFFFFF' ,text='Indices de Miller', font=('Times', 12, 'bold'), width=15)
        label_listind.grid(row=3,column=0)
        frameIndices = Frame(master=self._root)
        frameIndices.grid(row=4, column=0)
        frameIndices.columnconfigure(0, weight=1)
        frameIndices.rowconfigure(0, weight=1)
        num = Label(master=frameIndices, borderwidth=1, relief='solid', text='No.', font=('Times', 12, 'bold'), width=15)
        indices = Label(master=frameIndices, borderwidth=1, relief='solid', text='hkl', font=('Times', 12, 'bold'), width=15)
        distancias = Label(master=frameIndices, borderwidth=1, relief='solid', text='d [A]', font=('Times', 12, 'bold'), width=15)
        angulos = Label(master=frameIndices, borderwidth=1, relief='solid', text='2Theta[deg]', font=('Times', 12, 'bold'), width=15)
        for i in self.indices:
                auxNum = Label(master=frameIndices, borderwidth=1, text=contador + 1, font=('Times', 12), width=15)
                auxNum.grid(row=contador+1,column=0)
                auxIndices = Label(master=frameIndices, borderwidth=1, text=self.indices[contador], font=('Times', 12,), width=15)
                auxIndices.grid(row=contador+1,column=1)
                auxAngulos = Label(master=frameIndices, borderwidth=1, text=self.angulos[contador], font=('Times', 12,), width=15)
                auxAngulos.grid(row=contador+1,column=2)
                auxDistancias = Label(master=frameIndices, borderwidth=1, text=self._dis[contador], font=('Times', 12,), width=15)
                auxDistancias.grid(row=contador + 1, column=3)
                contador += 1
        distancias.grid(row=0,column=3)
        angulos.grid(row=0, column=2)
        indices.grid(row=0,column=1)
        num.grid(row=0,column=0)
        separator = Label(master=self._root,height='2', borderwidth=1, background='#FFFFFF',foreground='#FFFFFF' ,text='Versión: 1.0.1', font=('Times', 12, 'bold'), width=15)
        separator.grid(row=5,column=0)
        self._root.deiconify()


    def mostrarVentana(self):
        self.crearMenu()  # Creamos la barra de menú
        self.crearWidgets()
        self._root.mainloop()

    def crearReporte(self):
        # Instancia de la clase Report
        self.p = Report('P', 'cm', 'Letter')
        self.p.config()
        self.p.create_pdf(self.clas, self._dis, self.intensidades, self.angulos, self.indices, self._param.radioA, self._param.parametro)

    def guardarSimulacion(self):
        #Instancia de la clase Simulación
        nombre = askstring('Guardar','Introduzca el nombre con el que desea guardar la simulación')
        base_datos = ControllerSQLiteBD()
        if(nombre != 'None' and nombre.isalnum()):
            print(nombre)
            difractograma_img = open('C:/SECMDRX/reports/frames/difractogram.png','rb')
            difractograma_base64 = base64.b64encode(difractograma_img.read())
            estructura_img = open('C:/SECMDRX/reports/frames/crystallographic_planes.png','rb')
            estructura_base64 = base64.b64encode(estructura_img.read())
            
            base_datos.insertarSimulacion(nombre,str(self.angulos),str(self.indices),str(self._disInter.angstrom),difractograma_base64,estructura_base64)
            messagebox.showinfo('Guardar','La simulación se ha guardado con exito!')
            v = VentanaBDLocal()
            del base_datos
        else:
            messagebox.showerror('Error','Ocurrió un error al guardar la información')

    def crearNuevaSimulacion(self):
        from interfaz.InterfazSeleccion import VentanaSeleccion
        ventanaSelect = VentanaSeleccion()

    def abrirVenataLocal(self):
        local = VentanaBDLocal()
    
    def abrirVentanaNube(self):
        nube = VentanaBDCloud()

    def mostrarDatos(self):
        messagebox.showinfo('Acerca de',"El presente sistema SECMDRX fue desarrollado con la participación de los siguientes personas\n\nAlumnos: \nIsmael Cortés Castillo\nJesús Abelardo Dávila Mauricio\n\nDirector del proyecto: Dr. Miguel Fernando Delgado Pamanes\nAsesores: M. en C. Roberto Oswaldo Cruz Leija \nM. en I. Umanel Azazael Hernández González")
 
    def destroy_window(self):
        self._root.destroy()
        