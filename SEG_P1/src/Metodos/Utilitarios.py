# ---------------------------------------------------Imports------------------------------------------------------------
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.messagebox import askyesnocancel, showinfo

from src.Design import Objetos
from src.Variables import Variables
from src.Analizadores import AnalizadorLexicoHMTL as Analizadores


# ----------------------------------------------------Métodos-----------------------------------------------------------

# Método Nuevo
def OpcionNuevo():

    # Verificar Si Hay Un Archivo Abierto
    if Variables.rutaarchivo != "":

        # Verificar Si Se Desea Guardar O No El Archivo
        bandera = askyesnocancel(title="Aviso", message="¿Desea Guardar El Documento Que Esta Modificando?")

        if bandera:
            OpcionGuardar()
            Objetos.richtextbox.delete(1.0, "end-1c")
            Variables.rutaarchivo = ""
        elif bandera is None:
            print("")
        elif not bandera:
            Objetos.richtextbox.delete(1.0, "end-1c")
            Variables.rutaarchivo = ""

    else:

        # Verificar Si No Hay Nada En El Rich Text
        texto = Objetos.richtextbox.get(1.0, "end-1c")

        if texto != "":

            # Verificar Si Se Desea guardar O No El Archivo
            bandera2 = askyesnocancel(title="Aviso", message="¿Desea Guardar El Documento Que Esta Modificando?")

            if bandera2:
                OpcionGuardarComo()
                Objetos.richtextbox.delete(1.0, "end-1c")
            elif bandera2 is None:
                print("")
            elif not bandera2:
                Objetos.richtextbox.delete(1.0, "end-1c")


# Método Abrir Archivo
def OpcionAbrir():

    # Obtener El Nombre Del Archivo
    nombrearchivo = askopenfilename(initialdir="C:\\", title="Abrir Archivo", filetypes=(
        ("Archivos HTML", "*.html"), ("Archivos CSS", "*.css*"), ("Archivos JS", "*.js"),
        ("Archivos Análisis Sintáctico", "*.rmt")))

    # Verificar Si No Se Presiono Cancelar
    if nombrearchivo != "":
        # Limpiar TextBox
        Objetos.richtextbox.delete(1.0, "end-1c")

        # Obtener Ruta Archivo
        arreglosplit = nombrearchivo.split(".")

        # Guardar Ruta Y Extension Del Archivo
        Variables.rutaarchivo = nombrearchivo.strip()
        Variables.extensionarchivo = arreglosplit[1].strip()

        # Abrir Archivo En Modo Lectura
        nuevoarchivo = open(nombrearchivo, "r")

        # Obtener Texto Completo
        Variables.cadenaarchivo = nuevoarchivo.read()
        nuevoarchivo.close()

        # Colocar Texto En Rich Text
        Objetos.richtextbox.insert("end-1c", Variables.cadenaarchivo)


# Método Guardar Archivo
def OpcionGuardar():

    # Verificar Que Existe Archivo Abierto
    if Variables.rutaarchivo != "":
        # Abrir Archivo En Modo Escritura
        archivomodificado = open(Variables.rutaarchivo, "w")

        # Obtener El Texto Del Rich Text
        cadenaarchivo = Objetos.richtextbox.get(1.0, "end-1c")

        # Escribir En Archivo
        archivomodificado.write(cadenaarchivo)
        archivomodificado.close()


# Método Guardar Como
def OpcionGuardarComo():

    # Obtener Directorio Guardar Archivo
    rutaarchivo = asksaveasfile(initialdir="C:\\", title="Guardar Como...", filetypes=(
        ("Archivos HTML", "*.html"), ("Archivos CSS", "*.css*"), ("Archivos JS", "*.js"),
        ("Archivos Análisis Sintáctico", "*.rmt")), defaultextension=".html")

    # Si Se Indico Un Archivo
    if rutaarchivo:
        # Escribir En Archivo
        rutaarchivo.write(Objetos.richtextbox.get(1.0, "end-1c"))
        rutaarchivo.close()

        # Mensaje
        showinfo("Información", "Archivo Guardado Con Exito!")


# Método Salir
def OpcionSalir():

    Objetos.ventanaprincipal.quit()


# Modulo Decisión
def ModuloDecisionAnalizador():

    # Obtener Texto Archivo
    Variables.cadenaarchivo = Objetos.richtextbox.get(1.0, "end-1c")

    # Verificar Si Hay Una Archivo Abierto
    if Variables.extensionarchivo != "":

        # Verificar Extensión
        if Variables.extensionarchivo.strip() == "html":
            Analizadores.AnalizadorLexicoHTML()
        elif Variables.extensionarchivo.strip() == "css":
            print("Analizo Css")
        elif Variables.extensionarchivo.strip() == "js":
            print("Analizo Js")
        elif Variables.extensionarchivo.strip() == "rmt":
            print("Analisis Sintactico")
    else:
        showinfo("Información", "Aún No Se Ha Abierto Ningún Archivo Valido")
