# módulo 'mostrar' usando a recursividade
def mostrar(n, i):
    if (i <= n):
        if (i == 1):
            print("{ ", end="")
        print(f"{i}", end=" ")
        i = i + 1
        mostrar(n, i)
    else:
        print("} ", end="")

# módulo 'somar' usando a recursividade
def somar(n, i):
    if (i <= n):
        novoI = i + 1
        return(i + somar(n, novoI))
    else:
        return(0)
# módulo 'resultados'
def resultados(n):
    mostrar(n, 1)
    print(f"soma = {somar(n, 1)}")
    print()

# módulo principal
resultados(5)
resultados(7)
