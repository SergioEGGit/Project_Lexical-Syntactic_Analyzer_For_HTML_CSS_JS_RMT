# --------------------------------------------------Variables-----------------------------------------------------------

# Ruta Archivo Abierto Recientemente
rutaarchivo = ""

# Extension Archivo
extensionarchivo = ""

# Cadena Archivo
cadenaarchivo = ""

# Cadena Archivo Lineas
lineasarchivo = []

# Vericar Si Hay Un Caracter
existecaracter = False

# Verificar Numero De Comillas
numerocomillas = 0

# Comillas Final
comillasfinales = False

# Nombre De Archivo
nombrearchivo = ""

# Arreglo Split

# Analizador HTML
columnaauxiliarhtml = 0
filaauxiliarhtml = 0
indexcaracterhtml = 0
contadortokenshtml = 0
contadorerroreshtml = 0
auxiliarlexicohtml = ""
archivohtml = ""
dicpalabrasreservadashtml = ["html", "head", "title", "body", "h1", "h2", "h3", "h4", "h5", "h6", "p", "br", "img",
                             "src", "a", "href", "ul", "li", "style", "table", "border", "th", "tr", "td", "caption",
                             "colgroup", "col", "thead", "tbody", "tfoot", "div", "class"]
listatokenshtml = []
listaerroreshtml = []

# Analizador CSS
columnaauxiliarcss = 0
filaauxiliarcss = 0
indexcaractercss = 0
contadortokenscss = 0
contadorerrorescss = 0
contadorbitacora = 0
auxiliarlexicocss = ""
archivocss = ""
numeral = False
dicpalabrasreservadascss = ["color", "background-color", "background-image", "border", "opacity", "background",
                            "text-align", "font-family", "font-style", "font-weight", "font-size",
                            "font", "padding-left", "padding-right", "padding-bottom",
                            "padding-top", "padding", "display", "line-height", "width", "height",
                            "margin-top", "margin-right", "margin-bottom", "margin-left", "margin", "border-style",
                            "display", "position", "bottom", "top", "right", "left", "float", "clear", "max-width",
                            "min-width", "max-height", "min-height", "px", "em", "vh", "vw", "in", "cm", "mm", "pt",
                            "pc", "relative", "inline-block", "rgba"]
listatokenscss = []
listaerrorescss = []
bitacoracss = []

# Analizador Js
columnaauxiliarjs = 0
filaauxiliarjs = 0
indexcaracterjs = 0
contadortokensjs = 0
contadorerroresjs = 0
auxiliarlexicojs = ""
archivojs = ""
dicpalabrasreservadasjs = ["var", "false", "true", "console", "log", "if", "else", "for", "while", "do", "continue",
                           "break", "return", "function", "constructor", "this", "class", "Math", "pow", "window",
                           "location", "document", "push", "pop", "append", "null", "new", "parseInt", "parse",
                           "forEach", "appendChild"]
listatokensjs = []
listaerroresjs = []
# Verificar Reporte JS
existenumero = False
existeidentificador = False
existesimbolo = False
existecadenadetextodobles = False
existecadenadetextosimple = False
existecomentariounilinea = False
existecomentariomultilinea = False

# Analizador RMT
columnaauxiliarrmt = 0
filaauxiliarrmt = 0
indexcaracterrmt = 0
contadortokensrmt = 0
contadorerroresrmt = 0
auxiliarlexicormt = ""
archivormt = ""
listatokensrmt = []
listaerroresrmt = []
listaerroreslexicosrmt = []
listaanalisissintacticormt = []
