from alohaSlotted import executarAlohaSlotted
from CMSA import executarCSMAP
from RecuoExponencial import executarRecuo
import matplotlib.pyplot as plt
import statistics

while(True):
    print("------------------ MENU ------------------")
    print("1. Slotted Aloha")
    print("2. CSMA P-Persistente")
    print("3. Algoritmo de Recuo Binário Exponencial")
    print("4. Sair")
    print("------------------------------------------")
    comando = int(input("Comando: "))
    print()

    if(comando == 1):
        maquinas = int(input("Digite o Número de Máquinas usadas: "))

        numTentativa = []
        vetorTempoMedio = []
        vetorTempoPrimeira = []

        for i in range(33):
            numTentativa.append(i)
            tempoPrimeiro,tempoMedio = executarAlohaSlotted(maquinas, 1024, False)
            vetorTempoPrimeira.append(51.2 * tempoPrimeiro)
            vetorTempoMedio.append(51.2 * tempoMedio)


        print("--------------------------------------------")
        print("Média Primeira Estação: %.4f" % float(statistics.mean(vetorTempoPrimeira)))
        print("Desvio Padrão Primeira Estção: %.4f" % float(statistics.stdev(vetorTempoPrimeira)))
        print("Média Todas as Estações: %.4f" % float(statistics.mean(vetorTempoMedio)))
        print("Desvio Padrão Todas as Estações: %.4f" % float(statistics.stdev(vetorTempoMedio)))
        print("--------------------------------------------")


        plt.plot(numTentativa, vetorTempoPrimeira)
        plt.xlabel("Tentativa")
        plt.ylabel('Tempo Primeiro Estção Transmitir')
        plt.savefig('slottedAlohaPrimeiraEstacao' + str(maquinas) + '.png')
        plt.show()

        plt.plot(numTentativa, vetorTempoMedio)
        plt.xlabel("Tentativa")
        plt.ylabel('Média de Tempo')
        plt.savefig('slottedAlohaTodasEstacoes' + str(maquinas) + '.png')
        plt.show()

    elif(comando == 2):
        maquinas = int(input("Digite o Número de Máquinas usadas: "))

        numTentativa = []
        vetorTempoMedio = []
        vetorTempoPrimeira = []

        for i in range(33):
            numTentativa.append(i)
            tempoPrimeiro,tempoMedio = executarCSMAP(maquinas,1,1024,False)
            vetorTempoPrimeira.append(tempoPrimeiro)
            vetorTempoMedio.append(tempoMedio)

        print("--------------------------------------------")
        print("Média Primeira Estação: %.4f" % float(statistics.mean(vetorTempoPrimeira)))
        print("Desvio Padrão Primeira Estção: %.4f" % float(statistics.stdev(vetorTempoPrimeira)))
        print("Média Todas as Estações: %.4f" % float(statistics.mean(vetorTempoMedio)))
        print("Desvio Padrão Todas as Estações: %.4f" % float(statistics.stdev(vetorTempoMedio)))
        print("--------------------------------------------")

        plt.plot(numTentativa, vetorTempoPrimeira)
        plt.xlabel("Tentativa")
        plt.ylabel('Tempo Primeiro Estção Transmitir')
        plt.savefig('csmaPPersistentePrimeiraEstacao' + str(maquinas) + '.png')
        plt.show()

        plt.plot(numTentativa, vetorTempoMedio)
        plt.xlabel("Tentativa")
        plt.ylabel('Média de Tempo')
        plt.savefig('csmaPPersistenteTodasEstacoes' + str(maquinas) + '.png')
        plt.show()

        
    elif(comando == 3):
        maquinas = int(input("Digite o Número de Máquinas usadas: "))

        numTentativa = []
        vetorTempoMedio = []
        vetorTempoPrimeira = []

        for i in range(33):
            numTentativa.append(i)
            tempoPrimeiro,tempoMedio = executarRecuo(maquinas,False)
            vetorTempoPrimeira.append(tempoPrimeiro)
            vetorTempoMedio.append(tempoMedio)


        print("--------------------------------------------")
        print("Média Primeira Estação: %.4f" % float(statistics.mean(vetorTempoPrimeira)))
        print("Desvio Padrão Primeira Estção: %.4f" % float(statistics.stdev(vetorTempoPrimeira)))
        print("Média Todas as Estações: %.4f" % float(statistics.mean(vetorTempoMedio)))
        print("Desvio Padrão Todas as Estações: %.4f" % float(statistics.stdev(vetorTempoMedio)))
        print("--------------------------------------------")

        plt.plot(numTentativa, vetorTempoPrimeira)
        plt.xlabel("Tentativa")
        plt.ylabel('Tempo Primeiro Estção Transmitir')
        plt.savefig('algoritmoBinarioExponencialPrimeiraEstacao' + str(maquinas) + '.png')
        plt.show()

        plt.plot(numTentativa, vetorTempoMedio)
        plt.xlabel("Tentativa")
        plt.ylabel('Média de Tempo')
        plt.savefig('algoritmoBinarioExponencialTodasEstacoes' + str(maquinas) + '.png')
        plt.show()
        
    else:
        break