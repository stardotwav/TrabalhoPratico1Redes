from alohaSlotted import executarAlohaSlotted
from CMSA import executarCSMAP
from RecuoExponencial import executarRecuo
import matplotlib.pyplot as plt

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
        print()
        print("--------------------------")
        vetorResultado = []
        for i in range(33):
            vetorResultado.append(executarAlohaSlotted(maquinas,1024,True))

        plt.plot(vetorResultado)
        plt.ylabel('Slotted Aloha')
        plt.savefig('books_read.png')
        plt.show()

    elif(comando == 2):
        maquinas = int(input("Digite o Número de Máquinas usadas: "))
        print()
        print("--------------------------")
        executarCSMAP(maquinas,25,2,True)
        
    elif(comando == 3):
        maquinas = int(input("Digite o Número de Máquinas usadas: "))
        print()
        print("--------------------------")
        executarRecuo(maquinas,True)
        
    else:
        break

#vetorResultado = []
#for i in range(33):
    #vetorResultado.append(executarAlohaSlotted(10,3,True))
    #executarCSMAP(10,1,2,True)

#executarAlohaSlotted(10,5000,True)
#executarCSMAP(10,25,2,True)
#executarRecuo(10,True)