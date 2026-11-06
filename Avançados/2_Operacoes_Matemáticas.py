
from math import sqrt

def dobro(n):
    return(n * 2)

def triplo(n):
    return(n * 3)

def quadrado(n):
    return(n ** 2)

def cubo(n):
    return(n ** 3)

def raizQuadrada(n):
    return(sqrt(n))
def toString(n):
    result = f"Sendo n = {n}, tem-se:\n" + \
             f"Drobro = {dobro(n)}\n" + \
             f"Triplo = {triplo(n)}\n" + \
             f"Quadrado = {quadrado(n)}\n" + \
             f"Cubro = {cubo(n)}\n" + \
             f"Raiz Quadrada = {raizQuadrada(n):.4f}\n"

    return(result)

# módulo principal (main)
n = int(input("Digite um numero: "))

print()
print(toString(n))
