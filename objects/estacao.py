from objects.canal import Canal
import random

class Estacao:
    limiteAloha = 3
    numeroEstacao = 0
    querTransmitir: bool
    cooldownTransmitir : int

    def __init__(self,numeroEstacao : int):
        self.numeroEstacao = numeroEstacao
        self.querTransmitir = True
        self.cooldownTransmitir = 0

    def printEstacao(self):
        print("--------------------------")
        print("Numero da estação: "+str(self.numeroEstacao)+"")
        print("Quer efetuar a transmissão: "+str(self.querTransmitir)+"")
        print("Cooldown: "+str(self.cooldownTransmitir)+"")
        print("--------------------------")

    def definirLimiteAloha(self,numLimite):
        self.limiteAloha = numLimite

    def tentarTransmitirAloha(self,canal : Canal):
        if self.cooldownTransmitir == 0:
            self.querTransmitir = False
        else:
            self.cooldownTransmitir -=1

    def colisaoAloha(self):
        self.querTransmitir = True
        self.cooldownTransmitir = random.randint(1, self.limiteAloha)


