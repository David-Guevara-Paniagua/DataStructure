class ConjuntoADT:
    listaConjunto=[]
    def __init__(self, tamanio):
        self.tamanio=tamanio
    def getLongitud(self):
        return self.tamanio
    def contiene(self,elemento):
        flag = False
        for item in self.listaConjunto:
            if item==elemento:
                flag=True
        return flag
    def agregar(self,elemento):
        if elemento not in self.listaConjunto:
            self.listaConjunto.append(elemento)
    def eliminar(self,elemento):
        if elemento in self.listaConjunto:
            self.listaConjunto.remove(elemento)
    def equals(self,otroConjunto):
        if self.listaConjunto == otroConjunto.listaConjunto:
            return True
        else:
            return False
    def esSubConjunto(self,otroConjunto):
        flag = True
        for item in self.listaConjunto:
            if item not in otroConjunto.listaConjunto:
                flag=False
        return flag
    def union(self,otroConjunto):
        nuevoConjunto=[]
        for item in self.listaConjunto:
            nuevoConjunto.append(item)
        for item in otroConjunto.listaConjunto:
            if item not in nuevoConjunto:
                nuevoConjunto.append(item)
        return nuevoConjunto
    def interseccion(self,otroConjunto):
        nuevoConjunto=[]
        for item in self.listaConjunto:
            if item in otroConjunto.listaConjunto:
                nuevoConjunto.append(item)
        return nuevoConjunto
    def diferencia(self, otroConjunto):
        nuevoConjunto=[]
        for item in self.listaConjunto:
            if item not in otroConjunto.listaConjunto:
                nuevoConjunto.append(item)
        return nuevoConjunto
    def imprimir(self):
        for item in self.listaConjunto:
            print(item,end=", ")
        print()
    def limpiar(self):
        self.listaConjunto=[]
        
#Crear conjuntoA y agregar 5 elementos (1-5)
miConjuntoA=ConjuntoADT(5)
for i in range(5):
    miConjuntoA.agregar(i+1)
print("ConjuntoA:")
miConjuntoA.imprimir()
print("tamanio:",miConjuntoA.getLongitud())

#Comprobar si contiene a 5 y a 22
print()
print("Contiene a 5?")
print(miConjuntoA.contiene(5))
print("Contiene 22?")
print(miConjuntoA.contiene(22))

#Eliminando el elemento '5'
print()
print("Eliminando '5' del conjunto A:")
print("ConjuntoA:")
miConjuntoA.eliminar(5)
miConjuntoA.imprimir()

#Creando el conjunto B y agregando 4 elementos (0-3)
print()
print("ConjuntoB:")
miConjuntoB=ConjuntoADT(4)
miConjuntoB.limpiar()
for i in range(4):
    miConjuntoB.agregar(i)
miConjuntoB.imprimir()

#Comprobar si el conjunto A es subconjunto del conjunto B
print()
print("A es subconjunto de B?:",miConjuntoA.esSubConjunto(miConjuntoB))

#Agregando 4 al conjunto B:
print()
print("Agregando '4' al conjunto B:")
miConjuntoB.agregar(4)
print("ConjuntoB:")
miConjuntoB.imprimir()

#Mostrando conjunto A:
print("ConjuntoA:")
miConjuntoA.imprimir()

#Comprobar si el conjunto A es subconjunto del conjunto B
print()
print("A es subconjunto de B?:",miConjuntoA.esSubConjunto(miConjuntoB))

#Comprobar si el conjunto A es igual al conjunto B
print()
print("ConjuntoA es igual al conjuntoB?",miConjuntoA.equals(miConjuntoB))

#Restablecer el conjunto B con 4 elementos (1-4)
miConjuntoB.limpiar()
for i in range(4):
    miConjuntoB.agregar(i+1)
print()
print("Restablecer el conjunto B con 4 elementos (1-4)")
print("ConjuntoB:")
miConjuntoB.imprimir()

#Comprobar si el conjunto A es igual al conjunto B
print("ConjuntoA es igual a conjuntoB?:",miConjuntoA.equals(miConjuntoB))

#Agregando '5' al conjunto B
print()
print("Agregando '5' al conjunto B")
miConjuntoB.agregar(5)

#Agregando '0' al conjunto A
print()
print("Agregando '0' al conjunto A")
miConjuntoA.agregar(0)

#Realizando las operaciones de union, interseccion y 
# diferencia entre los conjutos A y B
print()
print("ConjuntoA:")
miConjuntoA.imprimir()
print("ConjuntoB:")
miConjuntoB.imprimir()

print("Union:",miConjuntoA.union(miConjuntoB))
print("Interseccion:",miConjuntoA.interseccion(miConjuntoB))
print("Diferencia (A-B):",miConjuntoA.diferencia(miConjuntoB))