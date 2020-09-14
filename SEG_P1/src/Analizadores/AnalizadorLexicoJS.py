# ---------------------------------------------------Imports------------------------------------------------------------
import re

from src.Variables import Variables

# ----------------------------------------------------Métodos-----------------------------------------------------------


# Analizador Lexico js
def AnalizadorLexicoJS():

    # Asignación
    Variables.columnaauxiliarjs = 1
    Variables.filaauxiliarjs = 1
    Variables.indexcaracterjs = 0
    Variables.contadortokensjs = 1
    Variables.contadorerroresjs = 1
    Variables.numerocomillas = 0
    Variables.auxiliarlexicojs = ""
    Variables.archivojs = ""
    Variables.listatokensjs[:] = []
    Variables.listaerroresjs[:] = []

    # Comienzo A Recorrer Archivo
    while Variables.indexcaracterjs < len(Variables.cadenaarchivo):

        # Estados
        # Revisar Espacios Vacios
        if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1

        # Revisar Tabulaciones
        elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1

        # Revisar Salto De Linea
        elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Sumar Fila E Indice Del Array, Reiniciar Columna
            Variables.columnaauxiliarjs = 1
            Variables.filaauxiliarjs += 1
            Variables.indexcaracterjs += 1

        # Verificar Comentarios Unilinea - Multilinea (/)
        elif re.search(r"[/]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            if Variables.indexcaracterjs + 1 < len(Variables.cadenaarchivo):

                if Variables.cadenaarchivo[Variables.indexcaracterjs + 1] == "/":
                    
                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Archivo Sin Errores
                    Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokensjs.append(
                        [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                         Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarjs += 1
                    Variables.indexcaracterjs += 1
                    Variables.contadortokensjs += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicojs = ""

                    # Verificar Cadena Completa
                    VerificarComentariosUnilineaJS()

                else:

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Archivo Sin Errores
                    Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokensjs.append(
                        [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                         Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarjs += 1
                    Variables.indexcaracterjs += 1
                    Variables.contadortokensjs += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicojs = ""

            else:

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Aceptar Cadena Como Valida

                # Agregar Token A Lista
                Variables.listatokensjs.append(
                    [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                     Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

                # Sumar Columna, Contador Tokens E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1
                Variables.contadortokensjs += 1

                # Vaciar Auxiliar Lexico
                Variables.auxiliarlexicojs = ""

        # Verificar Comentarios Unilinea - Multilinea (*)
        elif re.search(r"[*]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            if Variables.indexcaracterjs - 1 > 0:

                if Variables.cadenaarchivo[Variables.indexcaracterjs - 1] == "/":

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Archivo Sin Errores
                    Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokensjs.append(
                        [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                         Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarjs += 1
                    Variables.indexcaracterjs += 1
                    Variables.contadortokensjs += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicojs = ""

                    # Verificar Cadena Completa
                    VerificarComentariosMultilineaJS()

                else:

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Archivo Sin Errores
                    Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokensjs.append(
                        [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                         Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarjs += 1
                    Variables.indexcaracterjs += 1
                    Variables.contadortokensjs += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicojs = ""

            else:

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Aceptar Cadena Como Valida

                # Agregar Token A Lista
                Variables.listatokensjs.append(
                    [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                     Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

                # Sumar Columna, Contador Tokens E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1
                Variables.contadortokensjs += 1

                # Vaciar Auxiliar Lexico
                Variables.auxiliarlexicojs = ""
                       
        # Verificar Palabras Reservas / Identificadores
        elif re.search(r"[a-zA-Z]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Primer Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs = Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Verificar Palabra Completa
            VerificarReservadasEIdentificadoresJS()

        # Verificar Numeros Enteros / Decimales
        elif re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Primer Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs = Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Sumar Columna E Indice Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1

            # Verificar Palabra Completa
            VerificarNumerosEnterosDecimalesJS()

        # Verificar Signo Igual (=)
        elif re.search(r"[=]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Cadenas De Texto - Signo (")
        elif re.search(r"[\"]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Sumar Numero De Comillas
            Variables.numerocomillas += 1

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs, Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])

            # Sumar Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

            # Verificar Numero De Comillas
            if Variables.numerocomillas < 2:
                # Verificar Cadenas De Texto
                VerificarCadenasDeTextoComillasDoblesJS()

            if Variables.numerocomillas == 2:
                # Reiniciar Numero De Comillas
                Variables.numerocomillas = 0

        # Verificar Cadenas De Texto - Signo (')
        elif re.search(r"[']", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Sumar Numero De Comillas
            Variables.numerocomillas += 1

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs, Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])

            # Sumar Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

            # Verificar Numero De Comillas
            if Variables.numerocomillas < 2:
                # Verificar Cadenas De Texto
                VerificarCadenasDeTextoComillasSimplesJS()

            if Variables.numerocomillas == 2:
                # Reiniciar Numero De Comillas
                Variables.numerocomillas = 0

        # Verificar Signo (:)
        elif re.search(r"[:]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (;)
        elif re.search(r"[;]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (.)
        elif re.search(r"[.]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (,)
        elif re.search(r"[,]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (()
        elif re.search(r"[(]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo ())
        elif re.search(r"[)]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo ({)
        elif re.search(r"[{]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (})
        elif re.search(r"[}]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (<)
        elif re.search(r"[<]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (>)
        elif re.search(r"[>]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (+)
        elif re.search(r"[+]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

         # Verificar Signo (-)
        elif re.search(r"[-]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verificar Signo (&)
        elif re.search(r"[&]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

        # Verficar Errores Lexicos
        else:

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listaerroresjs.append(
                [Variables.contadorerroresjs, "Error_Lexico", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

            # Sumar Contador Tokens E Indice Del Array
            Variables.indexcaracterjs += 1
            Variables.columnaauxiliarjs += 1
            Variables.contadorerroresjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""


# Verificar Palabras Reservadas E Identificadores
def VerificarReservadasEIdentificadoresJS():
    
    # Variables
    tipocadena = ""

    # Sumar Columna E Indice Array
    Variables.columnaauxiliarjs += 1
    Variables.indexcaracterjs += 1

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterjs < len(Variables.cadenaarchivo):

        # Verificar Si Hay Mas Letras
        if re.search(r"[a-zA-Z_]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Verificar Cadena Completa
            VerificarReservadasEIdentificadoresJS()

        # Verificar Si Hay Números
        elif re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Verificar Cadena Completa
            VerificarReservadasEIdentificadoresJS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarjs -= 1

            # Asignar Tipo
            tipocadena = "Identificador"

            # Verificar Si Es Palabra Reservada
            for PalabraReservada in Variables.dicpalabrasreservadasjs:

                # Verificar Diccionario
                if Variables.auxiliarlexicojs == PalabraReservada:

                    # Verificar Diccionario
                    if PalabraReservada == "true" or PalabraReservada == "false":

                        # Definir Tipo
                        tipocadena = "Boolean"
                    else:

                        # Definir Tipo
                        tipocadena = "Palabra_Reservada"

            # Agregar Token A Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, tipocadena, Variables.auxiliarlexicojs, Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])

            # Contador Tokens Y Vaciar Auxiliar Lexico
            Variables.contadortokensjs += 1
            Variables.columnaauxiliarjs += 1
            Variables.auxiliarlexicojs = ""

    # Aceptar Cadena Como Valida (Final Del Archivo)
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarjs -= 1

        # Asignar Tipo
        tipocadena = "Identificador"

        # Verificar Si Es Palabra Reservada
        for PalabraReservada in Variables.dicpalabrasreservadasjs:

            # Verificar Diccionario
            if Variables.auxiliarlexicojs == PalabraReservada:

                # Verificar Diccionario
                if PalabraReservada == "true" or PalabraReservada == "false":

                    # Definir Tipo
                    tipocadena = "Boolean"
                else:

                    # Definir Tipo
                    tipocadena = "Palabra_Reservada"

        # Agregar Token A Lista
        Variables.listatokensjs.append(
            [Variables.contadortokensjs, tipocadena, Variables.auxiliarlexicojs, Variables.columnaauxiliarjs,
             Variables.filaauxiliarjs])


# Verificar Numeros Enteros - Decimales
def VerificarNumerosEnterosDecimalesJS():

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterjs < len(Variables.cadenaarchivo):

        # Verificar Mas Numeros
        if re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1

            # Verificar Cadena Completa
            VerificarNumerosEnterosDecimalesJS()

        # Verificar Punto
        elif re.search(r"[.]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Archivo Sin Errores
            Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarjs += 1
            Variables.indexcaracterjs += 1

            # Verificar Cadena Completa
            VerificarNumerosEnterosDecimalesJS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarjs -= 1

            # Agregar Token A La Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Numeros", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarjs -= 1

        # Agregar Token A La Lista
        Variables.listatokensjs.append(
            [Variables.contadortokensjs, "Numeros", Variables.auxiliarlexicojs,
             Variables.columnaauxiliarjs,
             Variables.filaauxiliarjs])


# Verificar Comentarios Unilinea
def VerificarComentariosUnilineaJS():
   
    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterjs < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Verificar Simbolo /
            if re.search(r"[/]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Aceptar Cadena Como Valida

                # Agregar Token A Lista
                Variables.listatokensjs.append(
                    [Variables.contadortokensjs, "Simbolo", Variables.auxiliarlexicojs,
                     Variables.columnaauxiliarjs, Variables.filaauxiliarjs])

                # Sumar Columna, Contador Tokens E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1
                Variables.contadortokensjs += 1

                # Vaciar Auxiliar Lexico
                Variables.auxiliarlexicojs = ""

                # Verificar Cadena Completa
                VerificarComentariosUnilineaJS()

            # Verificar Espacios Vacios
            elif re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosUnilineaJS()

            # Verificar Espacios Vacios
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.filaauxiliarjs += 1
                Variables.columnaauxiliarjs = 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosUnilineaJS()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosUnilineaJS()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosUnilineaJS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarjs -= 1

            # Agregar Token A La Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Comentario_UniLinea", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarjs -= 1

        # Agregar Token A La Lista
        Variables.listatokensjs.append(
            [Variables.contadortokensjs, "Comentario_UniLinea", Variables.auxiliarlexicojs,
             Variables.columnaauxiliarjs,
             Variables.filaauxiliarjs])
        

# Verificar Cadenas De Texto
def VerificarCadenasDeTextoComillasDoblesJS():

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterjs < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[\"]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Verificar Espacios Vacios
            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasDoblesJS()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasDoblesJS()

            # Verificar Salto De Linea
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Fila E Indice Del Array, Reiniciar Columna
                Variables.columnaauxiliarjs = 1
                Variables.filaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasDoblesJS()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Existe Caracter
                Variables.existecaracter = True

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasDoblesJS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarjs -= 1

            # Verificar Si Existe Caracter
            if Variables.existecaracter:
                # Agregar Token A La Lista
                Variables.listatokensjs.append(
                    [Variables.contadortokensjs, "Texto", Variables.auxiliarlexicojs,
                     Variables.columnaauxiliarjs,
                     Variables.filaauxiliarjs])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarjs -= 1

        # Verificar Si Existe Caracter
        if Variables.existecaracter:
            # Agregar Token A La Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Texto", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])


# Verificar Cadenas De Texto
def VerificarCadenasDeTextoComillasSimplesJS():

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterjs < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[']", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Verificar Espacios Vacios
            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasSimplesJS()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasSimplesJS()

            # Verificar Salto De Linea
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Fila E Indice Del Array, Reiniciar Columna
                Variables.columnaauxiliarjs = 1
                Variables.filaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasSimplesJS()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Existe Caracter
                Variables.existecaracter = True

                # Verificar Cadena Completa
                VerificarCadenasDeTextoComillasSimplesJS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarjs -= 1

            # Verificar Si Existe Caracter
            if Variables.existecaracter:
                # Agregar Token A La Lista
                Variables.listatokensjs.append(
                    [Variables.contadortokensjs, "Texto", Variables.auxiliarlexicojs,
                     Variables.columnaauxiliarjs,
                     Variables.filaauxiliarjs])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarjs -= 1

        # Verificar Si Existe Caracter
        if Variables.existecaracter:
            # Agregar Token A La Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Texto", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])

        
# Verificar Comentarios Multilinea
def VerificarComentariosMultilineaJS():

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaracterjs < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[*]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

            # Verificar Espacios Vacios
            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosMultilineaJS()

            # Verificar Espacios Vacios
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.filaauxiliarjs += 1
                Variables.columnaauxiliarjs = 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosMultilineaJS()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaracterjs]):

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosMultilineaJS()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Archivo Sin Errores
                Variables.archivojs += Variables.cadenaarchivo[Variables.indexcaracterjs]

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarjs += 1
                Variables.indexcaracterjs += 1

                # Verificar Cadena Completa
                VerificarComentariosMultilineaJS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarjs -= 1

            # Agregar Token A La Lista
            Variables.listatokensjs.append(
                [Variables.contadortokensjs, "Comentario_MultiLinea", Variables.auxiliarlexicojs,
                 Variables.columnaauxiliarjs,
                 Variables.filaauxiliarjs])

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarjs += 1
            Variables.contadortokensjs += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicojs = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarjs -= 1

        # Agregar Token A La Lista
        Variables.listatokensjs.append(
            [Variables.contadortokensjs, "Comentario_MultiLinea", Variables.auxiliarlexicojs,
             Variables.columnaauxiliarjs,
             Variables.filaauxiliarjs])
