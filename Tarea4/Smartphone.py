class Smartphone:
    def __init__(self,marca,capacidad):
        self.marca=marca
        self.capacidad=capacidad
    def toString(self):
        cadena="|Marca: "+self.marca+", Capacidad: "+str(self.capacidad)+"GB|"
        return cadena
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
    def getCapacidad(self):
        return self.capacidad()
    def setCapacidad(self,capacidad):
        self.capacidad=capacidad