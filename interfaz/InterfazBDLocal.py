import base64
from tkinter import *
from os import remove,path
from PIL import Image
from tkinter import messagebox
from bd_local.controller.ControllerSQLiteBD import ControllerSQLiteBD
from bd_cloud.controller.ControllerMongoDB import ControllerMongoDB

class VentanaBDLocal():
    def __init__(self):
        self._ventanabd_local= Tk()
        self._ventanabd_local.withdraw()
        self._ventanabd_local.title('SECMDRX - Tus Simulaciones')
        #self._ventanabd_local.iconcbitmap('./resourses/images/logo-ipn.ico')
        w_frame = Frame(self._ventanabd_local)
        w_frame.configure(background='white')
        w_frame.pack(fill=BOTH,expand=1)

        w_canvas = Canvas(w_frame)
        w_canvas.configure(background='white')
        w_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        w_scrollbar = Scrollbar(w_frame, orient=VERTICAL, command=w_canvas.yview)
        w_scrollbar.pack(side=RIGHT,fill=Y)

    
        w_canvas.configure(yscrollcommand=w_scrollbar.set)
        w_canvas.bind('<Configure>',lambda e: w_canvas.configure(scrollregion=w_canvas.bbox("all")))

        aux_frame =Frame(w_canvas)
        aux_frame.configure(background='white')
        w_canvas.create_window((0,0),window=aux_frame,anchor="nw")

        self._ventanabd_local.config(bg='white')
        self._ventanabd_local.state('zoomed')
        
        self.bg_azul = '#12636A' #Azul
        self._consulta = ControllerSQLiteBD()
        data = self._consulta.consultarSimulaciones()
        auxcontador = 0
        
        id = Label(master=aux_frame, borderwidth=1, text='ID', font="balck", background="white", foreground=self.bg_azul, width=5)
        id.grid(row=0, column=0,ipadx=3, ipady=3, padx=3, pady=3)
        nombre = Label(master=aux_frame, borderwidth=1, text='Nombre', font="balck", background="white", foreground=self.bg_azul, width=15)
        nombre.grid(row=0, column=1,ipadx=3, ipady=3, padx=3, pady=3)
        indices = Label(master=aux_frame, borderwidth=1, text='Indices', font="balck", background="white", foreground=self.bg_azul, width=15)
        indices.grid(row=0, column=2,ipadx=3, ipady=3, padx=3, pady=3)
        angulos = Label(master=aux_frame, borderwidth=1, text='Ángulos',width=15, font="balck", background="white", foreground=self.bg_azul)
        angulos.grid(row=0, column=3,ipadx=3, ipady=3, padx=3, pady=3)
        angstrom = Label(master=aux_frame, borderwidth=1, text='Ángstrom',width=15, font="balck", background="white", foreground=self.bg_azul)
        angstrom.grid(row=0, column=4,ipadx=3, ipady=3, padx=3, pady=3)
        difractograma = Label(master=aux_frame, borderwidth=1, text='Difractograma',width=15, font="balck", background="white", foreground=self.bg_azul)
        difractograma.grid(row=0, column=5,ipadx=3, ipady=3, padx=3, pady=3)
        difractograma = Label(master=aux_frame, borderwidth=1, text='Estructura',width=15, font="balck", background="white", foreground=self.bg_azul)
        difractograma.grid(row=0, column=6,ipadx=3, ipady=3, padx=3, pady=3)
        acciones = Label(master=aux_frame, borderwidth=1, text='Acciones',width=15, font="balck", background="white", foreground=self.bg_azul)
        acciones.grid(row=0, column=7,ipadx=3, ipady=3, padx=3, pady=3, columnspan=2)
        for d in data:
            auxId = Label(master=aux_frame,borderwidth = 1, text=d[0], font="balck", background="white", foreground=self.bg_azul)
            auxId.grid(row=auxcontador + 1, column=0,ipadx=3, ipady=3, padx=3, pady=3)
            auxNombre = Label(master=aux_frame, borderwidth = 1, text=d[1], font="balck", background="white", foreground=self.bg_azul)
            auxNombre.grid(row=auxcontador + 1, column=1, ipadx=3, ipady=3, padx=3, pady=3)
            auxIndices = Label(master=aux_frame, borderwidth = 1, text=d[2], font="balck", background="white", foreground=self.bg_azul)
            auxIndices.grid(row=auxcontador + 1, column=2,ipadx=3, ipady=3, padx=3, pady=3)
            auxAngulos = Label(master=aux_frame, borderwidth = 1, text=d[3], font="balck", background="white", foreground=self.bg_azul)
            auxAngulos.grid(row=auxcontador + 1, column=3,ipadx=3, ipady=3, padx=3, pady=3)
            auxAngstrom = Label(master=aux_frame, borderwidth = 1, text=d[4], font="balck", background="white", foreground=self.bg_azul)
            auxAngstrom.grid(row=auxcontador + 1, column=4,ipadx=3, ipady=3, padx=3, pady=3)
            auxDifractograma = Button(aux_frame, text="Mostrar Difractograma", command=lambda j=d[5]: self.mostrarFigura(j), height=1,
                                background="#249794", foreground="white")
            auxDifractograma.grid(row=auxcontador + 1, column=5,ipadx=3, ipady=3, padx=3, pady=3)
            auxEstructura = Button(aux_frame, text="Mostrar Estructura", command=lambda j=d[6]: self.mostrarFigura(j), height=1,
                                background="#249794", foreground="white")
            auxEstructura.grid(row=auxcontador + 1, column=6,ipadx=3, ipady=3, padx=3, pady=3)
            auxBorrar = Button(aux_frame, text="Borrar", command=lambda j=str(d[0]): self.eliminarRegistro(j), height=1,
                                background="#249794", foreground="white")
            auxBorrar.grid(row=auxcontador + 1, column=8,ipadx=3, ipady=3, padx=3, pady=3)

            auxInsertar = Button(aux_frame, text="Agregar a Nube", command=lambda nombre=d[1],indices=d[2],angulos=d[3],angstrom=d[4],difractograma=d[5],estructura=d[6]: self.agregarRegistroNube(nombre,indices,angulos,angstrom,difractograma,estructura), height=1,
                                background="#249794", foreground="white")
            auxInsertar.grid(row=auxcontador + 1, column=7,ipadx=3, ipady=3, padx=3, pady=3)
            auxcontador += 1
        self._ventanabd_local.deiconify()
        #self._ventanabd_local.mainloop()

    def mostrarFigura(self,figura): 
        image_64_decode = base64.decodebytes(figura)
        if path.exists("C:/SECMDRX/reports/frames/figura.png"):
            remove('C:/SECMDRX/reports/frames/figura.png')
        image_result = open('C:/SECMDRX/reports/frames/figura.png', 'wb') # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        image_result.close()
        
        im_dif = Image.open('C:/SECMDRX/reports/frames/figura.png')
        im_dif.show()

    def agregarRegistroNube(self,nombre,indices,angulos,angstrom,difractograma,estructura):
        mongoInsert = ControllerMongoDB()
        if mongoInsert.insertarDocumento(nombre,indices,angulos,angstrom,difractograma,estructura) == True:
            messagebox.showinfo("Guardado exitoso","El registro se ha guardado exitosamente en la Nube")
        else:
             messagebox.showerror("Error","Ocurrió un error al agregar el registro, intente de nuevo")

    def eliminarRegistro(self,id_sim):
        if self._consulta.borrarSimulacion(id_sim) == True:
            messagebox.showinfo("Borrado exitoso","El registro ha sido borrado exitosamente")
            self._ventanabd_local.destroy()
            self._ventanabd_local = VentanaBDLocal()
        else:
            messagebox.showerror("Error","Ocurrió un error al borrar el registro, intente de nuevo")
        