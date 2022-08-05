def main():
    print("[1]: jogador1 vs jogador2")
    print("[2]: jogador vs computador")
    print("Escolha o modo do jogo:")
    modoDeJogo = int(input())
    n = int(input("Entre com o numero de pecas:"))
    print()
    print("Entre com o numero maximo de pecas que podem ser retiradas:")
    m = int(input())
    print("*****")

    turno = 1
    fimDeJogo = False
    nPecas = n
    #caso usuario escolha o modo 1
    if (modoDeJogo == 1):
        while(not fimDeJogo):
            print("Turno:", turno)
            if (turno%2): #significa que estamos em rodada impar, jogador 1 joga
                print("Jogador: 1")
            else:
                print("Jogador: 2")
            print("Quantas pecas voce gostaria de retirar?:")
            pecasRetiradas = int(input())
            print("Jogador retirou", pecasRetiradas, "peca(s)")
            nPecas = nPecas - pecasRetiradas
            print("Numero de pecas restantes =", nPecas)
            print("*****")
            if (nPecas == 0):
                fimDeJogo = True
                if (turno%2):
                    print("Jogador 1 ganhou!")
                else:
                    print("Jogador 2 ganhou!")
            turno += 1

    #caso usuario escolha o modo 2
    else:
        if (n%(m+1) == 0): #computador "convida" jogador a comecar
            while (not fimDeJogo):
                print("Turno:", turno)
                print("Quantas pecas voce gostaria de retirar?:")
                pecasRetiradas = int(input())
                print("Jogador retirou", pecasRetiradas, "peca(s)")
                nPecas = nPecas - pecasRetiradas
                print("Numero de pecas restantes =", nPecas)
                print("*****")
                turno += 1
                print("Turno:", turno)
                ehMultiplo = False
                temp = m
                while (not ehMultiplo):
                    if ((nPecas - temp) % (m+1) == 0):
                        pecasRetiradas = temp
                        ehMultiplo = True
                    else:
                        temp -= 1
                nPecas = nPecas - pecasRetiradas
                print("Computador retirou", pecasRetiradas, "peca(s)")
                print("Numero de pecas restantes =", nPecas)
                print("*****")
                turno += 1
                if (nPecas == 0):
                    fimDeJogo = True
                    print("Que pena! Voce perdeu!")
        
        else: #computador comeca 
            print("Turno:", turno)
            ehMultiplo = False
            temp = m
            while (not ehMultiplo):
                if ((nPecas - temp) % (m+1) == 0):
                    pecasRetiradas = temp
                    ehMultiplo = True
                else:
                    temp -= 1
            nPecas = nPecas - pecasRetiradas
            print("Computador retirou", pecasRetiradas, "peca(s)")
            print("Numero de pecas restantes =", nPecas)
            print("*****")
            turno += 1
            if (nPecas == 0):
                fimDeJogo = True
                print("Que pena! Voce perdeu!")
            while (not fimDeJogo):
                print("Turno:", turno)
                print("Quantas pecas voce gostaria de retirar?:")
                pecasRetiradas = int(input())
                print("Jogador retirou", pecasRetiradas, "peca(s)")
                nPecas = nPecas - pecasRetiradas
                print("Numero de pecas restantes =", nPecas)
                print("*****")
                turno += 1
                print("Turno:", turno)
                ehMultiplo = False
                temp = m
                while (not ehMultiplo):
                    if ((nPecas - temp) % (m+1) == 0):
                        pecasRetiradas = temp
                        ehMultiplo = True
                    else:
                        temp -= 1
                nPecas = nPecas - pecasRetiradas
                print("Computador retirou", pecasRetiradas, "peca(s)")
                print("Numero de pecas restantes =", nPecas)
                print("*****")
                turno += 1
                if (nPecas == 0):
                    fimDeJogo = True
                    print("Que pena! Voce perdeu!")

main()
