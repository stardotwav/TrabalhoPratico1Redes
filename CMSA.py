from objects import estacaoCSMA
from objects import canal

def executarCSMAP(numeroEstacoes: int,p=1,limite = 1024,impressaoDetalhada = False):
    #O limite considera até quando será o intervalo de tempo aleatório do RANDOM
    tempo = 0
    canalTeste = canal.Canal()
    N = numeroEstacoes
    listaEstacao = []
    for i in range(N):
        novaEstacao = estacaoCSMA.EstacaoCSMA(i,limite,p)
        novaEstacao.colisaoCSMA()
        canalTeste.ocorrerColisao()
        listaEstacao.append(novaEstacao)
    terminouSimular = False
    canalTeste.desocuparCanal()

    while(terminouSimular == False):
        maquinasTransmitindo = []

        for maquina in listaEstacao:
            maquina.tentarTransmitirCSMA(canalTeste)
            if maquina.emEspera == False:
                maquinasTransmitindo.append(maquina)

        if len(maquinasTransmitindo) == 1:
            canalTeste.ocuparCanal(maquinasTransmitindo[0].numeroEstacao)
            terminouSimular = True

        elif len(maquinasTransmitindo) > 1:
            for i in maquinasTransmitindo:
                i.colisaoCSMA()
                canalTeste.ocorrerColisao()

        canalTeste.passarCanal()
        tempo+=1


    if impressaoDetalhada:
        for i in listaEstacao:
            i.printEstacao()

        print("Dados do canal:")
        canalTeste.printCanal()
        print("Tempo: %.4f u segundos"%(float(tempo)*51.2))

    return tempo