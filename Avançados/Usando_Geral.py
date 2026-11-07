from random import randint
import Geral

for i in range(10):
    nro = randint(1, 100)
    print(f" {i+1}o. número: {nro} ")

    
    Geral.delay(1)
    print(Geral.linha())

print()
print("Fim do programa!!!")
Geral.parada()