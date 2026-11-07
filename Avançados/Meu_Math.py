def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divInt(a, b):
    if b != 0:
        return a // b
    else:
        return 0

def divReal(a, b):
    if b != 0:
        return a / b
    else:
        return 0

def toString(a, b):
    result = (
        f"{a} + {b} = {soma(a, b)}\n"
        + f"{a} - {b} = {sub(a, b)}\n"
        + f"{a} x {b} = {mult(a, b)}\n"
        + f"{a} / {b} = {divInt(a, b)} divisão inteira\n"
        + f"{a} / {b} = {divReal(a, b):.2f} divisão real\n"
    )
    return result

def divisores(n):
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
    return div

def ehPrimo(n):
    return len(divisores(n)) == 2