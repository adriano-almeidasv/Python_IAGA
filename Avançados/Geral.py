
from os import system
from time import sleep

def cls():
    system('cls')

def delay(tmp): # tmp em segundos
    sleep(tmp)

def parada():
    print("\nPressione [ENTER] para prosseguir. ", end="")
    input()

def confirmou(rotulo):
    op = input(rotulo)
    if ((op == "S") or (op == "s")):
        return(True)
    else:
        return(False)

def linha(tipo="*", tam=10):
    result = ""
    for i in range(tam):
        result += tipo
    return(result)
