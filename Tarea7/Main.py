from Paciente import *
from ColaADT import *

#Creando la cola y aniadiendo 3 pacientes
colaDePacientes=ColaADT()
colaDePacientes.encolar(Paciente("Daniel",35))
colaDePacientes.encolar(Paciente("Rosa",46))
colaDePacientes.encolar(Paciente("Javier",28))
print(colaDePacientes.toString())
#Mostrando al paciente de adelante
proximoPaciente=colaDePacientes.frente()
print("Proximo paciente: "+proximoPaciente.toString())
print(colaDePacientes.toString())
#Atendiendo al siguiente
print("Atendiendo al siguiente")
colaDePacientes.desencolar()
print(colaDePacientes.toString())
#Aniadiendo 2 pacientes a la cola
print("Aniadiendo 2 pacientes a la cola")
colaDePacientes.encolar(Paciente("Hector",66))
colaDePacientes.encolar(Paciente("Carlos", 54))
print(colaDePacientes.toString())
#Atendiendo al siguiente
print("Atendiendo al siguiente")
colaDePacientes.desencolar()
print(colaDePacientes.toString())