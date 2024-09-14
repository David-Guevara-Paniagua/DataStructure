class Array2d:
    def __init__(self,ren,col):
        self.ren=ren
        self.col=col
        self.data=[]
        for i in range(self.ren):
            newRen=[]
            for j in range(self.col):
                newRen.append(None)
            self.data.append(newRen)
    def clear(self, dato):
        ren=[]
        for fila in range(self.ren):
            for col in range(self.col):
                ren.append(dato)
            self.data.append(ren)
    def getRen(self):
        return self.ren
    def getCol(self):
        return self.col
    def toString(self):
        for ren in self.data:
            for col in ren:
                print(col.toString(),end=" ")
            print()
    def setItem(self,ren,col,dato):
        if(ren<0 or ren>=self.ren or col<0 or col>=self.col):
            raise IndexError
        else:
            self.data[ren][col]=dato
    def getItem(self,ren,col):
        item=None
        if(ren<0 or ren>=self.ren or col<0 or col>=self.col):
            raise IndexError
            item='\0'
        else:
            item=self.data[ren][col]
        return item
