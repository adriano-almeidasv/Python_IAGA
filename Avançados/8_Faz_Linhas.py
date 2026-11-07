
def linha(tipo="*", tam=20):
    result = ""
    for i in range(tam):
        result = result + tipo

    return(result)

# módulo principal (main)
# por onde começa a execução desta estrutura modular
print(linha("*", 20))
print(linha())
print(linha(tipo="X"))
print(linha(tipo="@", tam=50))
print(linha("@", 50))
print(linha(tam=50))
print(linha("<<< ABC >>>", 5))

 #Vetor.py: arquivo de módulos com operações sobre vetores
def entrada(id, tam):
    x = []
    for i in range(tam):
        x.append(int(input(f"{i+1}o. valor, {id}[{i}] = ")))
    print()

    return(x)

def saida(id, x):
    tam = len(x)

    result = f"{id} = ["
    for i in range(tam):
        result += f"{x[i]}"
        if (i != (tam-1)):
            result += ", "

    result += "]"

    return(result)

def somar(x):
    return(sum(x))

def media(x):
    return(sum(x) / len(x))

def toString(id, x):
    result = saida(id, x) + \
             f"\n\nSoma dos Valores = {somar(x)}\n" + \
             f"Valor médio      = {media(x)}\n"

    return(result)
