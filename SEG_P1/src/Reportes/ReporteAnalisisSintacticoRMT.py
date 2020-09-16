# ---------------------------------------------------Imports------------------------------------------------------------
from pathlib import Path
from tkinter.messagebox import showinfo, askyesno

from src.Analizadores import AnalizadorSintacticoRMT
from src.Variables import Variables


# ----------------------------------------------------Métodos-----------------------------------------------------------

# Reporte Analisis Sintactico RMT
def ReporteAnalisisSintacticoRMT(extensionarchivo):
    AnalizadorSintacticoRMT.AnalizadorSintacticoRMT()

    if extensionarchivo == "rmt":

        resultado = askyesno("Reporte", "Desea Visualizar El Reporte De Análsis Sintactico En Formato HTML?")

        if resultado:

            # Variables
            cadenaarchivo = ""
            rutastring = ""
            cadenaauxiliar = ""

            # Asignacion
            rutastring = "C:\\Reportes\\rmt"

            # Convertir String A Ruta
            patharchivo = Path(rutastring)

            # Verificar Si Existe El Directorio
            if not patharchivo.is_dir():
                # Crear Directorios
                patharchivo.mkdir(parents=True)

            reporteerrores = open(rutastring + "\\ReporteAnalisisSintacticoRMT.html", "w")

            # Path Salida
            pathsalida = rutastring + "\\ReporteAnalisisSintacticoRMT.html"

            showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Reporte \n"
                               "Se Guardara En La Siguiente Ruta: \n"
                               "C:\\Reportes\\rmt")

            # Escribir Reporte HTML
            cadenaarchivo = "<html> \n" \
                            "<head> \n" \
                            "    <title> Reporte Errores RMT </title> \n" \
                            "</head> \n" \
                            "<body bgcolor=\"#FA8072\">  \n" \
                            "    <center><H1><p style=\"color:#00008B\"> Reporte Análisis Sintactico </p></H1></center> \n" \
                            "    <center><table border=\"1\"> \n" \
                            "    <thead> \n" \
                            "        <tr bgcolor=\"#FAEBD7\"> \n" \
                            "            <center><td> No. </td></center> \n" \
                            "            <center><td> Linea </td></center> \n" \
                            "            <center><td> Operación </td></center> \n" \
                            "            <center><td> Análisis </td></center> \n" \
                            "        </tr> \n"

            for Linea in Variables.listaanalisissintacticormt:

                if Linea[2] != "" or Linea[2] != " " or Linea[2] != "\n" or Linea[2] != "\t":

                    if len(Linea[2]) > 0:
                        cadenaarchivo += "        <tr bgcolor=\"#FFE4E1\"> \n" \
                                         "            <center><td>" + str(Linea[0]) + "</td></center> \n" \
                                                                                      "            <center><td>" + \
                                         str(Linea[1]) + "</td></center> \n " \
                                                         "            <center><td>" + Linea[2] + "</td></center> \n" \
                                                         "            <center><td>" + \
                                         Linea[
                                             3] + "</td></center> \n" \
                                                  "        </tr>"


            cadenaarchivo += "    </thead> \n" \
                             "    </table></center> \n" \
                             "</body> \n" \
                             "</html> \n"

    else:

        showinfo("Error!", "No Se Ha Realizado Ningun Análisis De RMT")
