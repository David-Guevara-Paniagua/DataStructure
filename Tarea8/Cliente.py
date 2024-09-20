class Cliente:
    def __init__(self,nombre,prioridad):
        self.nombre=nombre
        self.prioridad=prioridad
    def getNombre(self):
        return self.nombre
    def getPrioridad(self):
        return self.prioridad
    def retiro(self,cantidad):
        print("Se retiro,",cantidad, "de la cuenta de",self.nombre)
    def __str__(self):
        return str(self.nombre)+": "+str(self.prioridad)