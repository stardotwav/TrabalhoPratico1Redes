class Canal:
    numCanal : int
    canalOcupado = False
    numEstacao = -1
    numColisoes: int

    def __init__(self):
        self.canalOcupado = True
        self.numCanal = 0
        self.numColisoes = 0

    def estadoCanal(self):
        return self.canalOcupado

    def ocuparCanal(self,numeroEstacao:int):
        self.canalOcupado = True
        self.numEstacao = numeroEstacao

    def desocuparCanal(self):
        self.canalOcupado = False
        self.numEstacao = -1

    def passarCanal(self):
        self.numCanal+=1

    def ocorrerColisao(self):
        self.numColisoes+=1

    def printCanal(self):
        print("--------------------------")
        print("Numero de canais necessários: "+str(self.numCanal))
        print("Numero de colisões: "+str(self.numColisoes))
        print("ID da estação que transmitiu: "+str(self.numEstacao))
        print("--------------------------")

