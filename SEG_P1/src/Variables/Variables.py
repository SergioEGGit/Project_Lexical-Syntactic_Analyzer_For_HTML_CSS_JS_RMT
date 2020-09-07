# --------------------------------------------------Variables-----------------------------------------------------------

# Ruta Archivo Abierto Recientemente
rutaarchivo = ""

# Extension Archivo
extensionarchivo = ""

# Cadena Archivo
cadenaarchivo = ""

# Vericar Si Hay Un Caracter
existecaracter = False

# Verificar Numero De Comillas
numerocomillas = 0

# Comillas Final
comillasfinales = False

# Nombre De Archivo
nombrearchivo = ""

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
                             "colgroup", "col", "thead", "tbody", "tfoot"]
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
dicpalabrasreservadasjs = ["var"]
listatokensjs = []
listaerroresjs = []
