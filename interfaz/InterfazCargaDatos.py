import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from interfaz.InterfazGraficos import VentanaGraficos
class VentanaDatos:
    def __init__(self):

        self.combo_indice = None
        self.indices = []
        self.angulos = []
        self.intensidades = []
        self.datos = {}
        self.ventana_cargadatos = Tk()
        self.ventana_cargadatos.withdraw()
        self.ventana_cargadatos.title('SECMDRX')
        self.ventana_cargadatos.iconbitmap("./resourses/images/logo_secmdrx.ico")
        self.ventana_cargadatos.resizable(False, False)
        width_of_window = 670
        height_of_window = 300
        screen_width = self.ventana_cargadatos.winfo_screenwidth()
        screen_height = self.ventana_cargadatos.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.ventana_cargadatos.geometry(
            "%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        self.ventana_cargadatos.configure(background='white')
        vcmd = (self.ventana_cargadatos.register(validate), '%S', '%P')
        bg_azul = '#249794'  # Azul
        
        label_titulo = ttk.Label(self.ventana_cargadatos, font="black", text="Agregar picos de difracción ",
                                      background="white",
                                      foreground=bg_azul)
        btn_agregar = tk.Button(self.ventana_cargadatos, text="+", command=self.agregarDatos,
                                     width=7, height=1,
                                     background="#249794", foreground="white")
        self.entry_angstrom = tk.Entry(self.ventana_cargadatos, width=10, font="black",
                                       foreground="white", background="#249794", border=False, validate='key',
                                       validatecommand=vcmd)
        label_angstrom = ttk.Label(self.ventana_cargadatos, font="black", text="Valor de Ángstrom",
                                        background="white",
                                        foreground=bg_azul)
        btn_aceptar = tk.Button(self.ventana_cargadatos, text="Aceptar", command=self.aceptarDatos, width=12,
                                     height=1,
                                     background="#249794", foreground="white")
        btn_cancelar = tk.Button(self.ventana_cargadatos, text="Cancelar", command=self.cancelar, width=12, height=1,
                                      background="#249794", foreground="white")
        # Eliminar Externo
        self.btn_eliminar = tk.Button(self.ventana_cargadatos, text="X", command=self.eliminarDatos, width=7,
                                      height=1,
                                      background="#249794", foreground="white")
        # self.Barra = tk.Scale(self.int2, from_=0, to=42)
        # self.Barra.place(x=450,y=50)
        self.posicion = 50
        self.click = 1
        btn_agregar.place(x=600, y=10)
        label_titulo.place(x=10, y=10)
        self.entry_angstrom.place(x=570, y=220)
        label_angstrom.place(x=400, y=220)
        btn_aceptar.place(x=560, y=270)
        btn_cancelar.place(x=460, y=270)
        self.btn_eliminar.place(x=530, y=10)
        self.ventana_cargadatos.deiconify()
        #self.ventana_cargadatos.mainloop()

    def agregarDatos(self):
        if self.click == 1:

            vcmd = (self.ventana_cargadatos.register(validate), '%S', '%P')
            entry_pico = StringVar()
            entry_inten = StringVar()
            self.entry_pico = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                       background="#249794",
                                       border=False, validate='key', validatecommand=vcmd, textvariable=entry_pico)

            self.label_pico = tk.Label(self.ventana_cargadatos, font='black', text='Angulo del pico', background="white",
                                       foreground="#249794")
            self.label_indice = tk.Label(self.ventana_cargadatos, font='black', text='Indice de Miller',
                                         background="white",
                                         foreground="#249794")
            self.combo_indice = ttk.Combobox(self.ventana_cargadatos, values=["111", "002", "022", "113", "222",
                                                                           "200", "220", "311", "110",
                                                                           "211", "310", "101", "102", "103"], width=10,
                                             validate='key', validatecommand=vcmd, state="readonly")
            self.entry_intensity = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                            background="#249794",
                                            border=False, validate='key', validatecommand=vcmd, textvariable=entry_inten)

            self.label_intensity = tk.Label(self.ventana_cargadatos, font='black', text='Intensidad', background="white",
                                            foreground="#249794")

            self.combo_indice.current(0)
            self.label_pico.place(x=10, y=self.posicion)
            self.entry_pico.place(x=140, y=self.posicion)
            self.label_indice.place(x=250, y=self.posicion)
            self.combo_indice.place(x=380, y=self.posicion)
            self.label_intensity.place(x=480, y=self.posicion)
            self.entry_intensity.place(x=570, y=self.posicion)
            entry_pico.trace("w", lambda *args: limiter(entry_pico))
            entry_inten.trace("w", lambda *args: validator_intensity(entry_inten))
            self.click += 1
            self.posicion += 30
        elif self.click == 2:
            vcmd = (self.ventana_cargadatos.register(validate), '%S', '%P')
            entry_pico = StringVar()
            entry_inten = StringVar()
            self.entry_pico2 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                        background="#249794",
                                        border=False, validate='key', validatecommand=vcmd, textvariable=entry_pico)
            self.label_pico2 = tk.Label(self.ventana_cargadatos, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice2 = tk.Label(self.ventana_cargadatos, font='black', text='Indice de Miller',
                                          background="white",
                                          foreground="#249794")
            self.combo_indice2 = ttk.Combobox(self.ventana_cargadatos, values=["111", "002", "022", "113", "222",
                                                                            "200", "220", "311", "110",
                                                                            "211", "310", "101", "102", "103"],
                                              width=10, validate='key',
                                              validatecommand=vcmd, state="readonly")
            self.entry_intensity2 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                             background="#249794",
                                             border=False, validate='key', validatecommand=vcmd, textvariable=entry_inten)

            self.label_intensity2 = tk.Label(self.ventana_cargadatos, font='black', text='Intensidad', background="white",
                                             foreground="#249794")
            self.combo_indice2.current(0)
            self.label_pico2.place(x=10, y=self.posicion)
            self.entry_pico2.place(x=140, y=self.posicion)
            self.label_indice2.place(x=250, y=self.posicion)
            self.combo_indice2.place(x=380, y=self.posicion)
            self.label_intensity2.place(x=480, y=self.posicion)
            self.entry_intensity2.place(x=570, y=self.posicion)
            entry_pico.trace("w", lambda *args: limiter(entry_pico))
            entry_inten.trace("w", lambda *args: validator_intensity(entry_inten))
            self.click += 1
            self.posicion += 30
        elif self.click == 3:
            entry_pico = StringVar()
            entry_inten = StringVar()
            vcmd = (self.ventana_cargadatos.register(validate), '%S', '%P')
            self.entry_pico3 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                        background="#249794",
                                        border=False, validate='key', validatecommand=vcmd, textvariable=entry_pico)
            self.label_pico3 = tk.Label(self.ventana_cargadatos, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice3 = tk.Label(self.ventana_cargadatos, font='black', text='Indice de Miller',
                                          background="white",
                                          foreground="#249794")
            self.combo_indice3 = ttk.Combobox(self.ventana_cargadatos, values=["111", "002", "022", "113", "222",
                                                                            "200", "220", "311", "110",
                                                                            "211", "310", "101", "102", "103"],
                                              width=10, validate='key',
                                              validatecommand=vcmd, state="readonly")
            self.entry_intensity3 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                             background="#249794",
                                             border=False, validate='key', validatecommand=vcmd, textvariable=entry_inten)

            self.label_intensity3 = tk.Label(self.ventana_cargadatos, font='black', text='Intensidad', background="white",
                                             foreground="#249794")

            self.combo_indice3.current(0)
            self.label_pico3.place(x=10, y=self.posicion)
            self.entry_pico3.place(x=140, y=self.posicion)
            self.label_indice3.place(x=250, y=self.posicion)
            self.combo_indice3.place(x=380, y=self.posicion)
            self.label_intensity3.place(x=480, y=self.posicion)
            self.entry_intensity3.place(x=570, y=self.posicion)
            entry_pico.trace("w", lambda *args: limiter(entry_pico))
            entry_inten.trace("w", lambda *args: validator_intensity(entry_inten))
            self.click += 1
            self.posicion += 30
        elif self.click == 4:
            entry_pico = StringVar()
            entry_inten = StringVar()
            vcmd = (self.ventana_cargadatos.register(validate), '%S', '%P')
            self.entry_pico4 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                        background="#249794",
                                        border=False, validate='key', validatecommand=vcmd, textvariable=entry_pico)
            self.label_pico4 = tk.Label(self.ventana_cargadatos, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice4 = tk.Label(self.ventana_cargadatos, font='black', text='Indice de Miller',
                                          background="white",
                                          foreground="#249794")
            self.combo_indice4 = ttk.Combobox(self.ventana_cargadatos, values=["111", "002", "022", "113", "222",
                                                                            "200", "220", "311", "110",
                                                                            "211", "310", "101", "102", "103"],
                                              width=10, validate='key',
                                              validatecommand=vcmd, state="readonly")
            self.entry_intensity4 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                             background="#249794",
                                             border=False, validate='key', validatecommand=vcmd, textvariable=entry_inten)

            self.label_intensity4 = tk.Label(self.ventana_cargadatos, font='black', text='Intensidad', background="white",
                                             foreground="#249794")
            self.combo_indice4.current(0)
            self.label_pico4.place(x=10, y=self.posicion)
            self.entry_pico4.place(x=140, y=self.posicion)
            self.label_indice4.place(x=250, y=self.posicion)
            self.combo_indice4.place(x=380, y=self.posicion)
            self.label_intensity4.place(x=480, y=self.posicion)
            self.entry_intensity4.place(x=570, y=self.posicion)
            entry_pico.trace("w", lambda *args: limiter(entry_pico))
            entry_inten.trace("w", lambda *args: validator_intensity(entry_inten))
            self.click += 1
            self.posicion += 30
        elif self.click == 5:
            entry_pico = StringVar()
            entry_inten = StringVar()
            vcmd = (self.ventana_cargadatos.register(validate), '%S', '%P')
            self.entry_pico5 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                        background="#249794",
                                        border=False, validate='key', validatecommand=vcmd, textvariable=entry_pico)
            self.label_pico5 = tk.Label(self.ventana_cargadatos, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice5 = tk.Label(self.ventana_cargadatos, font='black', text='Indice de Miller',
                                          background="white",
                                          foreground="#249794")
            self.combo_indice5 = ttk.Combobox(self.ventana_cargadatos, values=["111", "002", "022", "113", "222",
                                                                            "200", "220", "311", "110",
                                                                            "211", "310", "101", "102", "103"],
                                              width=10, validate='key',
                                              validatecommand=vcmd, state="readonly")
            self.entry_intensity5 = tk.Entry(self.ventana_cargadatos, width=10, font="black", foreground="white",
                                             background="#249794",
                                             border=False, validate='key', validatecommand=vcmd, textvariable=entry_inten)

            self.label_intensity5 = tk.Label(self.ventana_cargadatos, font='black', text='Intensidad', background="white",
                                             foreground="#249794")
            self.combo_indice5.current(0)
            self.label_pico5.place(x=10, y=self.posicion)
            self.entry_pico5.place(x=140, y=self.posicion)
            self.label_indice5.place(x=250, y=self.posicion)
            self.combo_indice5.place(x=380, y=self.posicion)
            self.label_intensity5.place(x=480, y=self.posicion)
            self.entry_intensity5.place(x=570, y=self.posicion)
            entry_pico.trace("w", lambda *args: limiter(entry_pico))
            entry_inten.trace("w", lambda *args: validator_intensity(entry_inten))
            self.click += 1
            self.posicion += 30

        print("Click Agregar", self.click)

    def eliminarDatos(self):
        if self.click == 6:
            self.label_pico5.place_forget()
            self.entry_pico5.place_forget()
            self.label_indice5.place_forget()
            self.combo_indice5.place_forget()
            self.label_intensity5.place_forget()
            self.entry_intensity5.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 5:
            self.label_pico4.place_forget()
            self.entry_pico4.place_forget()
            self.label_indice4.place_forget()
            self.combo_indice4.place_forget()
            self.label_intensity4.place_forget()
            self.entry_intensity4.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 4:
            self.label_pico3.place_forget()
            self.entry_pico3.place_forget()
            self.label_indice3.place_forget()
            self.combo_indice3.place_forget()
            self.label_intensity3.place_forget()
            self.entry_intensity3.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 3:
            self.label_pico2.place_forget()
            self.entry_pico2.place_forget()
            self.label_indice2.place_forget()
            self.combo_indice2.place_forget()
            self.label_intensity2.place_forget()
            self.entry_intensity2.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 2:
            self.label_pico.place_forget()
            self.entry_pico.place_forget()
            self.label_indice.place_forget()
            self.combo_indice.place_forget()
            self.label_intensity.place_forget()
            self.entry_intensity.place_forget()
            self.click -= 1
            self.posicion -= 30

        print("Click eliminar", self.click)

    def aceptarDatos(self):

        if self.click == 6:
            if validate_notNull(self.entry_pico.get()) \
                    is True and validate_notNull(self.entry_intensity.get()) \
                    is True and validate_notNull(self.entry_pico2.get()) \
                    is True and validate_notNull(self.entry_intensity2.get()) \
                    is True and validate_notNull(self.entry_pico3.get()) \
                    is True and validate_notNull(self.entry_intensity3.get()) \
                    is True and validate_notNull(self.entry_pico4.get()) \
                    is True and validate_notNull(self.entry_intensity4.get()) \
                    is True and validate_notNull(self.entry_pico5.get()) \
                    is True and validate_notNull(self.entry_intensity5.get())\
                    is True and limiter_Angstrom(self.entry_angstrom) is True:
                self.angulos.append(float(self.entry_pico.get()))
                self.angulos.append(float(self.entry_pico2.get()))
                self.angulos.append(float(self.entry_pico3.get()))
                self.angulos.append(float(self.entry_pico4.get()))
                self.angulos.append(float(self.entry_pico5.get()))
                self.indices.append(self.combo_indice.get())
                self.indices.append(self.combo_indice2.get())
                self.indices.append(self.combo_indice3.get())
                self.indices.append(self.combo_indice4.get())
                self.indices.append(self.combo_indice5.get())
                self.intensidades.append(self.entry_intensity.get())
                self.intensidades.append(self.entry_intensity2.get())
                self.intensidades.append(self.entry_intensity3.get())
                self.intensidades.append(self.entry_intensity4.get())
                self.intensidades.append(self.entry_intensity5.get())
                self.datos[0] = self.angulos
                self.datos[1] = self.indices
                self.datos[2] = self.intensidades
                self.datos[3] = self.entry_angstrom.get()
                self.ventana_graficos = VentanaGraficos(2, self.datos)
                self.ventana_cargadatos.destroy()
                self.ventana_graficos.mostrarVentana()
            else:
                pass

        elif self.click == 5:
            if validate_notNull(self.entry_pico.get()) \
                    is True and validate_notNull(self.entry_intensity.get()) \
                    is True and validate_notNull(self.entry_pico2.get()) \
                    is True and validate_notNull(self.entry_intensity2.get()) \
                    is True and validate_notNull(self.entry_pico3.get()) \
                    is True and validate_notNull(self.entry_intensity3.get()) \
                    is True and validate_notNull(self.entry_pico4.get()) \
                    is True and validate_notNull(self.entry_intensity4.get()) \
                    is True and limiter_Angstrom(self.entry_angstrom) is True:
                self.angulos.append(float(self.entry_pico.get()))
                self.angulos.append(float(self.entry_pico2.get()))
                self.angulos.append(float(self.entry_pico3.get()))
                self.angulos.append(float(self.entry_pico4.get()))
                self.indices.append(self.combo_indice.get())
                self.indices.append(self.combo_indice2.get())
                self.indices.append(self.combo_indice3.get())
                self.indices.append(self.combo_indice4.get())
                self.intensidades.append(self.entry_intensity.get())
                self.intensidades.append(self.entry_intensity2.get())
                self.intensidades.append(self.entry_intensity3.get())
                self.intensidades.append(self.entry_intensity4.get())
                self.datos[0] = self.angulos
                self.datos[1] = self.indices
                self.datos[2] = self.intensidades
                self.datos[3] = self.entry_angstrom.get()
                self.ventana_graficos = VentanaGraficos(2, self.datos)
                self.ventana_cargadatos.destroy()
                self.ventana_graficos.mostrarVentana()
            else:
                pass
        elif self.click == 4:
            if validate_notNull(self.entry_pico.get()) \
                    is True and validate_notNull(self.entry_intensity.get()) \
                    is True and validate_notNull(self.entry_pico2.get()) \
                    is True and validate_notNull(self.entry_intensity2.get()) \
                    is True and validate_notNull(self.entry_pico3.get()) \
                    is True and validate_notNull(self.entry_intensity3.get()) \
                    is True and limiter_Angstrom(self.entry_angstrom) is True:
                self.angulos.append(float(self.entry_pico.get()))
                self.angulos.append(float(self.entry_pico2.get()))
                self.angulos.append(float(self.entry_pico3.get()))
                self.indices.append(self.combo_indice.get())
                self.indices.append(self.combo_indice2.get())
                self.indices.append(self.combo_indice3.get())
                self.intensidades.append(self.entry_intensity.get())
                self.intensidades.append(self.entry_intensity2.get())
                self.intensidades.append(self.entry_intensity3.get())
                self.datos[0] = self.angulos
                self.datos[1] = self.indices
                self.datos[2] = self.intensidades
                self.datos[3] = self.entry_angstrom.get()
                self.ventana_graficos = VentanaGraficos(2, self.datos)
                self.ventana_cargadatos.destroy()
                self.ventana_graficos.mostrarVentana()
            else:
                pass

        elif self.click == 3:
            if validate_notNull(self.entry_pico.get()) \
                    is True and validate_notNull(self.entry_intensity.get()) \
                    is True and validate_notNull(self.entry_pico2.get()) \
                    is True and validate_notNull(self.entry_intensity2.get())  \
                    is True and limiter_Angstrom(self.entry_angstrom) is True:
                self.angulos.append(float(self.entry_pico.get()))
                self.angulos.append(float(self.entry_pico2.get()))
                self.indices.append(self.combo_indice.get())
                self.indices.append(self.combo_indice2.get())
                self.intensidades.append(self.entry_intensity.get())
                self.intensidades.append(self.entry_intensity2.get())
                self.datos[0] = self.angulos
                self.datos[1] = self.indices
                self.datos[2] = self.intensidades
                self.datos[3] = self.entry_angstrom.get()
                self.ventana_graficos = VentanaGraficos(2, self.datos)
                self.ventana_cargadatos.destroy()
                self.ventana_graficos.mostrarVentana()
            else:
                pass
        elif self.click == 2:
            if validate_notNull(self.entry_pico.get()) is True and validate_notNull(self.entry_intensity.get()) is True and limiter_Angstrom(self.entry_angstrom) is True:
                self.angulos.append(float(self.entry_pico.get()))
                self.indices.append(self.combo_indice.get())
                self.intensidades.append(self.entry_intensity.get())
                self.datos[0] = self.angulos
                self.datos[1] = self.indices
                self.datos[2] = self.intensidades
                self.datos[3] = self.entry_angstrom.get()
                self.ventana_graficos = VentanaGraficos(2, self.datos)
                self.ventana_cargadatos.destroy()
                self.ventana_graficos.mostrarVentana()
            else:
                pass
        else:
            messagebox.showinfo('Nota','Debe agregar al menos 1 pico de difracción')

    def cancelar(self):
        self.ventana_cargadatos.destroy()
        from interfaz.InterfazSeleccion import VentanaSeleccion
        self.vetana_Select = VentanaSeleccion()

def validate(char, entry_value):
    try:
        if char in '1234567890.':  # esto es para validar solo numeros escritos aqui
            return True
        else:
            print('invalid: {s}'.format(s=char))
            messagebox.showinfo('Nota', 'Agregar solo números')
            return False
    except:
        messagebox.showinfo('Nota', 'Formato invalido')


def validate_notNull(cad):
    if cad != '':  # esto es para validar solo numeros escritos aqui
        return True
    else:
        messagebox.showinfo('Nota', 'Existen campos vacios')
        return False


def limiter(entry):
    try:
        if float(entry.get()) > 90:
            entry.set('')
            messagebox.showinfo('Nota', 'El angulo debe de ser mayor a 0 y menor o igual a 90°')
    except ValueError:
        entry.set('')
        messagebox.showinfo('Nota', 'Formato invalido')


def limiter_Angstrom(entry):
    try:
        if 0.5 > float(entry.get()) or float(entry.get()) > 2.5:
            messagebox.showinfo('Nota',
                                'El valor de Ángstrom debe ser mayor a 0.5 y menor o igual a 2.5 unidades de Ángstroms')
            return False
        else:
            return True
    except ValueError:
        messagebox.showinfo('Nota', 'Formato invalido del valor de Ángstrom')

def validator_intensity(entry):
    try:
        float(entry.get())
    except ValueError:
        entry.set('')
        messagebox.showinfo('Nota', 'Formato invalido')

