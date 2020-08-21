# ----------------------------------------------Imports-----------------------------------------------------------------
from src.Design import Objetos
from src.Design import Configuracion
from src.Variables import Variables

# -----------------------------------------------Metodos----------------------------------------------------------------

# Variarbles

# Configuración Ventana Principal
Configuracion.VentanaPrincipal()
Configuracion.MenuArchivo()
Configuracion.RichText()
Configuracion.Titulo()

# Ciclo Ventana
Objetos.ventanaprincipal.mainloop(0)
