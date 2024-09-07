class NodoDoble:
    def __init__(self,valor,siguiente,previo):
        self.valor=valor
        self.siguiente=siguiente
        self.previo=previo
    def getSiguiente(self):
        return self.siguiente
    def setSiguiente(self,siguienteNodo):
        self.siguiente=siguienteNodo
    def getPrevio(self):
        return self.previo
    def setPrevio(self, nodoPrevio):
        self.previo=nodoPrevio
    def getValor(self):
        return self.valor
    def setValor(self,valor):
        self.valor=valor

