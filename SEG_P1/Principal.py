# ----------------------------------------------Imports-----------------------------------------------------------------
from src.Design import Objetos
from src.Design import Configuracion

# -----------------------------------------------Metodos----------------------------------------------------------------

# Variarbles

# Configuración Ventana Principal
Configuracion.VentanaPrincipal()
Configuracion.Menu()
Configuracion.RichTextArchivo()
Configuracion.RichTextConsola()
Configuracion.TituloPrincipal()
Configuracion.TituloArchivo()
Configuracion.TituloConsola()

# Ciclo Ventana
Objetos.ventanaprincipal.mainloop(0)
