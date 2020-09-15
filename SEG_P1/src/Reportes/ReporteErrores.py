# ---------------------------------------------------Imports------------------------------------------------------------
import webbrowser

from tkinter.messagebox import showinfo, askyesno
from pathlib import Path

from src.Variables import Variables


# ----------------------------------------------------Métodos-----------------------------------------------------------

# Reporte De Errores HTML
def ReporteErroresHTML():

    # Variables
    rutaarchivo = ""
    cadenaarchivo = ""
    rutastring = ""
    listacomentarios = []
    listasplit = []

    # Asignacion
    rutastring = "C:\\Reportes\\html"
    listacomentarios[:] = []
    listasplit[:] = []

    # Obtener Ruta Archivo
    for Tokens in Variables.listatokenshtml:

        # Obtener Comentarios
        if Tokens[1] == "Comentario":
            # Agregar Token A Lista
            listacomentarios.append(Tokens[2].strip())

    # Obtener Ruta Archivo
    for Comentario in listacomentarios:

        # Verificar Que Contenga Una Ruta
        if ":" in Comentario:

            # Split Comentario
            listasplit = Comentario.split(":", maxsplit=1)

            # Verificar Si La Ruta Es Valida
            if listasplit[0].strip() == "PATHW":
                # Obtener Ruta Para Windows
                rutaarchivo = listasplit[1].strip()

    # Verificar Ruta Archivo
    if rutaarchivo != "":

        # Convertir String A Ruta
        patharchivo = Path(rutaarchivo)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        # Crear Archivo
        reporteerrores = open(rutaarchivo + "ReporteErroresHTML.html", "w")

        # Path Salida
        pathsalida = rutaarchivo + "ReporteErroresHTML.html"

    else:

        # Convertir String A Ruta
        patharchivo = Path(rutastring)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        reporteerrores = open(rutastring + "\\ReporteErroresHTML.html", "w")

        # Path Salida
        pathsalida = rutastring + "\\ReporteErroresHTML.html"

        showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Reporte \n"
                           "Se Guardara En La Siguiente Ruta: \n"
                           "C:\\Reportes\\html")

    # Escribir Reporte HTML
    cadenaarchivo = "<html> \n" \
                    "<head> \n" \
                    "    <title> Reporte Errores HTML </title> \n" \
                    "</head> \n" \
                    "<body bgcolor=\"#FA8072\">  \n" \
                    "    <center><H1><p style=\"color:#00008B\"> Tabla De Errores </p></H1></center> \n" \
                    "    <center><table border=\"1\"> \n" \
                    "    <thead> \n" \
                    "        <tr bgcolor=\"#FAEBD7\"> \n" \
                    "            <center><td> No. </td></center> \n" \
                    "            <center><td> Fila </td></center> \n" \
                    "            <center><td> Columna </td></center> \n" \
                    "            <center><td> Caracter </td></center> \n" \
                    "            <center><td> Descripción </td></center> \n" \
                    "        </tr> \n"

    # Recorrer Lista De Errores
    for Error in Variables.listaerroreshtml:
        # Agregar Error A Archivo
        cadenaarchivo += "        <tr bgcolor=\"#FFE4E1\"> \n" \
                         "            <center><td>" + str(Error[0]) + "</td></center> \n" \
                                                                      "            <center><td>" + \
                        str(Error[4]) + "</td></center> \n " \
                        "            <center><td>" + str(Error[3]) + "</td></center> \n" \
                                                                     "            <center><td>" + Error[
                             2] + "</td></center> \n" \
                                  "            <center><td>" \
                                  "            El Caracter Indicado No Pertene Al Lenguaje </td></center> \n" \
                                  "        </tr>"

    cadenaarchivo += "    </thead> \n" \
                     "    </table></center> \n" \
                     "</body> \n" \
                     "</html> \n"

    # Escribir En Archivo
    reporteerrores.write(cadenaarchivo)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Reporte De Errores!", "¿Desea Abrir El Reporte De Errores De HTML?")

    # Abrir Archivo
    if resultado:
        # Abrir Reporte HTML
        webbrowser.open_new_tab(pathsalida)


# Reporte De Errores CSS
def ReporteErroresCSS():

    # Variables
    rutaarchivo = ""
    cadenaarchivo = ""
    rutastring = ""
    listacomentarios = []
    listasplit = []

    # Asignacion
    rutastring = "C:\\Reportes\\css"
    listacomentarios[:] = []
    listasplit[:] = []

    # Obtener Ruta Archivo
    for Tokens in Variables.listatokenscss:

        # Obtener Comentarios
        if Tokens[1] == "Comentario":
            # Agregar Token A Lista
            listacomentarios.append(Tokens[2].strip())

    # Obtener Ruta Archivo
    for Comentario in listacomentarios:

        # Verificar Que Contenga Una Ruta
        if ":" in Comentario:

            # Split Comentario
            listasplit = Comentario.split(":", maxsplit=1)

            # Verificar Si La Ruta Es Valida
            if listasplit[0].strip() == "PATHW":
                # Obtener Ruta Para Windows
                rutaarchivo = listasplit[1].strip()

    # Verificar Ruta Archivo
    if rutaarchivo != "":

        # Convertir String A Ruta
        patharchivo = Path(rutaarchivo)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        # Crear Archivo
        reporteerrores = open(rutaarchivo + "ReporteErroresCSS.html", "w")

        # Path Salida
        pathsalida = rutaarchivo + "ReporteErroresCSS.html"

    else:

        # Convertir String A Ruta
        patharchivo = Path(rutastring)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        reporteerrores = open(rutastring + "\\ReporteErroresCSS.html", "w")

        # Path Salida
        pathsalida = rutastring + "\\ReporteErroresCSS.html"

        showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Reporte \n"
                           "Se Guardara En La Siguiente Ruta: \n"
                           "C:\\Reportes\\css")

    # Escribir Reporte HTML
    cadenaarchivo = "<html> \n" \
                    "<head> \n" \
                    "    <title> Reporte Errores CSS </title> \n" \
                    "</head> \n" \
                    "<body bgcolor=\"#FA8072\">  \n" \
                    "    <center><H1><p style=\"color:#00008B\"> Tabla De Errores </p></H1></center> \n" \
                    "    <center><table border=\"1\"> \n" \
                    "    <thead> \n" \
                    "        <tr bgcolor=\"#FAEBD7\"> \n" \
                    "            <center><td> No. </td></center> \n" \
                    "            <center><td> Fila </td></center> \n" \
                    "            <center><td> Columna </td></center> \n" \
                    "            <center><td> Caracter </td></center> \n" \
                    "            <center><td> Descripción </td></center> \n" \
                    "        </tr> \n"

    # Recorrer Lista De Errores
    for Error in Variables.listaerrorescss:
        # Agregar Error A Archivo
        cadenaarchivo += "        <tr bgcolor=\"#FFE4E1\"> \n" \
                         "            <center><td>" + str(Error[0]) + "</td></center> \n" \
                                                                      "            <center><td>" + \
                         str(Error[4]) + "</td></center> \n " \
                        "            <center><td>" + str(Error[3]) + "</td></center> \n" \
                                                                     "            <center><td>" + Error[
                             2] + "</td></center> \n" \
                                  "            <center><td>" \
                                  "            El Caracter Indicado No Pertene Al Lenguaje </td></center> \n" \
                                  "        </tr>"

    cadenaarchivo += "    </thead> \n" \
                     "    </table></center> \n" \
                     "</body> \n" \
                     "</html> \n"

    # Escribir En Archivo
    reporteerrores.write(cadenaarchivo)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Reporte De Errores!", "¿Desea Abrir El Reporte De Errores De CSS?")

    # Abrir Archivo
    if resultado:

        # Abrir Reporte HTML
        webbrowser.open_new_tab(pathsalida)


# Reporte De Errores JS
def ReporteErroresJS():

    # Variables
    rutaarchivo = ""
    cadenaarchivo = ""
    rutastring = ""
    listacomentarios = []
    listasplit = []

    # Asignacion
    rutastring = "C:\\Reportes\\js"
    listacomentarios[:] = []
    listasplit[:] = []

    # Obtener Ruta Archivo
    for Tokens in Variables.listatokensjs:

        # Obtener Comentarios
        if Tokens[1] == "Comentario_UniLinea":

            # Agregar Token A Lista
            listacomentarios.append(Tokens[2].strip())

    # Obtener Ruta Archivo
    for Comentario in listacomentarios:

        # Verificar Que Contenga Una Ruta
        if ":" in Comentario:

            # Split Comentario
            listasplit = Comentario.split(":", maxsplit=1)

            # Verificar Si La Ruta Es Valida
            if listasplit[0].strip() == "PATHW":

                # Obtener Ruta Para Windows
                rutaarchivo = listasplit[1].strip()

    # Verificar Ruta Archivo
    if rutaarchivo != "":

        # Convertir String A Ruta
        patharchivo = Path(rutaarchivo)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():

            # Crear Directorios
            patharchivo.mkdir(parents=True)

        # Crear Archivo
        reporteerrores = open(rutaarchivo + "ReporteErroresJS.html", "w")

        # Path Salida
        pathsalida = rutaarchivo + "ReporteErroresJS.html"

    else:

        # Convertir String A Ruta
        patharchivo = Path(rutastring)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():

            # Crear Directorios
            patharchivo.mkdir(parents=True)

        reporteerrores = open(rutastring + "\\ReporteErroresJS.html", "w")

        # Path Salida
        pathsalida = rutastring + "\\ReporteErroresJS.html"

        showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Reporte \n"
                           "Se Guardara En La Siguiente Ruta: \n"
                           "C:\\Reportes\\js")

    # Escribir Reporte HTML
    cadenaarchivo = "<html> \n" \
                    "<head> \n" \
                    "    <title> Reporte Errores CSS </title> \n" \
                    "</head> \n" \
                    "<body bgcolor=\"#FA8072\">  \n" \
                    "    <center><H1><p style=\"color:#00008B\"> Tabla De Errores </p></H1></center> \n" \
                    "    <center><table border=\"1\"> \n" \
                    "    <thead> \n" \
                    "        <tr bgcolor=\"#FAEBD7\"> \n" \
                    "            <center><td> No. </td></center> \n" \
                    "            <center><td> Fila </td></center> \n" \
                    "            <center><td> Columna </td></center> \n" \
                    "            <center><td> Caracter </td></center> \n" \
                    "            <center><td> Descripción </td></center> \n" \
                    "        </tr> \n"

    # Recorrer Lista De Errores
    for Error in Variables.listaerroresjs:
        # Agregar Error A Archivo
        cadenaarchivo += "        <tr bgcolor=\"#FFE4E1\"> \n" \
                         "            <center><td>" + str(Error[0]) + "</td></center> \n" \
                                                                      "            <center><td>" + \
                         str(Error[4]) + "</td></center> \n " \
                        "            <center><td>" + str(Error[3]) + "</td></center> \n" \
                                                                     "            <center><td>" + Error[
                             2] + "</td></center> \n" \
                                  "            <center><td>" \
                                  "            El Caracter Indicado No Pertene Al Lenguaje </td></center> \n" \
                                  "        </tr>"

    cadenaarchivo += "    </thead> \n" \
                     "    </table></center> \n" \
                     "</body> \n" \
                     "</html> \n"

    # Escribir En Archivo
    reporteerrores.write(cadenaarchivo)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Reporte De Errores!", "¿Desea Abrir El Reporte De Errores De JS?")

    # Abrir Archivo
    if resultado:

        # Abrir Reporte HTML
        webbrowser.open_new_tab(pathsalida)


# Reporte De Errores RMT
def ReporteErroresRMT():

    # Variables
    cadenaarchivo = ""
    rutastring = ""

    # Asignacion
    rutastring = "C:\\Reportes\\rmt"

    # Convertir String A Ruta
    patharchivo = Path(rutastring)

    # Verificar Si Existe El Directorio
    if not patharchivo.is_dir():

        # Crear Directorios
        patharchivo.mkdir(parents=True)

    reporteerrores = open(rutastring + "\\ReporteErroresRMT.html", "w")

    # Path Salida
    pathsalida = rutastring + "\\ReporteErroresRMT.html"

    showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Reporte \n"
                       "Se Guardara En La Siguiente Ruta: \n"
                       "C:\\Reportes\\rmt")

    # Escribir Reporte HTML
    cadenaarchivo = "<html> \n" \
                    "<head> \n" \
                    "    <title> Reporte Errores RMT </title> \n" \
                    "</head> \n" \
                    "<body bgcolor=\"#FA8072\">  \n" \
                    "    <center><H1><p style=\"color:#00008B\"> Tabla De Errores </p></H1></center> \n" \
                    "    <center><table border=\"1\"> \n" \
                    "    <thead> \n" \
                    "        <tr bgcolor=\"#FAEBD7\"> \n" \
                    "            <center><td> No. </td></center> \n" \
                    "            <center><td> Fila </td></center> \n" \
                    "            <center><td> Columna </td></center> \n" \
                    "            <center><td> Caracter </td></center> \n" \
                    "            <center><td> Descripción </td></center> \n" \
                    "        </tr> \n"

    # Recorrer Lista De Errores
    for Error in Variables.listaerroresrmt:
        # Agregar Error A Archivo
        cadenaarchivo += "        <tr bgcolor=\"#FFE4E1\"> \n" \
                         "            <center><td>" + str(Error[0]) + "</td></center> \n" \
                                                                      "            <center><td>" + \
                         str(Error[4]) + "</td></center> \n " \
                        "            <center><td>" + str(Error[3]) + "</td></center> \n" \
                                                                     "            <center><td>" + Error[
                             2] + "</td></center> \n" \
                                  "            <center><td>" \
                                  "            El Caracter Indicado No Pertene Al Lenguaje </td></center> \n" \
                                  "        </tr>"

    cadenaarchivo += "    </thead> \n" \
                     "    </table></center> \n" \
                     "</body> \n" \
                     "</html> \n"

    # Escribir En Archivo
    reporteerrores.write(cadenaarchivo)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Reporte De Errores!", "¿Desea Abrir El Reporte De Errores De RMT?")

    # Abrir Archivo
    if resultado:

        # Abrir Reporte HTML
        webbrowser.open_new_tab(pathsalida)
