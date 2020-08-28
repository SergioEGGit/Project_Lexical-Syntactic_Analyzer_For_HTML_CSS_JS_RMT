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

# Analizador HTML
columnaauxiliarhtml = 0
filaauxiliarhtml = 0
indexcaracterhtml = 0
contadortokens = 0
contadorerrores = 0
auxiliarlexicohtml = ""
dicpalabrasreservadashtml = ["html", "head", "title", "body", "h1", "h2", "h3", "h4", "h5", "h6", "p", "br", "img",
                             "src", "a", "href", "ul", "li", "style", "table", "border", "th", "tr", "td", "caption",
                             "colgroup", "col", "thead", "tbody", "tfoot"]
listatokenshtml = []
listaerroreshtml = []
