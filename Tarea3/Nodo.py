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

#Creando función para mostrar estructura de nodos con un while
def mostrarEstructura(head):
    aux=head
    while(aux!=None):
        print(aux.getValor(),end=" | ")
        aux=aux.getSiguiente()
    print()

#Creando la estructura de nodos
head=Nodo(100,Nodo(200,Nodo(300,Nodo(400,Nodo(600,None)))))
#Imprimiendo la estructura con un while
mostrarEstructura(head)
#Cambiando el valor del 3er nodo a 333
head.getSiguiente().getSiguiente().setValor(333)
#Mostrando la estructura
mostrarEstructura(head)
#Anadiendo un nodo 700 al final
head.getSiguiente().getSiguiente().getSiguiente().getSiguiente().setSiguiente(Nodo(700,None))
#Mostrando la estructura
mostrarEstructura(head)
#Insertando un nodo 50 al inicio
head=Nodo(50,head)
#Mostrando la estructura
mostrarEstructura(head)