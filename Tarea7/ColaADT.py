class ColaADT:
    def __init__(self):
        self.data=[]
    
    def estaVacia(self):
        flag = False
        if len(self.data)==0:
            flag = True
        return flag
    
    def longitud(self):
        return len(self.data)
    
    def frente(self):
        return self.data[0]
    
    def encolar(self,valor):
        self.data.append(valor)
    
    def desencolar(self):
        if not self.estaVacia():
            return self.data.pop(0)
        else:
            print("Error al desencolar: La cola esta vacia!!")
    
    def toString(self):
        cadena="["
        for i in self.data:
            cadena+=i.toString()+", "
        cadena+="]"
        return cadena
