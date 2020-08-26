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

# Rich Text Box (ScrollTextBox)
richtextbox = scrolledtext.ScrolledText(ventanaprincipal)

# Label Titulo Principal (Label)
titulo = Label(ventanaprincipal)
