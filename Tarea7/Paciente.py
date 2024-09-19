class Paciente:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def toString(self):
        cadena=self.nombre+": "+str(self.edad)
        return cadena