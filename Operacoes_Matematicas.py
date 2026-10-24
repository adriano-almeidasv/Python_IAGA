from math import sqrt

n = int(input("Digite o valor de n: "))

dobro = 2 * n
triplo = 3 * n
quadrado = n ** 2
cubo = n ** 3
raizQuadrada = sqrt(n)

print()
print(f"Sendo n = {n}, tem-se:")
print(f"Dobro = {dobro}")
print(f"Triplo = {triplo}")
print(f"Quadrado = {quadrado}")
print(f"Cubo = {cubo}")
print(f"Raiz Quadrada = {raizQuadrada:.4f}")
