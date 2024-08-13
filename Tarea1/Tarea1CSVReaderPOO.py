#Author Guevara Paniagua David
#Importando la libreria para leer archivos CSV
import csv

class Accion():
    #Creando matriz para guardar registros
    #Creando string con los meses a elegir
    matriz=[]
    menuMeses="1. Enero\n2. Febrero\n3. Marzo\n4. Abril\n5. Mayo\n6. Junio"

    def readCSV(self):
        #Abrir archivo csv y aniadir registros a una matriz
        with open("tarea1/PresenciaRedesSociales.csv") as myCSVFile:
            reader=csv.reader(myCSVFile)
            for registro in reader:
                self.matriz.append(registro)
                
    def mostrarMatriz(self):
        for registro in self.matriz:
            print(registro)

    def diferenciaSeguidoresTwitter(self):
        print("Elige el primer mes:")
        print(self.menuMeses)
        mes1=int(input())+2
        print("Elige el segundo mes:")
        print(self.menuMeses)
        mes2=int(input())+2
        diferencia=int(self.matriz[8][mes2])-int(self.matriz[8][mes1])
        print("La diferencia es de:",diferencia,"seguidores")

    def diferenciaVisualizacionesYoutube(self):
        print("Elige el primer mes:")
        print(self.menuMeses)
        mes1=int(input())+2
        print("Elige el segundo mes:")
        print(self.menuMeses)
        mes2=int(input())+2
        diferencia=int(self.matriz[16][mes2])-int(self.matriz[16][mes1])
        print("La diferencia es de:",diferencia,"visulizaciones")

    def calcularPromedio(self, registro):
        promedio=0
        i=3
        while i<9:
            promedio+=int(registro[i])
            i+=1
        promedio/=6
        return promedio

    def promedioCrecimientoTwitterYFacebook(self):
        promedio=self.calcularPromedio(self.matriz[9])
        print("El promedio de crecimiento en Twitter es de", promedio)

        promedio=self.calcularPromedio(self.matriz[2])
        print("El promedio de crecimiento en Facebook es de", promedio)

    def promedioMeGusta(self):
        promedio=self.calcularPromedio(self.matriz[9])
        print("El promedio de me gusta en Twitter es de ",promedio)

        promedio=self.calcularPromedio(self.matriz[2])
        print("El promedio de me gusta en Facebook es de ",promedio)

        promedio=self.calcularPromedio(self.matriz[18])
        print("El promedio de me gusta en YouTube es de ",promedio)

    #Menu principal
    def menu(self):
        continuar=1
        while continuar==1:
            print("Que accion quieres realizar?")
            print("1. Calcular diferencia de seguidores")
            print("2. Calcular diferencia de visulizaciones")
            print("3. Mostrar promedio de crecimiento en Twitter y Facebook")
            print("4. Mostrar promedio de me gusta de Twitter, Facebook y YouTube")
            print("5. Salir")
            opcion=int(input())
            if opcion==1:
                self.diferenciaSeguidoresTwitter()
            elif opcion==2:
                self.diferenciaVisualizacionesYoutube()
            elif opcion==3:
                self.promedioCrecimientoTwitterYFacebook()
            elif opcion==4:
                self.promedioMeGusta()
            elif opcion==5:
                print("Saliendo...")
                continuar=2

            if opcion != 5:
                print("Para continuar presiona cualquier tecla y enter")
                input()

#Creando el objeto accion1
accion1= Accion()
#Leyendo el archivo csv
accion1.readCSV()
#Ejecutando el menu principal
accion1.menu()