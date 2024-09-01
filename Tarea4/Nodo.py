class Nodo:
    siguiente=None
    def __init__(self, valor, siguiente):
        self.valor=valor
        self.siguiente=siguiente
    def getValor(self):
        return self.valor
    def setValor(self,valor):
        self.valor=valor
    def getSiguiente(self):
        return self.siguiente
    def setSiguiente(self,siguienteNodo):
        self.siguiente=siguienteNodo
