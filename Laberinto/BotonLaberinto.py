import tkinter as tk
class BotonLaberinto:
    def __init__(self,ventana,x,y,tipo):
        self.x=x
        self.y=y
        self.tipo=tipo
        self.boton=tk.Button(ventana,width=4,height=2)
        self.boton.config(background="grey")
        self.boton.grid(column=self.x,row=self.y)
    def colorearVerde(self):
        self.boton.config(background="green")
    def colorearAzul(self):
        self.boton.config(background="blue")
    def colorearRojo(self):
        self.boton.config(background="red")
    def colorearNegro(self):
        self.boton.config(background="black")