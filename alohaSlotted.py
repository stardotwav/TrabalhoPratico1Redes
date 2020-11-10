from objects import estacao
from objects import canal

def executarAlohaSlotted(numeroEstacoes: int,limiteAloha = 1024,impressaoDetalhada = False):
    tempo = 0
    canalTeste = canal.Canal()
    N = numeroEstacoes
    listaEstacao = []
    listaMaquinasTransmitidas = []
    for i in range(N):
        novaEstacao = estacao.Estacao(i)
        novaEstacao.definirLimiteAloha(limiteAloha)
        listaEstacao.append(novaEstacao)
    terminouSimular = False
    numMaquinasTransmitiram = 0
    while(terminouSimular == False):
        maquinasTransmitindo = []
        for maquina in listaEstacao:
            maquina.tentarTransmitirAloha(tempo)
            if maquina.emEspera == False:
                maquinasTransmitindo.append(maquina)

        if len(listaEstacao) == 0:
            terminouSimular = True

        if len(maquinasTransmitindo) == 1:
            canalTeste.ocuparCanal(maquinasTransmitindo[0].numeroEstacao)
            listaMaquinasTransmitidas.append(maquinasTransmitindo[0])
            listaEstacao.remove(maquinasTransmitindo[0])
            numMaquinasTransmitiram+=1

        elif len(maquinasTransmitindo) > 1:
            for i in maquinasTransmitindo:
                i.colisaoAloha()
                canalTeste.ocorrerColisao()

        canalTeste.passarCanal()
        tempo+=1
        if canalTeste.estadoCanal():
            canalTeste.desocuparCanal()


    mediaTempo = 0
    menorTempo = listaMaquinasTransmitidas[0].tempoTransmissao
    for i in listaMaquinasTransmitidas:
        mediaTempo+=i.tempoTransmissao
        if i.tempoTransmissao < menorTempo:
            menorTempo = i.tempoTransmissao
    mediaTempo = mediaTempo / N

    if impressaoDetalhada:
        for i in listaMaquinasTransmitidas:
            i.printEstacao()
        print("Dados do canal:")
        canalTeste.printCanal()
        print("Primeira máquina transmitir: %.4f u segundos"%(float(menorTempo)*51.2))
        print("Média do tempo: %.4f u segundos" % (float(mediaTempo) * 51.2))

    return menorTempo,mediaTempo