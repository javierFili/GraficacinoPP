import tkinter
from tkinter import *
global vista

from AlgoritmoModificadoDDA import AlgoritmoModificadoDDA
from Bresenham import Bresenham
# import AlgoritmoModificadoDDA
class Vista:

    def ddapresionado(self):
        self.botonDDApresionado = True
        self.ventana1.title("DDA")


    def bresPresionado(self):
        self.botonDDApresionado = False
        self.ventana1.title("Bresenham")

    def __init__(self):
        self.botonDDApresionado = True
        self.ventana1 = Tk()
        self.ventana1.title("APP interactiva")
        self.ventana1.geometry("400x300")

        self.menubar = Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Nuevo",command=lambda:self.correLinea(self.ventana1, True))
        self.filemenu.add_command(label="Cerrar")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Salir", command=self.ventana1.quit)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cortar")
        self.editmenu.add_command(label="Copiar")
        self.editmenu.add_command(label="Pegar")

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Ayuda")
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="Acerca de...")

        self.menubar.add_cascade(label="Archivo", menu=self.filemenu)
        self.menubar.add_cascade(label="Editar", menu=self.editmenu)
        self.menubar.add_cascade(label="Ayuda", menu=self.helpmenu)

        self.boton3 = Button(self.ventana1,text="DDA",command=lambda
            :self.ddapresionado())
        self.boton3.grid(column=0, row=0)

        self.boton4 = Button(self.ventana1, text="BRESENHAM", command=lambda
            :self.bresPresionado())

        self.boton4.grid(column=1, row=0)


        #---------------------------------------------

        self.label2 = Label(self.ventana1, text="Grosor")
        self.label2.grid(row=2, column=0, sticky="w", padx=2, pady=2)

        self.label1 = Label(self.ventana1, text="Segmento")
        self.label1.grid(row=3, column=0, sticky="w", padx=2, pady=2)

        self.label3 = Label(self.ventana1, text="Espacio")
        self.label3.grid(row=4, column=0, sticky="w", padx=2, pady=2)

        self.grosor = tkinter.StringVar()
        self.segmentacion = tkinter.StringVar()
        self.espacio = tkinter.StringVar()

        self.entry2 = Entry(self.ventana1, width=5, textvariable=self.grosor)
        self.entry2.grid(row=2, column=1, padx=2, pady=2)

        self.entry1 = Entry(self.ventana1, width=5, textvariable=self.segmentacion)
        self.entry1.grid(row=3, column=1, padx=2, pady=2)

        self.entry3 = Entry(self.ventana1, width=5, textvariable=self.espacio)
        self.entry3.grid(row=4, column=1, padx=2, pady=2)

        self.botonAceptar = Button(self.ventana1, text="ACEPTAR", command=lambda:
        self.llamadaprevia())

        self.botonAceptar.grid(row=5, column=1)

        # ---------------------------------
        self.ventana1.mainloop()


    def llamadaprevia(self):
        try:
            self.llamadaPrincipal(int(self.grosor.get()), int(self.segmentacion.get()), int(self.espacio.get()),self.botonDDApresionado)
        except:
            pass


    def llamadaPrincipal(self, grosor, segmentacion, espacio, dibujadoDDA):
        if dibujadoDDA:
            self.algoritmo = AlgoritmoModificadoDDA(grosor, segmentacion)
        else:
            self.algoritmo = Bresenham(segmentacion, espacio, grosor)



#bloque principal
if __name__ == '__main__':
    vis=Vista()

