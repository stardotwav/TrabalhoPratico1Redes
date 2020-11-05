from objects import estacao
from objects import canal

def executarAlohaSlotted(numeroEstacoes: int,limiteAloha = 1024,impressaoDetalhada = False):
    tempo = 0
    canalTeste = canal.Canal()
    N = numeroEstacoes
    listaEstacao = []
    for i in range(N):
        novaEstacao = estacao.Estacao(i)
        novaEstacao.definirLimiteAloha(limiteAloha)
        listaEstacao.append(novaEstacao)
    terminouSimular = False

    while(terminouSimular == False):
        maquinasTransmitindo = []

        for maquina in listaEstacao:
            maquina.tentarTransmitirAloha(canalTeste)
            if maquina.querTransmitir == False:
                maquinasTransmitindo.append(maquina)

        if len(maquinasTransmitindo) == 1:
            canalTeste.ocuparCanal(maquinasTransmitindo[0].numeroEstacao)
            terminouSimular = True

        elif len(maquinasTransmitindo) > 1:
            for i in maquinasTransmitindo:
                i.colisaoAloha()
                canalTeste.ocorrerColisao()

        if tempo == 0:
            canalTeste.desocuparCanal()
        canalTeste.passarCanal()
        tempo+=1


    if impressaoDetalhada:
        for i in listaEstacao:
            i.printEstacao()
        print("Dados do canal:")
        canalTeste.printCanal()
        print("Tempo: %.4f u segundos"%(float(tempo)*51.2))

    return tempo