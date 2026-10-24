
# módulo 'mostrar'
def mostrar(n):
    print("{ ", end="")
    for i in range(1, n+1):
        print(f"{i}", end=" ")
    print("} ", end="")
# módulo 'somar'
def somar(n):
    soma = 0
    for i in range(1, n+1):
        soma = soma + i
    return(soma)
# módulo 'resultados'
def resultados(n):
    mostrar(n)
    print(f"soma = {somar(n)}")
    print()
# módulo principal
resultados(5)
resultados(7)
