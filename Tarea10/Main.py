from NodoArbol import *

raiz1=NodoArbol(10,None,None)
raiz1.setHijoIzq(NodoArbol(5,NodoArbol(1,None,None),None))
raiz1.setHijoDer(NodoArbol(15,None,NodoArbol(25,None,None)))
print("raiz1:\n",raiz1)


print()
raiz2=NodoArbol("Diego",None,None)
raiz2.setHijoIzq(NodoArbol("Pedro",NodoArbol("Susan",None,None),NodoArbol("Diana",None,None)))
raiz2.setHijoDer(NodoArbol("Mario",None,None))
print("raiz2:\n",raiz2)