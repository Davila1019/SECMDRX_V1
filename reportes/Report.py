from fpdf import FPDF
import webbrowser
from tkinter import messagebox as mb
from tkinter import filedialog
class Report(FPDF):

    def config(self):
        self.set_author('SECMDRX')
        self.set_margins(1.5, 1.5, 1.5)
        self.alias_nb_pages(alias='pag_total')
        self.add_page()

    def header(self):
        self.set_font('Times', 'B', 12)

        self.image('./interfaz/logo-ipn.png', 1.5, .7, 3)
        self.image('./interfaz/logo-upiiz.png', 17.3, .4, 2.3)
        self.cell(0,.8,"Instituto Politécnico Nacional",0,0,'C')
        self.ln(.8)
        self.cell(0, .8,"Unidad Profesional Interdisciplinaria De Ingenierias Campus Zacatecas",0, 0, 'C')
        self.ln(.8)
        self.cell(0, .8,"UPIIZ",0, 0, 'C')
        self.ln(1.2)

    def footer(self):
        self.set_y(-1.5)
        self.set_font('Times','',8)
        paginado = 'Página {0} de pag_total'.format(self.page_no())
        self.cell(0,.8,paginado,0,0,'C')

    def create_pdf(self,metal,distancias:list,intensidad:list,angulos:list,indices:list,radioA=0,parametro=0):
        self.set_font('Times', 'B',16)
        self.set_title('Reporte')
        self.cell(0,.8,'Reporte simulación SECMDRX',0,0,'J')
        self.ln(1.2)
        self.set_font('Times', '', 12)
        self.cell(3,.8,'Metal simulado:',0,0,'J')
        self.set_font('Times', '', 12)
        self.cell(0, .8, metal, 0, 0, 'J')
        self.ln(0.8)
        if metal == 'Titanio':
            dataAl = open("./reportes/data/dataTi.txt","r+")
            cad = dataAl.read().split('\n')
            for line in cad:
                self.multi_cell(0, .8, line, 0, 'J')
        elif metal == 'Aluminio':
            dataAl = open("./reportes/data/dataAl.txt","r+")
            cad = dataAl.read().split('\n')
            for line in cad:
                self.multi_cell(0, .8, line, 0, 'J')
        if metal == 'Cobre':
            dataAl = open("./reportes/data/dataCu.txt","r+")
            cad = dataAl.read().split('\n')
            for line in cad:
                self.multi_cell(0, .8, line, 0, 'J')
        elif metal == 'Hierro':
            dataAl = open("./reportes/data/dataFe.txt","r+")
            cad = dataAl.read().split('\n')
            for line in cad:
                self.multi_cell(0, .8, line, 0, 'J')
        self.ln(.4)
        self.set_font('Times', 'B', 12)
        self.cell(0,.8,'Lista de picos:',0,0,'J')
        self.ln(0.8)
        i=0
        self.cell(0, .8, 'No.       hkl        d [A]         2Theta[deg]', 0, 0, 'J')
        self.ln(0.8)
        self.set_font('Times', '', 12)
        while i < len(distancias):
            self.cell(15, .8,i.__str__()+'          '+str(indices[i])+'           '+str(distancias[i])+'          '+str(angulos[i]), 0, 0, 'J')
            self.ln(0.8)
            i += 1
        self.set_font('Times', 'B', 12)
        self.cell(0, .8, 'Difractograma', 0, 0, 'J')
        self.ln(0.8)
        self.image('C:/SECMDRX/reports/frames/difractogram.png',w=10, x=5)
        self.ln(20)
        self.cell(0, .8, 'Estructura Cristalográfica', 0, 0, 'J')
        self.ln(0.8)
        self.image('C:/SECMDRX/reports/frames/crystallographic_planes.png', w=10, x=5)
        self.set_font('Times', '', 12)
        self.cell(0, .8, 'Radio Atómico: '+str(radioA), 0, 0, 'J')
        self.ln(0.8)
        self.cell(0, .8, 'Parametro de Red: ' + str(parametro), 0, 0, 'J')
        self.ln(0.8)
        self.ln(20)

        reporte = filedialog.asksaveasfilename(initialdir="/",title="Guardar",defaultextension=".pdf",
                                             filetypes=(("Documento PDF","*.pdf"), ))
        if(reporte != ''):
            try:
                self.output(reporte)
                webbrowser.open(reporte)
            except PermissionError as pe:
                mb.showinfo('SECMDRX','Para crear un nuevo reporte con el mismo nombre debe de cerrar el reporte '
                                      'actual')
                pass

if __name__ == "__main__":
    p = Report('P','cm','Letter')
    p.config()
    p.create_pdf('Titanio')