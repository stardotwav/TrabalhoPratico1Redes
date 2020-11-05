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

        vetorResultado = []
        vetorTentativa = []

        for i in range(33):
            vetorTentativa.append(i)
            vetorResultado.append(executarAlohaSlotted(maquinas,1024,True))

        plt.plot(vetorTentativa, vetorResultado)
        plt.title("Slotted Aloha")
        plt.xlabel('Tentativa')
        plt.ylabel('Resultado')
        nomeArquivo = "slottedAloha.png"
        plt.savefig(nomeArquivo)
        plt.show()

        print()
        print("-------------------------")
        print("Média: %.4f" % float(statistics.mean(vetorResultado)))
        print("Desvio Padrão: %.4f" % float(statistics.stdev(vetorResultado)))
        print("-------------------------")

    elif(comando == 2):
        maquinas = int(input("Digite o Número de Máquinas usadas: "))

        vetorResultado = []
        vetorTentativa = []

        for i in range(33):
            vetorTentativa.append(i)
            vetorResultado.append(executarCSMAP(maquinas,1,1024,True))

        plt.plot(vetorTentativa, vetorResultado)
        plt.title("CSMA P-Persistente")
        plt.xlabel('Tentativa')
        plt.ylabel('Resultado')
        nomeArquivo = "csmaPPersistente.png"
        plt.savefig(nomeArquivo)
        plt.show()

        print()
        print("-------------------------")
        print("Média: %.4f" % float(statistics.mean(vetorResultado)))
        print("Desvio Padrão: %.4f" % float(statistics.stdev(vetorResultado)))
        print("-------------------------")
        
    elif(comando == 3):
        maquinas = int(input("Digite o Número de Máquinas usadas: "))
        
        vetorResultado = []
        vetorTentativa = []

        for i in range(33):
            vetorTentativa.append(i)
            vetorResultado.append(executarRecuo(maquinas,True))

        plt.plot(vetorTentativa, vetorResultado)
        plt.title("Algoritmo de Recuo Binário Exponencial")
        plt.xlabel('Tentativa')
        plt.ylabel('Resultado')
        nomeArquivo = "algoritmoBinarioExponencial.png"
        plt.savefig(nomeArquivo)
        plt.show()

        print()
        print("-------------------------")
        print("Média: %.4f" % float(statistics.mean(vetorResultado)))
        print("Desvio Padrão: %.4f" % float(statistics.stdev(vetorResultado)))
        print("-------------------------")
        
    else:
        break

#vetorResultado = []
#for i in range(33):
    #vetorResultado.append(executarAlohaSlotted(10,3,True))
    #executarCSMAP(10,1,2,True)

#executarAlohaSlotted(10,5000,True)
#executarCSMAP(10,25,2,True)
#executarRecuo(10,True)