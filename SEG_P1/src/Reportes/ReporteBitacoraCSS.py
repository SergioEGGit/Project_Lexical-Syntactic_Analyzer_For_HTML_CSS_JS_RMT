# ---------------------------------------------------Imports------------------------------------------------------------
from src.Variables import Variables
from src.Design import Objetos


# ----------------------------------------------------Métodos-----------------------------------------------------------

# Reporte Bitacora CSS
def ReporteBitacoraCSS(extensionarchivo):

    # Variables
    bitacoracsstexto = ""

    # Cambiar De Color
    Objetos.richtextboxconsola.config(fg='#228B22', font=("arial", 14), background='#FAF0E6')

    # Modulo De Decision
    if extensionarchivo == "css":

        # Añadir Bitacora
        for Linea in Variables.bitacoracss:

            bitacoracsstexto += "Id: " + str(Linea[0]) + "." + "  Descripcion: " + Linea[1] + "." + " " + Linea[2] + \
                                "." + "\n\n"

    # Insertar Texto
    Objetos.richtextboxconsola.delete(1.0, "end-1c")
    Objetos.richtextboxconsola.insert("end-1c", bitacoracsstexto)
