# ---------------------------------------------------Imports------------------------------------------------------------
from tkinter import *
from tkinter import Menu, scrolledtext

# -----------------------------------------------Objetos Interfaz-------------------------------------------------------

# Frame Principal (form TK)
ventanaprincipal = Tk()

# Barra De Menú (Menubar)
barrademenu = Menu(ventanaprincipal)

# Menú Archivo (Menu Item)
menuarchivo = Menu(barrademenu)

# Menú Herrramientas (Menu Item)
menuherramientas = Menu(barrademenu)

# Menú Ayuda (Menu Item)
menuayuda = Menu(barrademenu)

# Rich Text Box Archivo (ScrollTextBox)
richtextboxarchivo = scrolledtext.ScrolledText(ventanaprincipal)

# Rich Text Box Consola (ScrollTextBox)
richtextboxconsola = scrolledtext.ScrolledText(ventanaprincipal)

# Label Titulo Principal (Label)
tituloprincipal = Label(ventanaprincipal)

# Label Titulo Archivo (Label)
tituloarchivo = Label(ventanaprincipal)

# Label Titulo Consola (Label)
tituloconsola = Label(ventanaprincipal)
