def matriz_I(n):
    i = 0
    while (i < n):
        j = 0
        while (j < n):
            print(f"{i}{j}", end=" ")
            j += 1
        print()
        i += 1

def matriz_II(n):
    for i in range(n+1):
        for j in range(n+1):
            print(f"{i}{j}", end=" ")
        print()

# módulo principal (main)
n = int(input("Tamanho da matriz? "))

print()
matriz_I(n)
print()
matriz_II(n)
print()
