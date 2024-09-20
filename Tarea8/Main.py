from ColaConPrioridad import *
from Cliente import *

colaBanco=ColaConPrioridad(5)
#Anadiendo 2 clientes nuevos
colaBanco.encolar(4,Cliente("Gerardo",4))
colaBanco.encolar(4,Cliente("Daniel",4))
print("#Anadiendo 2 clientes nuevos")
print(colaBanco.toString())
print()
#Anadiendo 3 personas no clientes
colaBanco.encolar(5,Cliente("Ximena",5))
colaBanco.encolar(5,Cliente("Maria",5))
colaBanco.encolar(5,Cliente("Ana",5))
print("#Anadiendo 3 personas no clientes")
print(colaBanco.toString())
print()
#Anadiendo 1 celebridad
colaBanco.encolar(1,Cliente("Katy Perry",1))
print("#Anadiendo 1 celebridad")
print(colaBanco.toString())
print()
#Atender al siguiente
siguienteCliente=colaBanco.desencolar()
print("Se atendio a",siguienteCliente)
#Retirando 10 000 de su cuenta
siguienteCliente.retiro(10000)
print(colaBanco.toString())
print()
#Anadiendo 1 cliente frecuente
print("#Anadiendo 1 cliente frecuente")
colaBanco.encolar(3,Cliente("Karen",3))
#Anadiendo 1 cliente premium
colaBanco.encolar(2,Cliente("Nicole",2))
print("#Anadiendo 1 cliente premium")
print(colaBanco.toString())
print()
#Atender al siguiente
siguienteCliente=colaBanco.desencolar()
print("Se atendio a",siguienteCliente)
print(colaBanco.toString())
print()
#Atendiendo al resto de clientes
while not colaBanco.estaVacia():
    siguienteCliente=colaBanco.desencolar()
    print("Se atendio a",siguienteCliente)
print(colaBanco.toString())
print()