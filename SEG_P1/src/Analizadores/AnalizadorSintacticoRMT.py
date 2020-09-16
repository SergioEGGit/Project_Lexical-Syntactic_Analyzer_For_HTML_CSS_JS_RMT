# ---------------------------------------------------Imports------------------------------------------------------------
from src.EstructurasDeDatos.PilaParentesisEstructura import PilaParentesisEstructura
from src.Variables import Variables


# ----------------------------------------------------Métodos-----------------------------------------------------------


# Verificar Balanceo De Parentesis
def VerificacarBalanceParentesis(operacionaritemetica):
    # Variables
    indicepila = 0
    caracteractual = ""
    cadenadeparentesis = ""
    bandera = False
    parentesisbalanceados = True

    # Creacion Nueva Pila
    PilaParentesis = PilaParentesisEstructura()

    # Asignación
    cadenadeparentesis = operacionaritemetica

    # Recorrer Cadena De Parentesis Y Esta Balanceado
    while indicepila < len(cadenadeparentesis) and parentesisbalanceados:

        # Obtener El Caracter A Analizar
        caracteractual = cadenadeparentesis[indicepila]

        # Verificar Si Hay Parentesis De Apertura
        if caracteractual == "(":

            # Agregar Parentesis A Pila
            PilaParentesis.PilaPush(caracteractual)

        elif caracteractual == ")":

            # Revisra Si La Pila Esta Vacia
            if PilaParentesis.PilaVacia():

                # Parentesis Desbalanceados
                parentesisbalanceados = False

            else:

                # Extraer Parentesis
                PilaParentesis.PilaPop()

        # Aumentar Indice Cadena
        indicepila += 1

    # Verificar Si Esta Correcto O No
    if parentesisbalanceados and PilaParentesis.PilaVacia():

        bandera = True

    else:

        bandera = False

    # Retornar Opcion
    return bandera


# Analizador Sintactico Y Balanceo De Parentesis
def AnalizadorSintacticoRMT():

    # Variables
    operacioncorrecta = False
    filaarchivo = 1
    contadorcorrelativo = 1
    informacionerrores = ""

    # Asignacion
    Variables.listaanalisissintacticormt[:] = []

    # Recorrer Lineas
    for OperacionesAritmeticas in Variables.lineasarchivo:

        # Limpiar Informacion
        informacionerrores = ""

        # Analizar Linea
        operacioncorrecta = VerificacarBalanceParentesis(OperacionesAritmeticas)

        # Verificar Resultado
        if operacioncorrecta:

            informacionerrores += "Correcto"

        else:

            informacionerrores += "Incorrecto"

        # Verificar Si Hay Errores Lexicos
        for Fila in Variables.listaerroreslexicosrmt:

            if Fila == filaarchivo:
                informacionerrores += ", Esta Linea Posee Errores Lexicos"

        # Agregar Arreglo Reporte
        Variables.listaanalisissintacticormt.append([contadorcorrelativo, filaarchivo,
                                                     OperacionesAritmeticas.strip(), informacionerrores])

        # Incrementar fila
        contadorcorrelativo += 1
        filaarchivo += 1
