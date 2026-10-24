
def menor(a, b):
    if (a <= b):
        return(a)
    else:
        return(b)
    
def maior(a, b):
    if (a >= b):
        return(a)
    else:
        return(b)

def menor_maior(a, b):
    if (a <= b):
        return(a, b)
    else:
        return(b, a)
        
def mostrar(a, b):
    print("Menor =", a)
    print("Maior =", b)

# módulo principal (main)
a = menor(1, 11)
b = maior(1, 11)
mostrar(a, b)
print()

a, b = menor_maior(1, 11)
mostrar(a, b)
print()

