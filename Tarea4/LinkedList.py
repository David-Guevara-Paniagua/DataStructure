from Nodo import *

class LinkedList:
    def __init__(self):
        self.head=None
        self.tamanio=0
    def esta_vacia(self):
        flag=False
        if self.tamanio==0:
            flag = True
        return flag
    def get_tamanio(self):
        return self.tamanio
    def agregar_al_final(self,dato):
        if self.esta_vacia():
            self.head=Nodo(dato,None)
        else:
            aux=self.head
            while aux.getSiguiente()!=None:
                aux=aux.getSiguiente()
            aux.setSiguiente(Nodo(dato,None))
        self.tamanio+=1
    def agregar_al_inicio(self,dato):
        if self.esta_vacia():
            self.head=Nodo(dato,None)
        else:
            self.head=Nodo(dato,self.head)
        self.tamanio+=1
    def agregar_despues_de(self,referencia,dato):
        posicionDeReferencia=self.buscar(referencia)
        if posicionDeReferencia != None:
            aux=self.head
            for i in range(posicionDeReferencia):
                aux=aux.getSiguiente()
            aux.setSiguiente(Nodo(dato,aux.getSiguiente()))
            self.tamanio+=1
    def eliminar(self,posicion):
        if posicion < self.get_tamanio() and posicion >= 0:
            if posicion==0:
                self.head=self.head.getSiguiente()
            else:
                aux=self.head
                for i in range(posicion-1):
                    aux=aux.getSiguiente()
                aux.setSiguiente(aux.getSiguiente().getSiguiente())
            self.tamanio-=1
        else:
            print("Posicion fuera del rango!")
    def eliminar_el_primero(self):
        self.head=self.head.getSiguiente()
        self.tamanio-=1
    def eliminar_el_final(self):
        aux=self.head
        for i in range(self.tamanio-2):#se descuenta el head y el ultimo para llegar al penultimo
            aux=aux.getSiguiente()
        aux.setSiguiente(None)
        self.tamanio-=1

    def buscar(self,dato):
        aux=self.head
        currentPos=0
        while aux!=None and aux.getValor()!=dato:
            currentPos+=1
            aux=aux.getSiguiente()
        if aux==None:
            currentPos=None
            print("El valor",dato,"no fue encontrado!!")
        return currentPos
    def actualizar(self,a_buscar,dato):
        a_buscarPosicion=self.buscar(a_buscar)
        if a_buscarPosicion!=None:
            aux=self.head
            for i in range(a_buscarPosicion):
                aux=aux.getSiguiente()
            aux.setValor(dato)
        
    def transversal(self):
        aux=self.head
        while aux!=None:
            print(aux.getValor().toString(),"--> ",end="")
            aux=aux.getSiguiente()
        print("None")