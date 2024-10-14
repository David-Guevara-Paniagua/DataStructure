class NodoArbol:
    def __init__(self,valor,hijoIzq,hijoDer):
        self.valor=valor
        self.hijoIzq=hijoIzq
        self.hijoDer=hijoDer
    def getHijoIzq(self):
        return self.hijoIzq
    def getHijoDer(self):
        return self.hijoDer
    def getValor(self):
        return self.valor
    def setHijoIzq(self,NodoArbol):
        self.hijoIzq=NodoArbol
    def setHijoDer(self,NodoArbol):
        self.hijoDer=NodoArbol
    def setValor(self,valor):
        self.valor=valor
    def __str__(self):
        cadena=str(self.valor)+": ["
        cadena+="H_Izq: "+str(self.getHijoIzq())+", "
        cadena+="H_Der: "+str(self.getHijoDer())
        cadena+="]"
        return cadena
        

        