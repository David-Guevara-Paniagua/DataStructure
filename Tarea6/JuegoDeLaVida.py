from Array2d import *
from Celula import *

#Creando la rejilla
rejillaRen=int(input("Cuantas filas tendra la rejilla? "))
rejillaCol=int(input("Cuantas columnas tendra la rejilla? "))

rejilla=Array2d(rejillaRen,rejillaCol)
rejillaSiguienteGen=Array2d(rejillaRen,rejillaCol)#Creando la rejilla de la siguiente generacion    

#Llenandola con objetos Celula muertos
for ren in range(rejilla.getRen()):
    for col in range(rejilla.getCol()):
        rejilla.setItem(ren,col,Celula(ren,col))
rejilla.toString()

#Config inicial
print()
print("Config inicial")

colocarCelulaViva=1
while colocarCelulaViva==1:
    celulaRen=int(input("En que fila quieres colocar la celula viva? "))
    celulaCol=int(input("En que columna quieres colocar la celula viva? "))
    if celulaRen >= 0 and celulaRen < rejillaRen and celulaCol>= 0 and celulaCol<rejillaCol:
        rejilla.getItem(celulaRen,celulaCol).estoyViva=True
    else:
        print("Valores no validos!!\n")
    rejilla.toString()
    print()
    print("Desea colocar otra celula?")
    print("1. Si")
    print("2. No")
    colocarCelulaViva=int(input())

print()
generacionesACalcular=int(input("Cuantas generaciones desea calcular? "))
print()
print("Config inicial")
rejilla.toString()
print()
for i in range(generacionesACalcular):
    for ren in range(rejilla.getRen()):
        for col in range(rejilla.getCol()):
            rejilla.getItem(ren,col).estareViva(rejilla)

    for ren in range(rejilla.getRen()):
        for col in range(rejilla.getCol()):
            rejilla.getItem(ren,col).actualizarEstado()

    rejilla.toString()
    print()
