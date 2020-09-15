# ---------------------------------------------------Imports------------------------------------------------------------
import subprocess

from pathlib import Path
from tkinter.messagebox import showinfo, askyesno

from src.Variables import Variables

# ----------------------------------------------------Métodos-----------------------------------------------------------


# Automata Numeros JS
def AutomataNumerosJS():

    # Variables
    cadenatextojs = "    subgraph Automata_Numeros { \n\n" \
                    "        graph[fontsize = \"36\"] \n" \
                    "        node[shape = note, color = navy] \n" \
                    "        Titulo_Numeros [label = \" Automata_Numeros \", fontsize = \"20\"] \n" \
                    "        node[shape = doublecircle, color = deepskyblue, fontsize = \"14\"] " \
                    "Estado_N_1 Estado_N_3; \n" \
                    "        node[shape = circle, color = deepskyblue, fontsize = \"14\"] \n" \
                    "        Titulo_Numeros -> Estado_N_0 \n" \
                    "        Estado_N_0 -> Estado_N_1 [label = \" Digito \", fontsize = \"15\"] \n" \
                    "        Estado_N_1 -> Estado_N_1 [label = \" Digito \", fontsize = \"15\"] \n" \
                    "        Estado_N_1 -> Estado_N_2 [label = \" . \", fontsize = \"50\"] \n" \
                    "        Estado_N_2 -> Estado_N_3 [label = \" Digito \", fontsize = \"15\"] \n" \
                    "        Estado_N_3 -> Estado_N_3 [label = \" Digito \", fontsize = \"15\"] \n\n" \
                    "    } \n\n\n"

    return cadenatextojs


# Automata Identificadores JS
def AutomataIdentificadoresJS():

    # Variables
    cadenatextojs = "    subgraph Automata_Identificadores { \n\n" \
                    "        graph[fontsize = \"36\"] \n" \
                    "        node[shape = note, color = darkgreen] \n" \
                    "        Titulo_Identificadores [label = \" Automata_Identificadores \", fontsize = \"20\"] \n" \
                    "        node[shape = doublecircle, color = springgreen, fontsize = \"14\"] Estado_I_1; \n" \
                    "        node[shape = circle, color = springgreen, fontsize = \"14\"] \n" \
                    "        Titulo_Identificadores -> Estado_I_0 \n" \
                    "        Estado_I_0 -> Estado_I_1 [label = \" Letra \", fontsize = \"15\"] \n" \
                    "        Estado_I_1 -> Estado_I_1 [label = \" Letra | Digito | _ \", fontsize = \"15\"] \n\n" \
                    "    } \n\n\n"

    return cadenatextojs


# Automata Simbolos JS
def AutomataSimbolosJS():

    # Variables
    cadenatextojs = "   subgraph Automata_Simbolos { \n\n" \
                    "       graph[fontsize = \"36\"] \n" \
                    "       node[shape = note, color = goldenrod] \n" \
                    "       Titulo_Simbolos [label = \" Automata_Simbolos \", fontsize = \"20\"] \n" \
                    "       node[shape = doublecircle, color = gold, fontsize = \"14\"] Estado_S_1; \n" \
                    "       node[shape = circle, color = gold, fontsize = \"14\"] \n" \
                    "       Titulo_Simbolos -> Estado_S_0 \n" \
                    "       Estado_S_0 -> Estado_S_1 [label = \" Simbolo \", fontsize = \"15\"] \n\n" \
                    "   } \n\n\n"

    return cadenatextojs


# Automata Cadenas De Texto Dobles JS
def AutomataCadenasDeTextoDoblesJS():

    # Variables
    cadenatextojs = "   subgraph Automata_Cadenas_De_Texto_D { \n\n" \
                    "       graph[fontsize = \"36\"] \n" \
                    "       node[shape = note, color = coral4] \n" \
                    "       Titulo_Cadenas_De_Texto_D [label = \" Automata_Cadenas_De_Texto_D \", " \
                    "fontsize = \"20\"] \n" \
                    "       node[shape = doublecircle, color = coral1, fontsize = \"14\"] Estado_Cad_2; \n" \
                    "       node[shape = circle, color = coral1, fontsize = \"14\"] \n" \
                    "       Titulo_Cadenas_De_Texto_D -> Estado_Cad_0 \n" \
                    "       Estado_Cad_0 -> Estado_Cad_1 [label = \" \\\" \", fontsize = \"30\"] \n" \
                    "       Estado_Cad_1 -> Estado_Cad_1 [label = \" Todo \", fontsize = \"15\"] \n" \
                    "       Estado_Cad_1 -> Estado_Cad_2 [label = \" \\\" \", fontsize = \"30\"] \n\n" \
                    "   } \n\n\n"

    return cadenatextojs


# Automata Cadenas De Texto Simples JS
def AutomataCadenasDeTextoSimplesJS():

    # Variables
    cadenatextojs = "   subgraph Automata_Cadenas_De_Texto_S { \n\n" \
                    "       graph[fontsize = \"36\"] \n" \
                    "       node[shape = note, color = purple4] \n" \
                    "       Titulo_Cadenas_De_Texto_S [label = \" Automata_Cadenas_De_Texto_S \", fontsize = \"20\"] \n" \
                    "       node[shape = doublecircle, color = lightslateblue, fontsize = \"14\"] Estado_Cas_2; \n" \
                    "       node[shape = circle, color = lightslateblue, fontsize = \"14\"] \n" \
                    "       Titulo_Cadenas_De_Texto_S -> Estado_Cas_0 \n" \
                    "       Estado_Cas_0 -> Estado_Cas_1 [label = \" ' \", fontsize = \"30\"] \n" \
                    "       Estado_Cas_1 -> Estado_Cas_1 [label = \" Todo \", fontsize = \"15\"] \n" \
                    "       Estado_Cas_1 -> Estado_Cas_2 [label = \" ' \", fontsize = \"30\"] \n\n" \
                    "   } \n\n\n"

    return cadenatextojs


# Automata Comentario Unilinea JS
def AutomataComentarioUnilineaJS():

    # Variables
    cadenatextojs = "   subgraph Automata_Comentario_Unilinea { \n\n" \
                    "       graph[fontsize = \"36\"] \n" \
                    "       node[shape = note, color = crimson] \n" \
                    "       Titulo_Comentario_Unilinea [label = \" Automata_Comentario_Unilinea \", " \
                    "fontsize = \"20\"] \n" \
                    "       node[shape = doublecircle, color = firebrick1, fontsize = \"14\"] Estado_Cou_3; \n" \
                    "       node[shape = circle, color = firebrick1, fontsize = \"14\"] \n" \
                    "       Titulo_Comentario_Unilinea -> Estado_Cou_0 \n" \
                    "       Estado_Cou_0 -> Estado_Cou_1 [label = \" / \", fontsize = \"30\"] \n" \
                    "       Estado_Cou_1 -> Estado_Cou_2 [label = \" / \", fontsize = \"30\"] \n" \
                    "       Estado_Cou_2 -> Estado_Cou_2 [label = \" Todo \", fontsize = \"15\"] \n" \
                    "       Estado_Cou_2 -> Estado_Cou_3 [label = \" Salto_De_Linea \", fontsize = \"15\"] \n\n" \
                    "   } \n\n\n"

    return cadenatextojs


# Automata Comentario Multilinea JS
def AutomataComentarioMultilineaJS():

    # Variables
    cadenatextojs = "   subgraph Automata_Comentario_Multilinea { \n\n" \
                    "       graph[fontsize = \"36\"] \n" \
                    "       node[shape = note, color = orangered3] \n" \
                    "       Titulo_Comentario_Multilinea [label = \" Automata_Comentario_Multilinea \", " \
                    "fontsize = \"20\"] \n" \
                    "       node[shape = doublecircle, color = orangered, fontsize = \"14\"] Estado_Com_4; \n" \
                    "       node[shape = circle, color = orangered, fontsize = \"14\"] \n" \
                    "       Titulo_Comentario_Multilinea -> Estado_Com_0 \n" \
                    "       Estado_Com_0 -> Estado_Com_1 [label = \" / \", fontsize = \"30\"] \n" \
                    "       Estado_Com_1 -> Estado_Com_2 [label = \" * \", fontsize = \"30\"] \n" \
                    "       Estado_Com_2 -> Estado_Com_2 [label = \" Todo \", fontsize = \"15\"] \n" \
                    "       Estado_Com_2 -> Estado_Com_3 [label = \" * \", fontsize = \"30\"] \n" \
                    "       Estado_Com_3 -> Estado_Com_4 [label = \" / \", fontsize = \"30\"] \n\n" \
                    "   } \n\n\n"

    return cadenatextojs


# Generar Archivo Txt
def GenerarArchivoTXTJS(cadenatextojs, archivotxt):

    # Crear Archivo Txt Graphviz

    with open(archivotxt, 'w') as archivonuevo:

        archivonuevo.write(cadenatextojs)


# Generar Imagen Graphviz
def GenerarImagenGraphvizJS(cadenareporte):

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

        # Generar Archivo De Texto
        GenerarArchivoTXTJS(cadenareporte, rutaarchivo + "Automata_Partes.txt")

        # Crear Archivo
        comandographviz = "dot -Tpng -o " + rutaarchivo + "Automata_Partes.png " + rutaarchivo \
                          + "Automata_Partes.txt"
        subprocess.run(comandographviz, shell=True)

        # Path Salida
        pathsalida = rutaarchivo + "Automata_Partes.png"

    else:

        # Convertir String A Ruta
        patharchivo = Path(rutastring)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        # Generar Archivo De Texto
        GenerarArchivoTXTJS(cadenareporte, rutastring + "\\Automata_Partes.txt")

        # Crear Archivo
        comandographviz = "dot -Tpng -o " + rutastring + "\\Automata_Partes.png " + rutastring \
                          + "\\Automata_Partes.txt"
        subprocess.run(comandographviz, shell=True)

        # Path Salida
        pathsalida = rutastring + "\\Automata_Partes.png"

        showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Reporte \n"
                           "Se Guardara En La Siguiente Ruta: \n"
                           "C:\\Reportes\\js")

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Reporte Automatat JS!", "¿Desea Abrir El Reporte La Imagen Del Automata?")

    # Abrir Archivo
    if resultado:

        # Abrir Imagen
        abririmagen = pathsalida + " &"
        subprocess.run(abririmagen, shell=True)


# Generar Reporte
def GenerarGraficaReporte():

    # Verificar Extension
    if Variables.extensionarchivo == "js":

        # Variables
        cadenareporte = ""

        # Asignación
        cadenareporte += "digraph Automata_Por_Partes { \n\n" \
                         "    rankdir = LR; \n\n"

        if Variables.existenumero:
            cadenareporte += AutomataNumerosJS()

        if Variables.existeidentificador:
            cadenareporte += AutomataIdentificadoresJS()

        if Variables.existesimbolo:
            cadenareporte += AutomataSimbolosJS()

        if Variables.existecadenadetextosimple:
            cadenareporte += AutomataCadenasDeTextoSimplesJS()

        if Variables.existecadenadetextodobles:
            cadenareporte += AutomataCadenasDeTextoDoblesJS()

        if Variables.existecomentariounilinea:
            cadenareporte += AutomataComentarioUnilineaJS()

        if Variables.existecomentariomultilinea:
            cadenareporte += AutomataComentarioMultilineaJS()

        cadenareporte += "} \n"

        # Generar Imagen
        GenerarImagenGraphvizJS(cadenareporte)

    else:

        showinfo("Error!", "Aún No Se Ha Realizado Un Análsis De JS")
