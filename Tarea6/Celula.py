class Celula:
    def __init__(self,celulaRen,celulaCol):
        self.estoyViva=False
        self.estoyVivaSiguienteGen=False
        self.celulaRen=celulaRen
        self.celulaCol=celulaCol

    def estareViva(self,rejilla):
        vecinosVivos=self.contarVecinosVivos(rejilla)
        self.estoyVivaSiguienteGen = False
        if (self.estoyViva and vecinosVivos==2) or (self.estoyViva and vecinosVivos==3):
            self.estoyVivaSiguienteGen=True
        if (not self.estoyViva and vecinosVivos==3):
            self.estoyVivaSiguienteGen=True
        return self.estoyVivaSiguienteGen

    def contarVecinosVivos(self,rejilla):
        vecinosVivos=0

        try:
            for col in range(self.celulaCol-1,self.celulaCol+2):#Buscando en renglon de arriba
                if col >= 0:
                    if rejilla.getItem(self.celulaRen-1,col).estoyViva:
                        vecinosVivos+=1
        except (IndexError,AttributeError):
            pass

        try:
            for col in range(self.celulaCol-1,self.celulaCol+2):#Buscando en renglon de abajo
                if col >= 0:
                    if rejilla.getItem(self.celulaRen+1,col).estoyViva:
                        vecinosVivos+=1
        except (IndexError,AttributeError):
            pass
        
        if self.celulaCol-1 >= 0:
            if rejilla.getItem(self.celulaRen,self.celulaCol-1).estoyViva:#Buscando a la izq
                vecinosVivos+=1
                
        try:
            if rejilla.getItem(self.celulaRen,self.celulaCol+1).estoyViva:#Buscando a la der
                vecinosVivos+=1
        except (IndexError,AttributeError):
            pass

        return vecinosVivos

    def actualizarEstado(self):
        self.estoyViva=self.estoyVivaSiguienteGen

    def toString(self):
        estado='m'
        if self.estoyViva:
            estado='v'
        return estado