from objects import estacaoRecuo
from objects import canal

def executarRecuo(numeroEstacoes: int,impressaoDetalhada = False):
    #O limite considera até quando será o intervalo de tempo aleatório do RANDOM
    tempo = 0
    canalTeste = canal.Canal()
    N = numeroEstacoes
    listaEstacao = []
    for i in range(N):
        novaEstacao = estacaoRecuo.Estacao(i)
        novaEstacao.colisao()
        canalTeste.ocorrerColisao()
        listaEstacao.append(novaEstacao)
    terminouSimular = False
    canalTeste.desocuparCanal()

    while(terminouSimular == False):
        maquinasTransmitindo = []

        for maquina in listaEstacao:
            maquina.tentarTransmitir(canalTeste)
            if maquina.emEspera == False:
                maquinasTransmitindo.append(maquina)

        if len(maquinasTransmitindo) == 1:
            canalTeste.ocuparCanal(maquinasTransmitindo[0].numeroEstacao)
            terminouSimular = True

        elif len(maquinasTransmitindo) > 1:
            for i in maquinasTransmitindo:
                i.colisao()
                canalTeste.ocorrerColisao()

        canalTeste.passarCanal()
        tempo+=1


    if impressaoDetalhada:
        for i in listaEstacao:
            i.printEstacao()

        print()
        print("Dados do canal:")
        canalTeste.printCanal()
        print("Tempo: %.4f u segundos"%(float(tempo)*51.2))
        print("--------------------------")
        print()

    return tempo