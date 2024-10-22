#El primero es el problema de  sacar de un ADT pila el valor en la posición media
#  con recursión.

import sys
sys.path.append("C:/Users/David/Documents/EstructuraDeDatos_fes_aragon")
from Tarea9.PilaADT import *

def definirValorMedio(tamanioOriginal):
    if tamanioOriginal%2!=0: return int(tamanioOriginal/2)+1
    else: return tamanioOriginal/2

def getValorDeEnMedio(pila, tamanioOriginal):
    if not pila.isEmpty():
        #sacar hasta el valor medio, luego agregar los sacados
        if pila.length() != definirValorMedio(tamanioOriginal):
            valor=pila.pop()
            getValorDeEnMedio(pila, tamanioOriginal)
            pila.push(valor)
        else:
            pila.pop()
    else:
        print("La pila esta vacia!")

# main--------------
myStack=Pila()
for i in range(5):
    myStack.push(i+1)
print(myStack)
print("---------------")
getValorDeEnMedio(myStack,myStack.length())
print(myStack)
