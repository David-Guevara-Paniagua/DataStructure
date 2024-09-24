from PilaADT import *

def IsBalanced(texto):
    pilaLlaves=Pila()
    pilaParentesis=Pila()
    hayLlavesExtra=False
    hayParentesisExtra=False

    for char in texto:
        if char=='{':
            pilaLlaves.push(1)
        elif char=='(':
            pilaParentesis.push(1)
        elif char=='}':
            if not pilaLlaves.isEmpty():#Verificar que no se hara un pop de una pila vacia
                pilaLlaves.pop()
            else:
                hayLlavesExtra=True
        elif char==')':
            if not pilaParentesis.isEmpty():#Verificar que no se hara un pop de una pila vacia
                pilaParentesis.pop()
            else:
                hayParentesisExtra=True
                
    if pilaLlaves.isEmpty() and not hayLlavesExtra:
        print("Las llaves estan balanceadas :)")
    else:
        print("Las llaves no estan balanceadas!!")
    if pilaParentesis.isEmpty() and not hayParentesisExtra:
        print("Los parentesis estan balanceados :)")
    else:
        print("Los parentesis no estan balanceados!!")

texto="añlsdkfañl(dk)jf{}lsikdj.x"

#texto=str(input("Ingresa el texto a verificar:\n"))

#O ANIADA EL TEXTO AQUI
#texto=(suTexto)

print()
IsBalanced(texto)
        