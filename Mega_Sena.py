from random import randint

jogo = []

i = 1
while (i <= 6):
    nro = randint(1, 60)
    if (nro not in jogo):
        jogo.append(nro)
        i = i + 1
     
print(jogo)
jogo.sort()
print(jogo)
