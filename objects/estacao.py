from objects.canal import Canal
import random

class Estacao:
    limiteAloha = 3
    numeroEstacao = 0
    emEspera: bool
    cooldownTransmitir : int
    tempoTransmissao = 0

    def __init__(self,numeroEstacao : int):
        self.numeroEstacao = numeroEstacao
        self.emEspera = True
        self.cooldownTransmitir = 0

    def printEstacao(self):
        print("--------------------------")
        print("Numero da estação: "+str(self.numeroEstacao)+"")
        print("Quer efetuar a transmissão: " + str(self.emEspera) + "")
        print("Quando transmitiu: "+str(self.tempoTransmissao)+"")
        print("--------------------------")

    def definirLimiteAloha(self,numLimite):
        self.limiteAloha = numLimite

    def tentarTransmitirAloha(self,tempo : int):
        if self.cooldownTransmitir == 0 and self.emEspera==True:
            self.emEspera = False
            self.tempoTransmissao = tempo
        else:
            self.cooldownTransmitir -=1

    def colisaoAloha(self):
        self.emEspera = True
        self.cooldownTransmitir = random.randint(1, self.limiteAloha)


