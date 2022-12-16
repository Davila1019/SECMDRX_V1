from tkinter import *
import base64
from PIL import Image
from os import remove, path
from bd_cloud.controller.ControllerMongoDB import ControllerMongoDB

class VentanaBDCloud():
    def __init__(self):
        self._ventanabd_nube= Tk()
        self._ventanabd_nube.withdraw()
        self._ventanabd_nube.title('SECMDRX - Simulaciones Nube')
        #self._ventanabd_nube.iconbitmap('./resourses/images/logo-ipn.ico')
        self._ventanabd_nube.config(background="white")
        w_frame = Frame(self._ventanabd_nube)
        w_frame.configure(background='white')
        w_frame.pack(fill=BOTH,expand=1)

        w_canvas = Canvas(w_frame)
        w_canvas.configure(background='white')
        w_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        w_scrollbar = Scrollbar(w_frame, orient=VERTICAL, command=w_canvas.yview)
        w_scrollbar.pack(side=RIGHT,fill="y")

    
        w_canvas.configure(yscrollcommand=w_scrollbar.set)
        w_canvas.bind('<Configure>',lambda e: w_canvas.configure(scrollregion=w_canvas.bbox("all")))

        aux_frame =Frame(w_canvas)
        aux_frame.configure(background='white')
        w_canvas.create_window((0,0),window=aux_frame,anchor="nw")

        self._ventanabd_nube.state('zoomed')
        self.bg_azul = '#12636A' #Azul
        self._consulta = ControllerMongoDB()
        data = self._consulta.leerDocumentos()
        auxcontador = 0
        nombre = Label(master=aux_frame, borderwidth=1, text='Nombre', font="balck", background="white", foreground=self.bg_azul, width=15)
        nombre.grid(row=0, column=0,ipadx=25, ipady=3, padx=3, pady=3)
        indices = Label(master=aux_frame, borderwidth=1, text='Indices', font="balck", background="white", foreground=self.bg_azul, width=15)
        indices.grid(row=0, column=1,ipadx=3, ipady=3, padx=3, pady=3)
        angulos = Label(master=aux_frame, borderwidth=1, text='Ángulos',width=15, font="balck", background="white", foreground=self.bg_azul)
        angulos.grid(row=0, column=2,ipadx=3, ipady=3, padx=3, pady=3)
        angstrom = Label(master=aux_frame, borderwidth=1, text='Ángstrom',width=15, font="balck", background="white", foreground=self.bg_azul)
        angstrom.grid(row=0, column=3,ipadx=3, ipady=3, padx=3, pady=3)
        difractograma = Label(master=aux_frame, borderwidth=1, text='Difractograma',width=15, font="balck", background="white", foreground=self.bg_azul)
        difractograma.grid(row=0, column=4,ipadx=3, ipady=3, padx=3, pady=3)
        difractograma = Label(master=aux_frame, borderwidth=1, text='Estructura',width=15, font="balck", background="white", foreground=self.bg_azul)
        difractograma.grid(row=0, column=5,ipadx=3, ipady=3, padx=3, pady=3)
        for d in data:
            auxNombre = Label(master=aux_frame, borderwidth = 1, text=d['nombre'], font="balck", background="white", foreground=self.bg_azul)
            auxNombre.grid(row=auxcontador + 1, column=0,ipadx=3, ipady=3, padx=3, pady=3)
            auxIndices = Label(master=aux_frame, borderwidth = 1, text=d['indices'], font="balck", background="white", foreground=self.bg_azul)
            auxIndices.grid(row=auxcontador + 1, column=1,ipadx=3, ipady=3, padx=3, pady=3)
            auxAngulos = Label(master=aux_frame, borderwidth = 1, text=d['angulos'], font="balck", background="white", foreground=self.bg_azul)
            auxAngulos.grid(row=auxcontador + 1, column=2,ipadx=3, ipady=3, padx=3, pady=3)
            auxAngstrom = Label(master=aux_frame, borderwidth = 1, text=d['angstrom'], font="balck", background="white", foreground=self.bg_azul)
            auxAngstrom.grid(row=auxcontador + 1, column=3,ipadx=3, ipady=3, padx=3, pady=3)
            auxDifractograma = Button(aux_frame, text="Mostrar Difractograma", command=lambda j=d['difractograma']: self.mostrarFigura(j), height=1,
                                background="#249794", foreground="white")
            auxDifractograma.grid(row=auxcontador + 1, column=4,ipadx=3, ipady=3, padx=3, pady=3)
            auxEstructura = Button(aux_frame, text="Mostrar Estructura", command=lambda j=d['estructura_cristalina']: self.mostrarFigura(j), height=1,
                                background="#249794", foreground="white")
            auxEstructura.grid(row=auxcontador + 1, column=5,ipadx=3, ipady=3, padx=3, pady=3)
            
            auxcontador += 1
        self._ventanabd_nube.deiconify()
        #self._ventanabd_nube.mainloop()
    
    def mostrarFigura(self,figura):
        image_64_decode = base64.decodebytes(figura)
        if path.exists("C:/SECMDRX/reports/frames/figura.png"):
            remove('C:/SECMDRX/reports/frames/figura.png')
        image_result = open('C:/SECMDRX/reports/frames/figura.png', 'wb') # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        image_result.close()
        
        im_dif = Image.open('C:/SECMDRX/reports/frames/figura.png')
        im_dif.show()
