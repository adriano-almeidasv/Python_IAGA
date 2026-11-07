
from random import randint
from Vetor import saida

while(True):
    n = int(input("Quantidade de cartões (no máximo 10, -1 para encerrar)? "))
    if (n == -1):
        break

    if ((n < 1) or (n > 10)):
        print(f"Erro: {n}, quantidade de cartões inválida!!!")
        print()
        continue    
    print()

    nos_Jogos = []
    for i in range(n):
        jogo = []
        j = 1
        while (j <= 6):
            nro = randint(1, 60)
            if (nro not in nos_Jogos):
                nos_Jogos.append(nro)
                jogo.append(nro)
                j += 1        
        print(saida(f"{i+1}o. jogo", sorted(jogo)))

    print()
