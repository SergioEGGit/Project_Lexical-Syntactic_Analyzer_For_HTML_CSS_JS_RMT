# ---------------------------------------------------Clase Pila---------------------------------------------------------
class PilaParentesisEstructura(object):

    # Crear Pila
    def __init__(self):

        self.Parentesis = []

    # Revisar Si La Pila Esta Vacia
    def PilaVacia(self):

        return self.Parentesis == []

    # Ingresar Caracter A La Pila
    def PilaPush(self, caracter):

        self.Parentesis.append(caracter)

    # Extraer Caracter De La Pila
    def PilaPop(self):

        return self.Parentesis.pop()

    def PilaPrimerElemento(self):

        return self.Parentesis[len(self.Parentesis) - 1]

    def PilaSize(self):

        return len(self.Parentesis)
