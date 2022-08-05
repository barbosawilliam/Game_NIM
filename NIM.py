def main():
    print("[1]: jogador1 vs jogador2")
    print("[2]: jogador vs computador")
    modoDeJogo = int(input("Escolha o modo do jogo: "))
    while (modoDeJogo != 1 and modoDeJogo != 2):
        print("Modo inválido.")
        print("[1]: jogador1 vs jogador2")
        print("[2]: jogador vs computador")
        modoDeJogo = int(input("Escolha o modo do jogo: "))

    n = int(input("Entre com o numero de pecas (n): "))
    while (n < 1):
        print("O numero de pecas deve ser um numero inteiro.")
        n = int(input("Entre com o numero de pecas (n): "))
    print()

    m = int(input(f"Entre com o numero maximo de pecas que podem ser retiradas (m) (obs: 1 <= m <= {n}): "))
    while (m < 1 or m > n):
        print(f"Escolha inválida, o número maximo de pecas que podem ser retiradas deve estar no intervalo [1;{n}]")
        m = int(input(f"Entre com o numero maximo de pecas que podem ser retiradas (m) (obs: 1 <= m <= {n}): "))
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
            pecasRetiradas = int(input("Quantas pecas voce gostaria de retirar? "))
            
            while (pecasRetiradas < 1 or pecasRetiradas > m):
                print(f"Número inválido de peças! Você deve escolher um número do intervalo [1;{m}]")
                pecasRetiradas = int(input("Quantas pecas voce gostaria de retirar? "))

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
                pecasRetiradas = int(input("Quantas pecas voce gostaria de retirar? "))

                while (pecasRetiradas < 1 or pecasRetiradas > m):
                    print(f"Número inválido de peças! Você deve escolher um número do intervalo [1;{m}]")
                    pecasRetiradas = int(input("Quantas pecas voce gostaria de retirar? "))

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
                pecasRetiradas = int(input("Quantas pecas voce gostaria de retirar? "))
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
