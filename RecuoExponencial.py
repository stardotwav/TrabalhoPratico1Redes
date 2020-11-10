from objects import estacaoRecuo
from objects import canal

def executarRecuo(numeroEstacoes: int,impressaoDetalhada = False):
    #O limite considera até quando será o intervalo de tempo aleatório do RANDOM
    tempo = 2
    canalTeste = canal.Canal()
    N = numeroEstacoes
    listaEstacao = []
    listaFalhas = []
    listaMaquinasTransmitidas = []

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
            maquina.tentarTransmitir(canalTeste,tempo)
            if maquina.emEspera == False:
                maquinasTransmitindo.append(maquina)
            if maquina.numColisoes == 16:
                listaFalhas.append(maquina)
                listaEstacao.remove(maquina)

        if len(maquinasTransmitindo) == 1:
            canalTeste.ocuparCanal(maquinasTransmitindo[0].numeroEstacao)
            listaMaquinasTransmitidas.append(maquinasTransmitindo[0])
            listaEstacao.remove(maquinasTransmitindo[0])

        elif len(maquinasTransmitindo) > 1:
            for i in maquinasTransmitindo:
                i.colisao()
                canalTeste.ocorrerColisao()

        if len(listaEstacao) == 0:
            terminouSimular = True
            break

        canalTeste.passarCanal()
        tempo += 1
        if canalTeste.estadoCanal():
            canalTeste.desocuparCanal()

    mediaTempo = 0
    menorTempo = listaMaquinasTransmitidas[0].tempoTransmissao
    for i in listaMaquinasTransmitidas:
        mediaTempo += i.tempoTransmissao
        if i.tempoTransmissao < menorTempo:
            menorTempo = i.tempoTransmissao
    mediaTempo = mediaTempo / N

    if impressaoDetalhada:
        print("Maquinas que falharam:")
        for i in listaFalhas:
            i.printEstacao()
        print("Maquinas que deram em sucesso:")
        for i in listaMaquinasTransmitidas:
            i.printEstacao()

        print("Dados do canal:")
        canalTeste.printCanal()
        print("Primeira máquina transmitir: %.4f u segundos" % (float(menorTempo) * 51.2))
        print("Média do tempo: %.4f u segundos" % (float(mediaTempo) * 51.2))

    return menorTempo, mediaTempo