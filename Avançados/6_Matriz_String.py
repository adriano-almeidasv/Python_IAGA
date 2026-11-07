def matriz_String(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1):
            print(f"{s[j]}", end=" ")
        print()

# módulo principal (main)
s = input("Informe uma String?\n")

print()

matriz_String(s)
