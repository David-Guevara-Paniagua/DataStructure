from NodoDoble import *
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.tamanio=0
    def esta_vacia(self):
        vacia=False
        if self.head==None:
            vacia=True
        return vacia
    def get_tamanio(self):
        return self.tamanio
    def agregar_al_inicio(self,valor):
        self.tamanio+=1
        if self.esta_vacia():
            self.head=NodoDoble(valor,None,None)
            self.tail=self.head
        else:
            self.head=NodoDoble(valor,self.head,None)
            self.head.getSiguiente().setPrevio(self.head)
    def agregar_al_final(self,valor):
        self.tamanio+=1
        if self.esta_vacia():
            self.tail=NodoDoble(valor,None,None)
            self.head=self.tail
        else:
            self.tail=NodoDoble(valor,None,self.tail)
            self.tail.getPrevio().setSiguiente(self.tail)

    def transversal(self,direccion):# 2:de der a izq // otro valor:de izq a der
        if direccion==2:
            aux=self.tail
            while aux!=None:
                print("|",aux.getValor(),end=" | <-> ")
                aux=aux.getPrevio()
            print("None")
        else:
            aux=self.head
            while aux!=None:
                print("|",aux.getValor(),end=" | <-> ")
                aux=aux.getSiguiente()
            print("None")
    def agregar_despues_de(self,referencia,valor):
        aux=self.head
        while aux != None and aux.getValor() != referencia:
            aux=aux.getSiguiente()
        if aux==None:
            print("No existe el valor",referencia)
        else:
            if aux==self.tail:
                self.agregar_al_final(valor)
            else:
                self.tamanio+=1
                nuevoNodo=NodoDoble(valor,aux.getSiguiente(),aux)
                aux.setSiguiente(nuevoNodo)
                nuevoNodo.getSiguiente().setPrevio(nuevoNodo)
    def obtener(self,posicion):
        if posicion>=self.tamanio or posicion<0:
            print("Indice fuera de rango")
            aux=None
        else:
            aux=self.head
            for i in range(posicion-1):
                aux=aux.getSiguiente()
        return aux
    def eliminar_el_primero(self):
        self.tamanio-=1
        self.head=self.head.getSiguiente()
        self.head.setPrevio(None)
    def eliminar_el_final(self):
        self.tamanio-=1
        self.tail=self.tail.getPrevio()
        self.tail.setSiguiente(None)
    def eliminar(self,posicion):
        if posicion>=self.tamanio or posicion<0:
            print("Indice fuera de rango")
        else:
            self.tamanio-=1
            aux=self.head
            for i in range(posicion):
                aux=aux.getSiguiente()
            aux.getPrevio().setSiguiente(aux.getSiguiente())
            aux.getSiguiente().setPrevio(aux.getPrevio())
    def buscar(self,valor):
        aux=self.head
        currentPos=0
        while aux!=None and aux.getValor()!=valor:
            aux=aux.getSiguiente()
            currentPos+=1
        if aux==None:
            print("No existe el valor",valor)
            currentPos=None
        return currentPos
    def actualizar(self,a_buscar, valor):
        posicion=self.buscar(a_buscar)
        if posicion!=None:
            aux=self.head
            for i in range(posicion):
                aux=aux.getSiguiente()
            aux.setValor(valor)

