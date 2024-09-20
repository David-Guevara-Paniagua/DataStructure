class ColaConPrioridad:
    def __init__(self, maxPrioridad):
        self.maxPrioridad=maxPrioridad
        self.colas=[]
        for i in range(self.maxPrioridad+1):
            self.colas.append([])
    def longitud(self):
        tamanio=0
        for i in range(self.maxPrioridad+1):
            tamanio+=len(self.colas[i])
        return tamanio
    def estaVacia(self):
        flag = False
        if self.longitud()==0:
            flag=True
        return flag
    def encolar(self, prioridad, elemento):
        if prioridad>0 and prioridad<=self.maxPrioridad:
            self.colas[prioridad].append(elemento)
        else:
            print("Prioridad fuera de rango!!")
    def desencolar(self):
        if not self.estaVacia():
            for i in range(self.maxPrioridad+1):
                colaVacia= len(self.colas[i])==0
                if not colaVacia:
                    return self.colas[i].pop(0)
        else:
            print("La cola de prioridad esta vacia!!")
    def toString(self):
        cadena="[\n"
        for cola in self.colas:
            cadena+="["
            for item in cola:
                cadena+=str(item)+", "
            cadena+="]\n"
        cadena+="]"
        return cadena