
def tabuada_I(n):
    i = 1
    while (i <= 10):
        print(f"{n} x {i} = {n*i}")
        i += 1

    print()

def tabuada_II(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# módulo principal (main)
while (True):
    n = int(input("De 0 até 10, -1 para encerrar. Tabuada do "))
    if (n == -1):
        break

    if ((n < 0) or (n > 10)):
        print("<<< Erro: forneça um valor de 0 até 10!!! >>>\n")
    else:
        print()
        tabuada_I(n)
        tabuada_II(n)

print("<<< FIM DO PROGRAMA >>>\n")
