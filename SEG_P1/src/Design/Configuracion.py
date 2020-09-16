# ---------------------------------------------------Imports------------------------------------------------------------
from tkinter import WORD

from src.Design import Objetos
from src.Metodos import Utilitarios
from src.Variables import Variables
from src.Reportes import ReporteBitacoraCSS, ReporteAutomataJS, ReporteAnalisisSintacticoRMT as ReporteRMT

# --------------------------------------------Conifguración Objetos-----------------------------------------------------


# Ventana Principal
def VentanaPrincipal():

    Objetos.ventanaprincipal.title("SEG: Proyecto_I")
    Objetos.ventanaprincipal.iconbitmap("assets/favicon.ico")
    Objetos.ventanaprincipal.state("zoomed")
    Objetos.ventanaprincipal.config(background='#ADD8E6')


# Barra De Menus
def Menu():

    # Menú Archivo
    Objetos.barrademenu.add_cascade(label="Archivo", menu=Objetos.menuarchivo)
    Objetos.menuarchivo.config(background='#FFEFD5', fg='#000080', tearoff=0)
    Objetos.menuarchivo.add_command(label="Nuevo Análisis", command=lambda: Utilitarios.OpcionNuevo())
    Objetos.menuarchivo.add_command(label="Abrir Archivo", command=lambda: Utilitarios.OpcionAbrir())
    Objetos.menuarchivo.add_separator()
    Objetos.menuarchivo.add_command(label="Guardar", command=lambda: Utilitarios.OpcionGuardar())
    Objetos.menuarchivo.add_command(label="Guardar como...", command=lambda: Utilitarios.OpcionGuardarComo())
    Objetos.menuarchivo.add_separator()
    Objetos.menuarchivo.add_command(label="Salir", command=lambda: Utilitarios.OpcionSalir())
    Objetos.ventanaprincipal.config(menu=Objetos.barrademenu)

    # Menú Herramientas
    Objetos.barrademenu.add_cascade(label="Herramientas", menu=Objetos.menuherramientas)
    Objetos.menuherramientas.config(background='#FFEFD5', fg='#000080', tearoff=0)
    Objetos.menuherramientas.add_command(label="Análisis", command=lambda: Utilitarios.ModuloDecisionAnalizador())
    Objetos.menuherramientas.add_separator()
    Objetos.menuherramientas.add_command(label="Mostar Tokens",
                                         command=lambda: Utilitarios.MostrarTokens(Variables.extensionarchivo))
    Objetos.menuherramientas.add_command(label="Mostar Errores",
                                         command=lambda: Utilitarios.MostrarErrores(Variables.extensionarchivo))
    Objetos.menuherramientas.add_separator()
    Objetos.menuherramientas.add_command(label="Reporte Automata Por Partes JS",
                                         command=lambda: ReporteAutomataJS.GenerarGraficaReporteArbolPorPartesJS())
    Objetos.menuherramientas.add_command(label="Reporte Automata Completo JS",
                                         command=lambda: ReporteAutomataJS.GenerarGraficaReporteArbolCompletoJS())
    Objetos.menuherramientas.add_command(label="Reporte Bitacora CSS",
                                         command=lambda: ReporteBitacoraCSS.ReporteBitacoraCSS(
                                             Variables.extensionarchivo))
    Objetos.menuherramientas.add_command(label="Reporte Analisis Sintáctico RMT",
                                         command=lambda: ReporteRMT.ReporteAnalisisSintacticoRMT(
                                             Variables.extensionarchivo))
    Objetos.ventanaprincipal.config(menu=Objetos.barrademenu)


# Rich Text Box Archivo
def RichTextArchivo():

    width = 55
    height = 26
    Objetos.richtextboxarchivo.config(width=width, height=height, wrap=WORD)
    Objetos.richtextboxarchivo.grid(column=0, columnspan=3)
    Objetos.richtextboxarchivo.config(fg='#000080', font=("arial", 14), background='#FFEFD5')
    Objetos.richtextboxarchivo.place(relx=0.01, rely=0.13)


# Rich Text Box Consola
def RichTextConsola():

    width = 61
    height = 26
    Objetos.richtextboxconsola.config(width=width, height=height, wrap=WORD)
    Objetos.richtextboxconsola.grid(column=0, columnspan=3)
    Objetos.richtextboxconsola.config(fg='#005B5B', font=("arial", 14), background='#FAF0E6')
    Objetos.richtextboxconsola.place(relx=0.48, rely=0.13)


# Titulo Principal
def TituloPrincipal():

    Objetos.tituloprincipal.config(background='#ADD8E6', fg='#0018C5', text='SEG: ML WEB', font=('arial', 22))
    Objetos.tituloprincipal.place(relx=0.41, rely=0)


# Titulo Archivo
def TituloArchivo():

    Objetos.tituloarchivo.config(background='#ADD8E6', fg='#483D8B', text='Texto A Analizar:', font=('arial', 18))
    Objetos.tituloarchivo.place(relx=0.01, rely=0.08)


# Titulo Consola
def TituloConsola():

    Objetos.tituloconsola.config(background='#ADD8E6', fg='#483D8B', text='Tokens, Errores Y Reportes', font=('arial',
                                                                                                              18))
    Objetos.tituloconsola.place(relx=0.48, rely=0.08)

