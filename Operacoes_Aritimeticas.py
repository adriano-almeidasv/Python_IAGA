a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

soma = a + b
sub = a - b
mult = a * b
divInt = a // b
resto = a % b
divReal = a / b

print()
print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {sub}")
print(f"{a} x {b} = {mult}\n")
print(f"{a} // {b} = {divInt} divisão inteira")
print(f"{a} % {b} = {resto} resto da divisão inteira\n")
print(f"{a} / {b} = {divReal:.2f} divisão real")
