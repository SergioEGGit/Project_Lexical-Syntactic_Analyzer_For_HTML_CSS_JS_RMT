# ---------------------------------------------------Imports------------------------------------------------------------
import re

from tkinter.messagebox import showinfo, askyesno

from src.Variables import Variables
from src.Metodos import ColorearTexto, Utilitarios
from src.Reportes import ReporteErrores
from src.Design import Objetos


# ----------------------------------------------------Métodos-----------------------------------------------------------


# Analizador Lexico HTML
def AnalizadorLexicoHTML():

    # Asignación
    Variables.columnaauxiliarhtml = 1
    Variables.filaauxiliarhtml = 1
    Variables.indexcaracterhtml = 0
    Variables.contadortokenshtml = 1
    Variables.contadorerroreshtml = 1
    Variables.numerocomillas = 0
    Variables.auxiliarlexicohtml = ""
    Variables.archivohtml = ""
    Variables.listatokenshtml[:] = []
    Variables.listaerroreshtml[:] = []

    # Comienzo A Recorrer Archivo
    while Variables.indexcaracterhtml < len(Variables.cadenaarchivo):

        # Estados

        # Revisar Espacios Vacios
        if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1

        # Revisar Tabulaciones
        elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1

        # Revisar Salto De Linea
        elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Sumar Fila E Indice Del Array, Reiniciar Columna
            Variables.columnaauxiliarhtml = 1
            Variables.filaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1

        # Revisar Letras (Palabras Reservadas / Identificadores)
        elif re.search(r"[a-zA-Z]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Agregar Primer Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml = Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Verifiicar Palabra Completa
            VerificarReservasEIdentificadoresHTML()

        # Verificar Simbolo <
        elif re.search(r"[<]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml = Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Simbolo", Variables.auxiliarlexicohtml, Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

        # Verificar Simbolo !
        elif re.search(r"[!]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            if Variables.indexcaracterhtml + 1 < len(Variables.cadenaarchivo):

                if Variables.cadenaarchivo[Variables.indexcaracterhtml + 1] == "-":

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicohtml = Variables.cadenaarchivo[Variables.indexcaracterhtml]

                    # Archivo Sin Errores
                    Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokenshtml.append(
                        [Variables.contadortokenshtml, "Simbolo", Variables.auxiliarlexicohtml,
                         Variables.columnaauxiliarhtml,
                         Variables.filaauxiliarhtml])

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarhtml += 1
                    Variables.indexcaracterhtml += 1
                    Variables.contadortokenshtml += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicohtml = ""

                    # Verificar Cadena Completa
                    VerificarComentariosHTML()

                elif Variables.cadenaarchivo[Variables.indexcaracterhtml - 1] == "-":

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicohtml = Variables.cadenaarchivo[Variables.indexcaracterhtml]

                    # Archivo Sin Errores
                    Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokenshtml.append(
                        [Variables.contadortokenshtml, "Simbolo", Variables.auxiliarlexicohtml,
                         Variables.columnaauxiliarhtml,
                         Variables.filaauxiliarhtml])

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    # Variables.columnaauxiliarhtml += 1
                    Variables.indexcaracterhtml += 1
                    Variables.contadortokenshtml += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicohtml = ""

                # Marcar Como Error
                else:

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                    # Sumar Columna
                    Variables.columnaauxiliarhtml += 1

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listaerroreshtml.append(
                        [Variables.contadorerroreshtml, "Error_Lexico", Variables.auxiliarlexicohtml,
                         Variables.columnaauxiliarhtml, Variables.filaauxiliarhtml])

                    # Sumar Contador Tokens E Indice Del Array
                    Variables.indexcaracterhtml += 1
                    Variables.contadorerroreshtml += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicohtml = ""

        # Verificar Simbolo =
        elif re.search(r"[=]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml = Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Sumar Columna
            Variables.columnaauxiliarhtml += 1

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Simbolo", Variables.auxiliarlexicohtml, Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

            # Sumar Contador Tokens E Indice Del Array
            Variables.columnaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

        # Verificar Simbolo > (Cadena De Textos)
        elif re.search(r"[>]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml = Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Sumar Columna
            Variables.columnaauxiliarhtml += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Simbolo", Variables.auxiliarlexicohtml, Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

            # No Existe Caracter
            Variables.existecaracter = False

            # Verificar Cadena De Texto
            VerificarCadenasDeTextoHTML()

        # Verificar Simbolo / (Comentarios / Etiqueta Final)
        elif re.search(r"[/]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Sumar Columna
            # Variables.columnaauxiliarhtml += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Simbolo", Variables.auxiliarlexicohtml, Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

        # Verificar Comillas Simples O Dobles (Cadenas De Texto)
        elif re.search(r"[\"']", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Sumar Numero De Comillas
            Variables.numerocomillas += 1

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Simbolo", Variables.auxiliarlexicohtml, Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

            # Sumar Contador Tokens E Indice Del Array
            Variables.columnaauxiliarhtml += 1
            Variables.indexcaracterhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

            # Verificar Numero De Comillas
            if Variables.numerocomillas < 2:
                # Verificar Cadenas De Texto
                VerificarComillasHTML()

            if Variables.numerocomillas == 2:
                # Reiniciar Numero De Comillas
                Variables.numerocomillas = 0
                Variables.columnaauxiliarhtml -= 1

        # Verficar Errores Lexicos
        else:

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Sumar Columna
            Variables.columnaauxiliarhtml += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listaerroreshtml.append(
                [Variables.contadorerroreshtml, "Error_Lexico", Variables.auxiliarlexicohtml,
                 Variables.columnaauxiliarhtml, Variables.filaauxiliarhtml])

            if Variables.indexcaracterhtml + 1 < len(Variables.cadenaarchivo):


                if re.search(r"[a-zA-Z_ 0-9]", Variables.cadenaarchivo[Variables.indexcaracterhtml + 1]):

                    # Verificar Columna
                    Variables.columnaauxiliarhtml += 1

            # Sumar Contador Tokens E Indice Del Array
            Variables.indexcaracterhtml += 1
            Variables.contadorerroreshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

    # Colorear Texto
    Objetos.richtextboxarchivo.tag_add("black", "1.0", "end-1c")
    Objetos.richtextboxarchivo.tag_config("black", foreground="black")
    ColorearTexto.ColorearTextoHTML()

    # Generar Reporte De Errores
    if Variables.listaerroreshtml:

        showinfo("Error!", "Se Encontraron Errores En El Análisis!")

        ReporteErrores.ReporteErroresHTML()

        # Preguntar Si Se Desea Corregir El Archivo
        resultado = askyesno("Corregir Archivo!", "¿Desea Corregir El Archivo?")

        # Abrir Archivo
        if resultado:

            # Archivo Sin Errores
            Objetos.richtextboxarchivo.delete(1.0, "end-1c")
            Objetos.richtextboxarchivo.insert("end-1c", Variables.archivohtml)

        # Preguntar Si Se Desea Guardar El Archivo Corregido
        resultado = askyesno("Archivo Corregido!", "¿Desea Generar Un Archivo Sin Errores?")

        # Abrir Archivo
        if resultado:

            # Archivo Sin Errores
            Utilitarios.ArchivoSinErroresHTML(Variables.nombrearchivo)
    else:

        showinfo("Exito!", "El Análisis Se Completo Con Exito!")


# Verificar Palabras Reservadas E Identificadores
def VerificarReservasEIdentificadoresHTML():

    # Variables
    tipocadena = ""

    # Sumar Columna E Indice Array
    Variables.columnaauxiliarhtml += 1
    Variables.indexcaracterhtml += 1

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterhtml < len(Variables.cadenaarchivo):

        # Verificar Si Hay Mas Letras
        if re.search(r"[a-zA-Z]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Verificar Cadena Completa
            VerificarReservasEIdentificadoresHTML()

        # Verificar Si Hay Números
        elif re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Archivo Sin Errores
            Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

            # Verificar Cadena Completa
            VerificarReservasEIdentificadoresHTML()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarhtml -= 1

            # Asignar Tipo
            tipocadena = "Identificador"

            # Verificar Si Es Palabra Reservada
            for PalabraReservada in Variables.dicpalabrasreservadashtml:

                # Verificar Diccionario
                if Variables.auxiliarlexicohtml == PalabraReservada:
                    # Definir Tipo
                    tipocadena = "Palabra_Reservada"

            # Agregar Token A Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, tipocadena, Variables.auxiliarlexicohtml, Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

            # Verificar Si Hay Espacio O No
            if re.search(r"[a-zA-Z0-9 ]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):
                # Sumar Columna
                Variables.columnaauxiliarhtml += 1

            # Contador Tokens Y Vaciar Auxiliar Lexico
            Variables.contadortokenshtml += 1
            Variables.auxiliarlexicohtml = ""

    # Aceptar Cadena Como Valida (Final Del Archivo)
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarhtml -= 1

        # Asignar Tipo
        tipocadena = "Identificador"

        # Verificar Si Es Palabra Reservada
        for PalabraReservada in Variables.dicpalabrasreservadashtml:

            # Verificar Diccionario
            if Variables.auxiliarlexicohtml == PalabraReservada:
                # Definir Tipo
                tipocadena = "Palabra_Reservada"

                # Agregar Token A Lista
        Variables.listatokenshtml.append(
            [Variables.contadortokenshtml, tipocadena, Variables.auxiliarlexicohtml, Variables.columnaauxiliarhtml,
             Variables.filaauxiliarhtml])


# Verificar Cadenas De Texto
def VerificarCadenasDeTextoHTML():

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterhtml < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[<]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Verificar Espacios Vacios
            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoHTML()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoHTML()

            # Verificar Salto De Linea
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicohtml += "\n"

                # Sumar Fila E Indice Del Array, Reiniciar Columna
                Variables.columnaauxiliarhtml = 1
                Variables.filaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoHTML()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Existe Caracter
                Variables.existecaracter = True

                # Verificar Cadena Completa
                VerificarCadenasDeTextoHTML()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarhtml -= 1

            # Verificar Si Existe Caracter
            if Variables.existecaracter:
                # Agregar Token A La Lista
                Variables.listatokenshtml.append(
                    [Variables.contadortokenshtml, "Cadena", Variables.auxiliarlexicohtml,
                     Variables.columnaauxiliarhtml,
                     Variables.filaauxiliarhtml])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarhtml -= 1

        # Verificar Si Existe Caracter
        if Variables.existecaracter:
            # Agregar Token A La Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Cadena", Variables.auxiliarlexicohtml,
                 Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

        # Vaciar Auxiliar Lexico
        Variables.auxiliarlexicohtml = ""


# Verificar Comillas
def VerificarComillasHTML():

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterhtml < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[\"']", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Verificar Espacios Vacios

            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarComillasHTML()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarComillasHTML()

            # Verificar Salto De Linea
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Fila E Indice Del Array, Reiniciar Columna
                Variables.columnaauxiliarhtml = 1
                Variables.filaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarComillasHTML()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Existe Caracter
                Variables.existecaracter = True

                # Verificar Cadena Completa
                VerificarComillasHTML()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarhtml -= 1

            # Verificar Si Existe Caracter
            if Variables.existecaracter:
                # Agregar Token A La Lista
                Variables.listatokenshtml.append(
                    [Variables.contadortokenshtml, "Texto", Variables.auxiliarlexicohtml,
                     Variables.columnaauxiliarhtml,
                     Variables.filaauxiliarhtml])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarhtml -= 1

        # Verificar Si Existe Caracter
        if Variables.existecaracter:
            # Agregar Token A La Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Texto", Variables.auxiliarlexicohtml,
                 Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])


# Verificar Comentarios
def VerificarComentariosHTML():

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterhtml < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[!]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

            # Verificar Espacios Vacios            
            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarComentariosHTML()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarComentariosHTML()

            # Verificar Salto De Linea
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Fila E Indice Del Array, Reiniciar Columna
                Variables.columnaauxiliarhtml = 1
                Variables.filaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarComentariosHTML()

            # Verificar Signo -
            elif re.search(r"[\-]", Variables.cadenaarchivo[Variables.indexcaracterhtml]):

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna
                # Variables.columnaauxiliarhtml += 1

                # Aceptar Cadena Como Valida

                # Agregar Token A Lista
                Variables.listatokenshtml.append(
                    [Variables.contadortokenshtml, "Simbolo", "-",
                     Variables.columnaauxiliarhtml, Variables.filaauxiliarhtml])

                # Sumar Columna, Contador Tokens E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1
                Variables.contadortokenshtml += 1

                # Verificar Cadena Completa
                VerificarComentariosHTML()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Archivo Sin Errores
                Variables.archivohtml += Variables.cadenaarchivo[Variables.indexcaracterhtml]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarhtml += 1
                Variables.indexcaracterhtml += 1

                # Verificar Cadena Completa
                VerificarComentariosHTML()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarhtml -= 1

            # Agregar Token A La Lista
            Variables.listatokenshtml.append(
                [Variables.contadortokenshtml, "Comentario", Variables.auxiliarlexicohtml,
                 Variables.columnaauxiliarhtml,
                 Variables.filaauxiliarhtml])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarhtml += 1
            Variables.contadortokenshtml += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicohtml = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarhtml -= 1

        # Agregar Token A Lista
        Variables.listatokenshtml.append(
            [Variables.contadortokenshtml, "Comentario", Variables.auxiliarlexicohtml,
             Variables.columnaauxiliarhtml,
             Variables.filaauxiliarhtml])
