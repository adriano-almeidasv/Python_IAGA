
from Ponto import Ponto
from Geral import cls

cls()

n = int(input("Quantos pontos serão informados? "))

pontos = []

for i in range(n):
    print()
    print(f"{i+1}o. ponto:")

    x = int(input("Coordenada 'x': "))
    y = int(input("Coordenada 'y': "))

    p = Ponto(x, y)
    pontos.append(p)

print()
for i in range(n):
    print(f"{i+1}o. ponto: {pontos[i]}")
