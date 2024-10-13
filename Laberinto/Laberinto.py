import sys
sys.path.append("C:/Users/David/Documents/EstructuraDeDatos_fes_aragon")
from Tarea6.Array2d import *
from Tarea9.PilaADT import *
import tkinter as tk
from BotonLaberinto import BotonLaberinto

#funcion para asingar bloques 'camino'
def asignarCamino(array):
    global laberinto
    for i in array:
        laberinto.setItem(i[0],i[1],'c')

#------------Hacer el laberinto-----------------
#laberinto=Array2d(6,6)
laberinto=Array2d(8,8)

#Llenarlo con bloques 'pared'
laberinto.clear('p')

#Asignar los bloques 'camino'
camino=[[7,2],[6,2],[5,2],[5,3],[5,4],[4,4],[3,4],[2,4],[2,3],[2,2],[1,2],[0,2],
[0,3],[0,4],[0,5],[0,6],[1,6],[2,6],[3,6],[3,7]]
#Asignar los blques 'camino' sin salida
camino.extend([[5,1],[4,2],[5,5]])
asignarCamino(camino)

#Asignar entrada y salida
entrada=[7,2]
salida=[3,7]

#funcion para Asignar laberitno propio----------*------------*---------------*----
def asignarLaberintoPropio(texto,posEntrada,posSalida):
    if texto!=None:
        renglones=[]
        renglon=[]
        for char in texto:
            if char!='\n':
                renglon.append(char)
            else:
                renglones.append(renglon)
                renglon=[]
        renglones.append(renglon)
        tamanioRenglones=len(renglones)
        tamanioColumnas=len(renglones[0])
        crearLaberintoConDatosPropios(tamanioRenglones,tamanioColumnas,renglones,posEntrada,posSalida)

def crearLaberintoConDatosPropios(tamanioRenglones,tamanioColumnas,renglones,posEntrada,posSalida):
    global laberinto,entrada,salida
    laberinto=Array2d(tamanioRenglones,tamanioColumnas)
    for renglon in range(tamanioRenglones):
        for columna in range(tamanioColumnas):
            laberinto.setItem(renglon,columna,renglones[renglon][columna])
    entrada=posEntrada
    salida=posSalida

#INSTRUCCIONES
#aniadir laberinto propio en 'textoLaberinto' (separando renglones con \n)-----------
#posciones de entrada y salida como listas con [x,y]
#'p' para pared
#'c' para camino

textoLaberinto=None #ANIADIR LABERINTO AQUI---------*-------*-------*
posSalida=[]
posEntrada=[]
asignarLaberintoPropio(textoLaberinto,posEntrada,posSalida)
print(laberinto)
#---------------------Mostrar laberinto y algoritmo---------

ListaDeBloques=[]
currentPos=entrada
pilaDeMovimientos=Pila()
listaCaminosSinSalida=[]
fin=False

def mostrarLaberinto(laberinto):
    root=tk.Tk()
    crearBloques(root,laberinto)
    pintarBloquesCamino()
    pintarSalida()
    pintarEntrada()
    root.after(1000,algoritmo,root)
    
    root.mainloop()

def crearBloques(ventana,laberinto):
    global ListaDeBloques
    for ren in range(len(laberinto)):
        for col in range(len(laberinto[0])):
            nuevoBloque=BotonLaberinto(ventana,col,ren,laberinto[ren][col])
            ListaDeBloques.append(nuevoBloque)
            
def pintarBloquesCamino():
    global ListaDeBloques
    print()
    for bloque in ListaDeBloques:
        if bloque.tipo=='c':
            bloque.colorearVerde()
def pintarAzul():
    for bloque in ListaDeBloques:
        if bloque.x==currentPos[1] and bloque.y==currentPos[0]:
            bloque.colorearAzul()
def pintarNegro():
    for bloque in ListaDeBloques:
        if bloque.x==currentPos[1] and bloque.y==currentPos[0]:
            bloque.colorearNegro()

def pintarSalida():
    for bloque in ListaDeBloques:
        if bloque.x==salida[1] and bloque.y==salida[0]:
            bloque.colorearRojo()
def pintarEntrada():
    for bloque in ListaDeBloques:
        if bloque.x==entrada[1] and bloque.y==entrada[0]:
            bloque.colorearRojo()       

def algoritmo(root):
    global laberinto, currentPos
    aniadirPosALaPila()
    esCaminoSinSalida=buscarCamino()
    pintarAzul()
    if esCaminoSinSalida:
        listaCaminosSinSalida.append(currentPos)
        pilaDeMovimientos.pop()
        pintarNegro()
        currentPos=pilaDeMovimientos.pop()
    
    if currentPos!=salida:
        root.after(500,algoritmo,root)
    else:
        global fin
        if not fin:
            fin=True
            mostrarDatos()
    

def buscarCamino():
    global currentPos
    esCaminoSinSalida=False
    if hayCamino("izq"):
        currentPos=moverA("izq")
    elif hayCamino("arriba"):
        currentPos=moverA("arriba")
    elif hayCamino("der"):
        currentPos=moverA("der")
    elif hayCamino("abajo"):
        currentPos=moverA("abajo")
    else:
        print(currentPos,"Camino sin salida!!")
        esCaminoSinSalida=True
    return esCaminoSinSalida

def hayCamino(direccion):
    global pilaDeMovimientos
    posicionAAnalizar=None
    valorDePosicionAAnalizar=None
    flag=False
    try:
        if direccion=="izq":
            posicionAAnalizar=[currentPos[0],currentPos[1]-1]
            valorDePosicionAAnalizar=laberinto.getItem(currentPos[0],currentPos[1]-1)
        elif direccion=="arriba":
            posicionAAnalizar=[currentPos[0]-1,currentPos[1]]
            valorDePosicionAAnalizar=laberinto.getItem(currentPos[0]-1,currentPos[1])
        elif direccion=="der":
            posicionAAnalizar=[currentPos[0],currentPos[1]+1]
            valorDePosicionAAnalizar=laberinto.getItem(currentPos[0],currentPos[1]+1)
        elif direccion=="abajo":
            posicionAAnalizar=[currentPos[0]+1,currentPos[1]]
            valorDePosicionAAnalizar=laberinto.getItem(currentPos[0]+1,currentPos[1])
    except IndexError:
        pass
    if valorDePosicionAAnalizar=='c':
        if posicionAAnalizar not in listaCaminosSinSalida and posicionAAnalizar not in pilaDeMovimientos.data:
            flag=True

    return flag

def moverA(direccion):
    newPos=currentPos

    if direccion=="izq":
        newPos[1]-=1
    elif direccion=="arriba":
        newPos[0]-=1
    elif direccion=="der":
        newPos[1]+=1
    elif direccion=="abajo":
        newPos[0]+=1
    
    return newPos

def aniadirPosALaPila():
    posAAniadir=[currentPos[0],currentPos[1]]
    pilaDeMovimientos.push(posAAniadir)

def mostrarDatos():
    print("Pila de movs:",pilaDeMovimientos)
    print("currentPos=",currentPos)
    print("listaCaminosSinSalida:",listaCaminosSinSalida)

#-------Mostrar el laberinto
mostrarLaberinto(laberinto.data)

