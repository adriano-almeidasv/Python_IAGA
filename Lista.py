n = int(input("Tamanho da Lista? "))

print()

soma = 0
l = []
for i in range(n):
    item = int(input(f"{i+1}o. item da lista: "))
    
    soma = soma + item
    l.append(item)

print()

# 1a. forma: print da lista
print(l, "soma =", soma)

# 2a. forma: item por item (for each)
for item in l:
    print(item, end=", ")
print("soma = ", soma)

# 3a. forma: com acesso indexado
print("[", end="")
for i in range(len(l)):
    print(f"{l[i]}", end="")
    if (i != len(l)-1): # não é o último item
        print(", ", end="")
print("] soma =", soma)
