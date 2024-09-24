class Pila:
    def __init__(self):
        self.data=[]
        self.top=None
    def isEmpty(self):
        flag = False
        if self.data==[]:
            flag=True
        return flag
    def length(self):
        return len(self.data)
    def pop(self):
        if not self.isEmpty():
            try:
                self.top=self.data[-2]
            except IndexError:
                self.top=None
            return self.data.pop()
        else:
            print("La pila esta vacia!!")
    def peek(self):
        return self.top
    def push(self,valor):
        self.data.append(valor)
        self.top=self.data[-1]
    def __str__(self):
        cadena="["
        for item in self.data:
            cadena+=str(item)+", "
        if not self.isEmpty(): cadena=cadena[:-2]
        cadena+="]"
        return cadena
