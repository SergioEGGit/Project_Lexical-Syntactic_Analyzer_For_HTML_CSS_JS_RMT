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
tokenanterior = ""
dicpalabrasreservadashtml = ["html", "head", "title"]
dicsignoshtml = {"MayorQue": ">", "MenorQue": "<"}
listatokenshtml = []
listaerroreshtml = []
