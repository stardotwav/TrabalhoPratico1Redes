from objects.canal import Canal
import random

class EstacaoCSMA:
    numeroEstacao = 0
    emEspera: bool
    cooldownTransmitir : int
    limite = 1024
    naoTransmitiu = 0

    def __init__(self,numeroEstacao : int,limite = 1024,p=1):
        self.limite = limite
        self.probabilidadeTransmtir = p #Já está em porcentagem, ou seja, 1 corresponde a 1%
        self.numeroEstacao = numeroEstacao
        self.emEspera = True
        self.cooldownTransmitir = 0

    def printEstacao(self):
        print("--------------------------")
        print("Numero da estação: "+str(self.numeroEstacao)+"")
        print("Quer efetuar a transmissão: " + str(self.emEspera) + "")
        print("Cooldown: "+str(self.cooldownTransmitir)+"")
        print("numVezes que não transmitiu: "+str(self.naoTransmitiu)+"")

        print("--------------------------")

    def tentarTransmitirCSMA(self,canal : Canal):
        if self.cooldownTransmitir == 0:
            if canal.estadoCanal() == False:
                if random.randint(1,100) <= self.probabilidadeTransmtir:
                    self.emEspera = False
                else:
                    self.naoTransmitiu+=1
                    #self.colisaoCSMA()
        else:
            self.cooldownTransmitir -=1

    def colisaoCSMA(self):
        self.emEspera = True
        self.cooldownTransmitir = random.randint(0, self.limite)



# self.cooldownTransmitir = random.randint(1, self.limiteAloha)
