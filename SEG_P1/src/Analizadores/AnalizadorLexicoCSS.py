# ---------------------------------------------------Imports------------------------------------------------------------
import re

from tkinter.messagebox import showinfo, askyesno

from src.Design import Objetos
from src.Metodos import ColorearTexto, Utilitarios
from src.Reportes import ReporteErrores
from src.Variables import Variables


# ----------------------------------------------------Métodos-----------------------------------------------------------


# Analizador Lexico CSS
def AnalizadorLexicoCSS():
    # Asignación
    Variables.columnaauxiliarcss = 1
    Variables.filaauxiliarcss = 1
    Variables.indexcaractercss = 0
    Variables.contadortokenscss = 1
    Variables.contadorerrorescss = 1
    Variables.numerocomillas = 0
    Variables.contadorbitacora = 0
    Variables.auxiliarlexicocss = ""
    Variables.archivocss = ""
    Variables.bitacoracss[:] = []
    Variables.listatokenscss[:] = []
    Variables.listaerrorescss[:] = []
    Variables.numeral = False

    # Comienzo A Recorrer Archivo
    while Variables.indexcaractercss < len(Variables.cadenaarchivo):

        # Estados
        # Agregar Estado 0 A Bitacora
        Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 0: Inicio", "Lexema: None"])
        Variables.contadorbitacora += 1

        # Revisar Espacios Vacios
        if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Agregar Estado 1 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 1: Espacios Vacios", "Lexema: "
                                                                                                   "Espacio Vacio"])
            Variables.contadorbitacora += 1

        # Revisar Tabulaciones
        elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Agregar Estado 2 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 2: Tabulaciones", "Lexema: \\t"])
            Variables.contadorbitacora += 1

        # Revisar Salto De Linea
        elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Fila E Indice Del Array, Reiniciar Columna
            Variables.columnaauxiliarcss = 1
            Variables.filaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Agregar Estado 3 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 3: Salto De Linea", "Lexema: \\n"])
            Variables.contadorbitacora += 1

        # Verificar Palabras Reservas / Identificadores
        elif re.search(r"[a-zA-Z]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Primer Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss = Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 4 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 4: Comienza Reconocimento De "
                                                                      "Identificadores/Palabras Reservadas",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Verifiicar Palabra Completa
            VerificarReservasEIdentificadoresCSS()

        # Verificar Numeros Enteros/Decimales
        elif re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Primer Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss = Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 8 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 8: Comienza Reconocimento De Numeros",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Sumar Columna E Indice Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Verifiicar Palabra Completa
            VerificarNumerosCSS()

        # Verificar Signo / (Comentarios)
        elif re.search(r"[/]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Verificar Si Estoy Al Final Del Archivo
            if Variables.indexcaractercss + 1 < len(Variables.cadenaarchivo):

                if Variables.cadenaarchivo[Variables.indexcaractercss + 1] == "*":

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Archivo Sin Errores
                    Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokenscss.append(
                        [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                         Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                    # Agregar Estado 13 A Bitacora
                    Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 13: Aceptacion Simbolo /",
                                                  "Token Aceptado: /"])
                    Variables.contadorbitacora += 1

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarcss += 1
                    Variables.indexcaractercss += 1
                    Variables.contadortokenscss += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicocss = ""

                elif Variables.cadenaarchivo[Variables.indexcaractercss - 1] == "*":

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Archivo Sin Errores
                    Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokenscss.append(
                        [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                         Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                    # Agregar Estado 13 A Bitacora
                    Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 13: Aceptacion Simbolo /",
                                                  "Token Aceptado: /"])
                    Variables.contadorbitacora += 1

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarcss += 1
                    Variables.indexcaractercss += 1
                    Variables.contadortokenscss += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicocss = ""

                else:

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Sumar Columna
                    Variables.columnaauxiliarcss += 1

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listaerrorescss.append(
                        [Variables.contadorerrorescss, "Error_Lexico", Variables.auxiliarlexicocss,
                         Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                    # Agregar Estado Error A Bitacora
                    Variables.bitacoracss.append([Variables.contadorbitacora, "Estado Error: Error Lexico",
                                                  "Error: /"])
                    Variables.contadorbitacora += 1

                    # Sumar Contador Tokens E Indice Del Array
                    Variables.indexcaractercss += 1
                    Variables.contadorerrorescss += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicocss = ""

            else:

                if Variables.cadenaarchivo[Variables.indexcaractercss - 1] == "*":

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Archivo Sin Errores
                    Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokenscss.append(
                        [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                         Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                    # Agregar Estado 13 A Bitacora
                    Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 13: Aceptacion Simbolo /",
                                                  "Token Aceptado: /"])
                    Variables.contadorbitacora += 1

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarcss += 1
                    Variables.indexcaractercss += 1
                    Variables.contadortokenscss += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicocss = ""

                else:

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Sumar Columna
                    Variables.columnaauxiliarcss += 1

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listaerrorescss.append(
                        [Variables.contadorerrorescss, "Error_Lexico", Variables.auxiliarlexicocss,
                         Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                    # Agregar Estado Error A Bitacora
                    Variables.bitacoracss.append([Variables.contadorbitacora, "Estado Error: Error Lexico",
                                                  "Error: /"])
                    Variables.contadorbitacora += 1

                    # Sumar Contador Tokens E Indice Del Array
                    Variables.indexcaractercss += 1
                    Variables.contadorerrorescss += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicocss = ""

        # Verificar Signo * (Comentario)
        elif re.search(r"[*]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Verificar Si Estoy Al Final De Archivo
            if Variables.indexcaractercss + 1 < len(Variables.cadenaarchivo):

                if Variables.cadenaarchivo[Variables.indexcaractercss - 1] == "/":

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Archivo Sin Errores
                    Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Aceptar Cadena Como Valida

                    # Agregar Token A Lista
                    Variables.listatokenscss.append(
                        [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                         Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                    # Agregar Estado 14 A Bitacora
                    Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 14: Aceptacion Simbolo *"
                                                                              " - Comienza Reconocimiento De "
                                                                              "Comentarios",
                                                  "Token Aceptado: *"])
                    Variables.contadorbitacora += 1

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarcss += 1
                    Variables.indexcaractercss += 1
                    Variables.contadortokenscss += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicocss = ""

                    # Verificar Comentario
                    VerificarComentariosCSS()

                else:

                    # Agregar Caracter A Auxiliar Lexico
                    Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Archivo Sin Errores
                    Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                    # Sumar Columna
                    if Variables.contadortokenscss - 2 >= 0:

                        if Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Comentario" or \
                                Variables.listatokenscss[Variables.contadortokenscss - 2][
                                    1].strip() == "Identificador" or \
                                Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == \
                                "Palabra_Reservada":
                            Variables.columnaauxiliarcss += 1

                    # Agregar Token A Lista
                    Variables.listatokenscss.append(
                        [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                         Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                    # Agregar Estado 14 A Bitacora
                    Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 14: Aceptacion Simbolo *",
                                                  "Token Aceptado: *"])
                    Variables.contadorbitacora += 1

                    # Sumar Columna, Contador Tokens E Indice Del Array
                    Variables.columnaauxiliarcss += 1
                    Variables.indexcaractercss += 1
                    Variables.contadortokenscss += 1

                    # Vaciar Auxiliar Lexico
                    Variables.auxiliarlexicocss = ""

            else:

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Aceptar Cadena Como Valida
                # Variables.columnaauxiliarcss += 1

                # Agregar Token A Lista
                Variables.listatokenscss.append(
                    [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                     Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

                # Agregar Estado 14 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 14: Aceptacion Simbolo *",
                                              "Token Aceptado: *"])
                Variables.contadorbitacora += 1

                # Sumar Columna, Contador Tokens E Indice Del Array
                Variables.columnaauxiliarcss += 1
                Variables.indexcaractercss += 1
                Variables.contadortokenscss += 1

                # Vaciar Auxiliar Lexico
                Variables.auxiliarlexicocss = ""

        # Verificar Signo {
        elif re.search(r"[{]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            if Variables.contadortokenscss - 2 >= 0:

                if Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Identificador" or \
                        Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Palabra_Reservada":
                    Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 20 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 20: Aceptacion Simbolo {",
                                          "Token Aceptado: {"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            if not Variables.numeral:
                Variables.columnaauxiliarcss += 1
                Variables.numeral = False

            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo %
        elif re.search(r"[%]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            if Variables.indexcaractercss - 1 > 0:

                if re.search(r"[a-zA-Z_0-9]", Variables.cadenaarchivo[Variables.indexcaractercss - 1]):
                    print("")
                    # Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 20 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 12: Aceptacion Simbolo %",
                                          "Token Aceptado: %"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo }
        elif re.search(r"[}]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 21 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 21: Aceptacion Simbolo }",
                                          "Token Aceptado: }"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo :
        elif re.search(r"[:]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            if Variables.contadortokenscss - 2 >= 0:

                if Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Identificador" or \
                        Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Palabra_Reservada":
                    Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 22 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 22: Aceptacion Simbolo :",
                                          "Token Aceptado: :"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo ;
        elif re.search(r"[;]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            if Variables.contadortokenscss - 2 >= 0:

                if Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Identificador" or \
                        Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Palabra_Reservada":
                    Variables.columnaauxiliarcss += 1

            # Sumar Columna
            # Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 23 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 23: Aceptacion Simbolo ;",
                                          "Token Aceptado: ;"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo ,
        elif re.search(r"[,]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            if Variables.contadortokenscss - 2 >= 0:

                if Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Identificador" or \
                        Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Palabra_Reservada":
                    Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 24 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 24: Aceptacion Simbolo ,",
                                          "Token Aceptado: ,"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo -
        elif re.search(r"[\-]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            # Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Operador", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 25 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 25: Aceptacion Simbolo -",
                                          "Token Aceptado: -"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo (
        elif re.search(r"[(]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 26 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 26: Aceptacion Simbolo (",
                                          "Token Aceptado: ("])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Signo )
        elif re.search(r"[)]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 27 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 27: Aceptacion Simbolo )",
                                          "Token Aceptado: )"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

        # Verificar Comillas Simples O Dobles (Cadenas De Texto)
        elif re.search(r"[\"]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Sumar Numero De Comillas
            Variables.numerocomillas += 1

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss, Variables.columnaauxiliarcss,
                 Variables.filaauxiliarcss])

            # Agregar Estado 28 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 28: Aceptacion Simbolo \" - Comienza"
                                                                      "Reconocimiento Cadenas De Texto",
                                          "Token Aceptado: \""])
            Variables.contadorbitacora += 1

            # Sumar Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

            # Verificar Numero De Comillas
            if Variables.numerocomillas < 2:
                # Verificar Cadenas De Texto
                VerificarComillasCSS()

            if Variables.numerocomillas == 2:
                # Reiniciar Numero De Comillas
                Variables.numerocomillas = 0
                Variables.columnaauxiliarcss -= 1

        # Verificar Signo #
        elif re.search(r"[#]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            if Variables.contadortokenscss - 2 >= 0:

                if Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Identificador" or \
                        Variables.listatokenscss[Variables.contadortokenscss - 2][1].strip() == "Palabra_Reservada":
                    Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 34 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 34: Aceptacion Simbolo #",
                                          "Token Aceptado: #"])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

            VerificarSignoNumeralCSS()

        # Verificar Signo .
        elif re.search(r"[.]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Simbolo", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Agregar Estado 38 A Bitacora
            Variables.bitacoracss.append(
                [Variables.contadorbitacora, "Estado 38: Aceptacion Simbolo . - Comienza Reconocimiento"
                                             " Cadena Especial",
                 "Token Aceptado: ."])
            Variables.contadorbitacora += 1

            # Sumar Columna, Contador Tokens E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

            # Verificar Color
            VerificarSignoPuntoCSS()

        # Verficar Errores Lexicos
        else:

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Sumar Columna
            if Variables.contadortokenscss - 2 > 0:

                if Variables.indexcaractercss + 1 < len(Variables.cadenaarchivo):

                    if Variables.cadenaarchivo[Variables.indexcaractercss - 1] == " ":

                        Variables.columnaauxiliarcss += 1

                    elif Variables.listatokenscss[Variables.contadortokenscss - 2][1] == "Identificador" or \
                            Variables.listatokenscss[Variables.contadortokenscss - 2][1] == "Palabra_Reservada":

                        if Variables.contadortokenscss - 3 > 0:

                            if Variables.listatokenscss[Variables.contadortokenscss - 3][2] == "#":

                                # Variables.columnaauxiliarcss -= 1
                                print("")

                            else:

                                Variables.columnaauxiliarcss += 1
                        else:

                            Variables.columnaauxiliarcss += 1

                    else:

                        Variables.columnaauxiliarcss += 1

                else:

                    if Variables.listatokenscss[Variables.contadortokenscss - 2][1] == "Identificador" or \
                            Variables.listatokenscss[Variables.contadortokenscss - 2][1] == "Palabra_Reservada":

                        if Variables.contadortokenscss - 3 > 0:

                            if Variables.listatokenscss[Variables.contadortokenscss - 3][2] == "#":

                                # Variables.columnaauxiliarcss -= 1
                                print("")

                            else:

                                Variables.columnaauxiliarcss += 1
                        else:

                            Variables.columnaauxiliarcss += 1
                    else:

                        Variables.columnaauxiliarcss += 1

            # Aceptar Cadena Como Valida

            # Agregar Token A Lista
            Variables.listaerrorescss.append(
                [Variables.contadorerrorescss, "Error_Lexico", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss, Variables.filaauxiliarcss])

            # Sumar Contador Tokens E Indice Del Array

            if Variables.indexcaractercss + 1 < len(Variables.cadenaarchivo):

                if re.search(r"[a-zA-Z-0-9]", Variables.cadenaarchivo[Variables.indexcaractercss + 1]):

                    Variables.columnaauxiliarcss += 1

            Variables.indexcaractercss += 1
            Variables.contadorerrorescss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

    # Colorear Texto
    Objetos.richtextboxarchivo.tag_add("black", "1.0", "end-1c")
    Objetos.richtextboxarchivo.tag_config("black", foreground="black")
    ColorearTexto.ColorearTextoCSS()

    # Generar Reporte De Errores
    if Variables.listaerrorescss:

        showinfo("Error!", "Se Encontraron Errores En El Análisis!")

        ReporteErrores.ReporteErroresCSS()

        # Preguntar Si Se Desea Corregir El Archivo
        resultado = askyesno("Corregir Archivo!", "¿Desea Corregir El Archivo?")

        # Abrir Archivo
        if resultado:
            # Archivo Sin Errores
            Objetos.richtextboxarchivo.delete(1.0, "end-1c")
            Objetos.richtextboxarchivo.insert("end-1c", Variables.archivocss)

        # Preguntar Si Se Desea Guardar El Archivo Corregido
        resultado = askyesno("Archivo Corregido!", "¿Desea Generar Un Archivo Sin Errores?")

        # Abrir Archivo
        if resultado:
            # Archivo Sin Errores
            Utilitarios.ArchivoSinErroresCSS(Variables.nombrearchivo)

    else:

        showinfo("Exito!", "El Análisis Se Completo Con Exito!")


# Verificar Palabras Reservadas E Identificadores
def VerificarReservasEIdentificadoresCSS():
    # Variables
    tipocadena = ""

    # Sumar Columna E Indice Array
    Variables.columnaauxiliarcss += 1
    Variables.indexcaractercss += 1

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaractercss < len(Variables.cadenaarchivo):

        # Verificar Si Hay Mas Letras
        if re.search(r"[a-zA-Z\-]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 5 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 5: Letras Y Simbolo - Identificadores"
                                                                      "/Palabras Reservadas",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Verificar Cadena Completa
            VerificarReservasEIdentificadoresCSS()

        # Verificar Si Hay Números
        elif re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 6 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 6: Digitos Identificadores"
                                                                      "/Palabras Reservadas",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Verificar Cadena Completa
            VerificarReservasEIdentificadoresCSS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarcss -= 1
            Variables.numeral = False

            # Asignar Tipo
            tipocadena = "Identificador"

            # Verificar Si Es Palabra Reservada
            for PalabraReservada in Variables.dicpalabrasreservadascss:

                # Verificar Diccionario
                if Variables.auxiliarlexicocss == PalabraReservada:
                    # Definir Tipo
                    tipocadena = "Palabra_Reservada"

            # Agregar Token A Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, tipocadena, Variables.auxiliarlexicocss, Variables.columnaauxiliarcss,
                 Variables.filaauxiliarcss])

            # Agregar Estado 7 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 7: Aceptacion Identificadores"
                                                                      "/Palabras Reservadas",
                                          "Token Aceptado: " + Variables.auxiliarlexicocss])
            Variables.contadorbitacora += 1

            # Verificar Si Hay Espacio O No
            if re.search(r"[a-zA-Z0-9 ]", Variables.cadenaarchivo[Variables.indexcaractercss]):
                # Sumar Columna
                Variables.columnaauxiliarcss += 1

            # Contador Tokens Y Vaciar Auxiliar Lexico
            Variables.contadortokenscss += 1
            Variables.auxiliarlexicocss = ""

    # Aceptar Cadena Como Valida (Final Del Archivo)
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarcss -= 1
        Variables.numeral = False

        # Asignar Tipo
        tipocadena = "Identificador"

        # Verificar Si Es Palabra Reservada
        for PalabraReservada in Variables.dicpalabrasreservadascss:

            # Verificar Diccionario
            if Variables.auxiliarlexicocss == PalabraReservada:
                # Definir Tipo
                tipocadena = "Palabra_Reservada"

                # Agregar Token A Lista
        Variables.listatokenscss.append(
            [Variables.contadortokenscss, tipocadena, Variables.auxiliarlexicocss, Variables.columnaauxiliarcss,
             Variables.filaauxiliarcss])

        # Agregar Estado 7 A Bitacora
        Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 7: Aceptacion Identificadores"
                                                                  "/Palabras Reservadas",
                                      "Token Aceptado: " + Variables.auxiliarlexicocss])
        Variables.contadorbitacora += 1


# Verificar Numeros
def VerificarNumerosCSS():
    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaractercss < len(Variables.cadenaarchivo):

        # Verificar Mas Numeros
        if re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 9 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 9: Digito Numeros",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Verificar Cadena Completa
            VerificarNumerosCSS()

        # Verificar Punto
        elif re.search(r"[.]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 10 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 10: Signo . Numeros",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Verificar Cadena Completa
            VerificarNumerosCSS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarcss -= 1

            # Agregar Token A La Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Numero", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss,
                 Variables.filaauxiliarcss])

            # Agregar Estado 11 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 11: Aceptacion Numeros",
                                          "Token Aceptado: " + Variables.auxiliarlexicocss])
            Variables.contadorbitacora += 1

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarcss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarcss -= 1

        # Agregar Token A La Lista
        Variables.listatokenscss.append(
            [Variables.contadortokenscss, "Numero", Variables.auxiliarlexicocss,
             Variables.columnaauxiliarcss,
             Variables.filaauxiliarcss])

        # Agregar Estado 11 A Bitacora
        Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 11: Aceptacion Numeros",
                                      "Token Aceptado: " + Variables.auxiliarlexicocss])
        Variables.contadorbitacora += 1


# Verificar Identificadores Antes De #
def VerificarSignoNumeralCSS():
    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaractercss < len(Variables.cadenaarchivo):

        # Verificar Mas Numeros
        if re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaractercss]):
            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 35 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 35: Digitos Cadena Especial",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Verificar Cadena Completa
            VerificarSignoNumeralCSS()

        # Verificar Letras Y Simbolo -
        elif re.search(r"[a-zA-Z\-]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 36 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 36: Letras Y Simbolo - Cadena Especial",
                                          "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Verificar Cadena Completa
            VerificarSignoNumeralCSS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarcss -= 1
            Variables.numeral = True

            # Agregar Token A La Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Identificador", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss,
                 Variables.filaauxiliarcss])

            # Agregar Estado 37 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 37: Aceptacion Cadena Especial",
                                          "Token Aceptado: " + Variables.auxiliarlexicocss])
            Variables.contadorbitacora += 1

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarcss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarcss -= 1
        Variables.numeral = True

        # Agregar Token A La Lista
        Variables.listatokenscss.append(
            [Variables.contadortokenscss, "Identificador", Variables.auxiliarlexicocss,
             Variables.columnaauxiliarcss,
             Variables.filaauxiliarcss])

        # Agregar Estado 37 A Bitacora
        Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 37: Aceptacion Cadena Especial",
                                      "Token Aceptado: " + Variables.auxiliarlexicocss])
        Variables.contadorbitacora += 1


# Verificar Identificadores Antes De #
def VerificarSignoPuntoCSS():
    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaractercss < len(Variables.cadenaarchivo):

        # Verificar Mas Numeros
        if re.search(r"[0-9]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 39 A Bitacora
            Variables.bitacoracss.append(
                [Variables.contadorbitacora, "Estado 39: Digitos Cadena Especial",
                 "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Verificar Cadena Completa
            VerificarSignoPuntoCSS()

        # Verificar Punto
        elif re.search(r"[a-zA-Z\-]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Agregar Caracter A Auxiliar Lexico
            Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Archivo Sin Errores
            Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

            # Agregar Estado 40 A Bitacora
            Variables.bitacoracss.append(
                [Variables.contadorbitacora, "Estado 40: Letras Y Simbolo - Cadena Especial",
                 "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
            Variables.contadorbitacora += 1

            # Sumar Columna E Indice Del Array
            Variables.columnaauxiliarcss += 1
            Variables.indexcaractercss += 1

            # Verificar Cadena Completa
            VerificarSignoPuntoCSS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarcss -= 1

            # Agregar Token A La Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Identificador", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss,
                 Variables.filaauxiliarcss])

            # Agregar Estado 41 A Bitacora
            Variables.bitacoracss.append(
                [Variables.contadorbitacora, "Estado 41: Aceptacion Cadena Especial",
                 "Token Aceptado: " + Variables.auxiliarlexicocss])
            Variables.contadorbitacora += 1

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarcss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarcss -= 1

        # Agregar Token A La Lista
        Variables.listatokenscss.append(
            [Variables.contadortokenscss, "Identificaodr", Variables.auxiliarlexicocss,
             Variables.columnaauxiliarcss,
             Variables.filaauxiliarcss])

        # Agregar Estado 41 A Bitacora
        Variables.bitacoracss.append(
            [Variables.contadorbitacora, "Estado 41: Aceptacion Cadena Especial",
             "Token Aceptado: " + Variables.auxiliarlexicocss])
        Variables.contadorbitacora += 1


# Verificar Comentarios
def VerificarComentariosCSS():
    # Variables
    bandera = True

    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaractercss < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if re.search(r"[*]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            if Variables.indexcaractercss + 1 < len(Variables.cadenaarchivo):

                if re.search(r"[/]", Variables.cadenaarchivo[Variables.indexcaractercss + 1]):
                    bandera = False

            else:

                bandera = False

        if bandera:

            # Verificar Espacios Vacios
            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaractercss]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 15 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 15: Espacio Vacio Comentarios",
                                              "Lexema: Espacio Vacio"])
                Variables.contadorbitacora += 1

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarcss += 1
                Variables.indexcaractercss += 1

                # Verificar Cadena Completa
                VerificarComentariosCSS()

            # Verificar Espacios Vacios
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaractercss]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 16 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 16: Salto De Linea Comentarios",
                                              "Lexema: \\n"])
                Variables.contadorbitacora += 1

                # Sumar Columna E Indice Del Array
                Variables.filaauxiliarcss += 1
                Variables.columnaauxiliarcss = 1
                Variables.indexcaractercss += 1

                # Verificar Cadena Completa
                VerificarComentariosCSS()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaractercss]):

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 17 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 17: Tabulacion Comentarios",
                                              "Lexema: \\t"])
                Variables.contadorbitacora += 1

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarcss += 1
                Variables.indexcaractercss += 1

                # Verificar Cadena Completa
                VerificarComentariosCSS()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 18 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 18: Letras Y Signos Comentarios",
                                              "Lexema: " + Variables.cadenaarchivo[Variables.indexcaractercss]])
                Variables.contadorbitacora += 1

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarcss += 1
                Variables.indexcaractercss += 1

                # Verificar Cadena Completa
                VerificarComentariosCSS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarcss -= 1

            # Agregar Token A La Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Comentario", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss,
                 Variables.filaauxiliarcss])

            # Agregar Estado 19 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 19: Aceptacion Comentarios",
                                          "Token Aceptado: " + Variables.auxiliarlexicocss])
            Variables.contadorbitacora += 1

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarcss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarcss -= 1

        # Agregar Token A La Lista
        Variables.listatokenscss.append(
            [Variables.contadortokenscss, "Comentario", Variables.auxiliarlexicocss,
             Variables.columnaauxiliarcss,
             Variables.filaauxiliarcss])

        # Agregar Estado 19 A Bitacora
        Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 19: Aceptacion Comentarios",
                                      "Token Aceptado: " + Variables.auxiliarlexicocss])
        Variables.contadorbitacora += 1


# Verificar Comillas
def VerificarComillasCSS():
    # Verificar Si No Estoy Al Final Del Archivo
    if Variables.indexcaractercss < len(Variables.cadenaarchivo):

        # Verificar Si Es Cadena De Texto O Comienzo Etiqueta
        if not re.search(r"[\"]", Variables.cadenaarchivo[Variables.indexcaractercss]):

            # Verificar Espacios Vacios
            if re.search(r"[ ]", Variables.cadenaarchivo[Variables.indexcaractercss]):

                # Agregar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 29 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 29: Espacios Vacios Cadenas De "
                                                                          "Texto",
                                              "Lexema: Espacio Vacio"])
                Variables.contadorbitacora += 1

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarcss += 1
                Variables.indexcaractercss += 1

                # Verificar Cadena Completa
                VerificarComillasCSS()

            # Verificar Tabulaciones
            elif re.search(r"[\t]", Variables.cadenaarchivo[Variables.indexcaractercss]):

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 30 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 30: Tabulaciones Cadenas De "
                                                                          "Texto",
                                              "Lexema: \\t"])
                Variables.contadorbitacora += 1

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarcss += 1
                Variables.indexcaractercss += 1

                # Verificar Cadena Completa
                VerificarComillasCSS()

            # Verificar Salto De Linea
            elif re.search(r"[\n]", Variables.cadenaarchivo[Variables.indexcaractercss]):

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 31 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 31: Salto De Linea Cadenas De "
                                                                          "Texto",
                                              "Lexema: \\n"])
                Variables.contadorbitacora += 1

                # Sumar Fila E Indice Del Array, Reiniciar Columna
                Variables.columnaauxiliarcss = 1
                Variables.filaauxiliarcss += 1
                Variables.indexcaractercss += 1

                # Verificar Cadena Completa
                VerificarComillasCSS()

            # Verificar Otro Tipo De Caracter
            else:

                # Agegar Caracter A Auxiliar Lexico
                Variables.auxiliarlexicocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Archivo Sin Errores
                Variables.archivocss += Variables.cadenaarchivo[Variables.indexcaractercss]

                # Agregar Estado 32 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 32: Letras, Simbols Y Digitos"
                                                                          " Cadenas De Texto",
                                              "Lexema: \\t"])
                Variables.contadorbitacora += 1

                # Sumar Columna E Indice Del Array
                Variables.columnaauxiliarcss += 1
                Variables.indexcaractercss += 1

                # Existe Caracter
                Variables.existecaracter = True

                # Verificar Cadena Completa
                VerificarComillasCSS()

        # Aceptar Cadena Como Valida
        else:

            # Ubicar La Columna Del Final De La Cadena
            Variables.columnaauxiliarcss -= 1

            # Verificar Si Existe Caracter
            if Variables.existecaracter:
                # Agregar Token A La Lista
                Variables.listatokenscss.append(
                    [Variables.contadortokenscss, "Texto", Variables.auxiliarlexicocss,
                     Variables.columnaauxiliarcss,
                     Variables.filaauxiliarcss])

                # Agregar Estado 33 A Bitacora
                Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 33: Aceptacion Cadenas De Texto",
                                              "Token Aceptado: " + Variables.auxiliarlexicocss])
                Variables.contadorbitacora += 1

            # Sumar Columna Y Contador Tokens
            Variables.columnaauxiliarcss += 1
            Variables.contadortokenscss += 1

            # Vaciar Auxiliar Lexico
            Variables.auxiliarlexicocss = ""

    # Aceptar Cadena Como Valida
    else:

        # Ubicar La Columna Del Final De La Cadena
        Variables.columnaauxiliarcss -= 1

        # Verificar Si Existe Caracter
        if Variables.existecaracter:
            # Agregar Token A La Lista
            Variables.listatokenscss.append(
                [Variables.contadortokenscss, "Texto", Variables.auxiliarlexicocss,
                 Variables.columnaauxiliarcss,
                 Variables.filaauxiliarcss])

            # Agregar Estado 33 A Bitacora
            Variables.bitacoracss.append([Variables.contadorbitacora, "Estado 33: Aceptacion Cadenas De Texto",
                                          "Token Aceptado: " + Variables.auxiliarlexicocss])
            Variables.contadorbitacora += 1
