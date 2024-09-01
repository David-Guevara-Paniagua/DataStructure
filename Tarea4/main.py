from Smartphone import *
from Nodo import *
from LinkedList import *
#Creando 5 smartphone
tel1=Smartphone("Nokia",120)
tel2=Smartphone("Xiamoi",256)
tel3=Smartphone("Samsung",500)
tel4=Smartphone("Motorola",80)
tel5=Smartphone("iPhone",256)
#Agragando los smartphones a una linked list
miListaDeSmartphones=LinkedList()
miListaDeSmartphones.agregar_al_final(tel1)
miListaDeSmartphones.agregar_al_final(tel2)
miListaDeSmartphones.agregar_al_final(tel3)
miListaDeSmartphones.agregar_al_final(tel4)
miListaDeSmartphones.agregar_al_final(tel5)
#Imprimiendo el contenido
miListaDeSmartphones.transversal()
#Eliminando el de la posicion 2
miListaDeSmartphones.eliminar(2)
#Imprimiendo el contenido
print()
miListaDeSmartphones.transversal()
#Actualizando el segundo elemento
tel6=Smartphone("Oppo",120)
miListaDeSmartphones.actualizar(tel2,tel6)
#Agregando un elemento al inicio
tel7=Smartphone("LG",80)
miListaDeSmartphones.agregar_al_inicio(tel7)
#Agregando un elemento al final
tel8=Smartphone("Poco",256)
miListaDeSmartphones.agregar_al_final(tel8)
#Imprimiendo el contenido
print()
miListaDeSmartphones.transversal()
#Eliminando el primero
miListaDeSmartphones.eliminar_el_primero()
#Imprimiendo el contenido
print()
miListaDeSmartphones.transversal()

