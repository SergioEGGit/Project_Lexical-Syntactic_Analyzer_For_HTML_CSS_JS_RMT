# ---------------------------------------------------Imports------------------------------------------------------------
import re

from tkinter.messagebox import showinfo, askyesno

from src.Design import Objetos
from src.Metodos import ColorearTexto, Utilitarios
from src.Reportes import ReporteErrores
from src.Analizadores import AnalizadorSintacticoRMT
from src.Variables import Variables


# ----------------------------------------------------Métodos-----------------------------------------------------------


# Analizador Lexico rmt
def AnalizadorLexicoRMT():

    # Variables
    bandera = False

    # Asignación
    Variables.columnaauxiliarrmt = 1
    Variables.filaauxiliarrmt = 1
    Variables.indexcaracterrmt = 0
    Variables.contadortokensrmt = 1
    Variables.contadorerroresrmt = 1
    Variables.numerocomillas = 0
    Variables.auxiliarlexicormt = ""
    Variables.archivormt = ""
    Variables.listatokensrmt[:] = []
    Variables.listaerroresrmt[:] = []
    Variables.listaerroreslexicosrmt[:] = []

    # Comienzo A Recorrer Archivo
    while Variables.indexcaracterrmt < len(Variables.cadenaarchivo):

        # Estados
        # Revisar Espacios Vacios
        if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1

        # Revisar Tabulaciones
        elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1

        # Revisar Salto De Linea
        elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Sumar Fila E Indice Del Array, Reiniciar Columna
            Variables.columnaauxiliarrmt = 1
            Variables.filaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1

        # Revisar Identificadores
        elif re.search(r"[a-zA-Z]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Primer Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt = Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Verificar Palabra Completa
            VerificarIdentificadoresRMT()

        # Verificar Numeros Enteros / Decimales
        elif re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Primer Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt = Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Sumar Columna E Indice Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1

            # Verificar Palabra Completa
            VerificarNumerosEnterosDecimalesRMT()

        # Verificar Signo (+)
        elif re.search(r"[+]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Operador", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt, Variables.filaauxiliarrmt])

            # Reportes Automatas
            Variables.existesimbolo = True

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1
            Variables.contadortokensrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

        # Verificar Signo (-)
        elif re.search(r"[-]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Operador", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt, Variables.filaauxiliarrmt])

            # Reportes Automatas
            Variables.existesimbolo = True

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1
            Variables.contadortokensrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

        # Verificar Signo (*)
        elif re.search(r"[*]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Operador", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt, Variables.filaauxiliarrmt])

            # Reportes Automatas
            Variables.existesimbolo = True

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1
            Variables.contadortokensrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

        # Verificar Signo (/)
        elif re.search(r"[/]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Operador", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt, Variables.filaauxiliarrmt])

            # Reportes Automatas
            Variables.existesimbolo = True

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1
            Variables.contadortokensrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

        # Verificar Signo (()
        elif re.search(r"[(]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Simbolo", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt, Variables.filaauxiliarrmt])

            # Reportes Automatas
            Variables.existesimbolo = True

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1
            Variables.contadortokensrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

        # Verificar Signo ())
        elif re.search(r"[)]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Simbolo", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt, Variables.filaauxiliarrmt])

            # Reportes Automatas
            Variables.existesimbolo = True

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1
            Variables.contadortokensrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

        # Verficar Errores Lexicos
        else:

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listaerroresrmt.append(
                [Variables.contadorerroresrmt, "Error_Lexico", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt, Variables.filaauxiliarrmt])

            bandera = False

            for Fila in Variables.listaerroreslexicosrmt:

                if Fila == Variables.filaauxiliarrmt:
                    bandera = True

            if not bandera:
                Variables.listaerroreslexicosrmt.append(Variables.filaauxiliarrmt)

                # Sumar Contador Tokens E Indice Del Array
            Variables.indexcaracterrmt += 1
            Variables.columnaauxiliarrmt += 1
            Variables.contadorerroresrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

    # Colorear Texto
    Objetos.richtextboxarchivo.tag_add("black", "1.0", "end-1c")
    Objetos.richtextboxarchivo.tag_config("black", foreground="black")
    ColorearTexto.ColorearTextoRMT()

    # Generar Reporte De Errores
    if Variables.listaerroresrmt:

        showinfo("Error!", "Se Encontraron Errores En El Análisis!")

        ReporteErrores.ReporteErroresRMT()

        # Preguntar Si Se Desea Corregir El Archivo
        resultado = askyesno("Corregir Archivo!", "¿Desea Corregir El Archivo?")

        # Abrir Archivo
        if resultado:
            # Archivo Sin Errores
            Objetos.richtextboxarchivo.delete(1.0, "end-1c")
            Objetos.richtextboxarchivo.insert("end-1c", Variables.archivormt)

        # Preguntar Si Se Desea Guardar El Archivo Corregido
        resultado = askyesno("Archivo Corregido!", "¿Desea Generar Un Archivo Sin Errores?")

        # Abrir Archivo
        if resultado:
            # Archivo Sin Errores
            Utilitarios.ArchivoSinErroresRMT(Variables.nombrearchivo)

    else:

        showinfo("Exito!", "El Análisis Se Completo Con Exito!")

    # Análisis Sintactico
    AnalizadorSintacticoRMT.AnalizadorSintacticoRMT()


# Verificar Identificadores
def VerificarIdentificadoresRMT():
    # Sumar Columna E Indice Array
    Variables.columnaauxiliarrmt += 1
    Variables.indexcaracterrmt += 1

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterrmt < len(Variables.cadenaarchivo):

        # Verificar Si Hay Mas Letras
        if re.search(r"[a-zA-Z_]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Verificar Cadena Completa
            VerificarIdentificadoresRMT()

        # Verificar Si Hay Números
        elif re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Verificar Cadena Completa
            VerificarIdentificadoresRMT()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarrmt -= 1

            # Agregar Token A Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Identificador", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt,
                 Variables.filaauxiliarrmt])

            # Contador Tokens Y Vaciar Auxiliar Lexico
            Variables.contadortokensrmt += 1
            Variables.columnaauxiliarrmt += 1
            Variables.auxiliarlexicormt = ""

    # Aceptar Cadena Como Valida (Final Del Archivo)
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarrmt -= 1

        # Agregar Token A Lista
        Variables.listatokensrmt.append(
            [Variables.contadortokensrmt, "Identificador", Variables.auxiliarlexicormt, Variables.columnaauxiliarrmt,
             Variables.filaauxiliarrmt])


# Verificar Numeros Enteros - Decimales
def VerificarNumerosEnterosDecimalesRMT():
    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterrmt < len(Variables.cadenaarchivo):

        # Verificar Mas Numeros
        if re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1

            # Verificar Cadena Completa
            VerificarNumerosEnterosDecimalesRMT()

        # Verificar Punto
        elif re.search(r"[.]", Variables.cadenaarchivo[Variables.indexcaracterrmt]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Archivo Sin Errores
            Variables.archivormt += Variables.cadenaarchivo[Variables.indexcaracterrmt]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarrmt += 1
            Variables.indexcaracterrmt += 1

            # Verificar Cadena Completa
            VerificarNumerosEnterosDecimalesRMT()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarrmt -= 1

            # Agregar Token A La Lista
            Variables.listatokensrmt.append(
                [Variables.contadortokensrmt, "Numero", Variables.auxiliarlexicormt,
                 Variables.columnaauxiliarrmt,
                 Variables.filaauxiliarrmt])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarrmt += 1
            Variables.contadortokensrmt += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicormt = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarrmt -= 1

        # Agregar Token A La Lista
        Variables.listatokensrmt.append(
            [Variables.contadortokensrmt, "Numero", Variables.auxiliarlexicormt,
             Variables.columnaauxiliarrmt,
             Variables.filaauxiliarrmt])
