
def separa(a):
    pares = []
    impares = []
    
    for i in range(len(a)):
        if ((a[i] % 2) == 0):
            pares.append(a[i])
        else:
            impares.append(a[i])
            
    return(pares, impares)

# módulo principal
x = [7, 1, 4, 3, 7, 8]

a, b = separa(x)

print(x)
print(a)
print(b)



