paciente = input("Nome do Paciente......: ")
pc = float(input("Peso Corporal (em kgs): "))
alt = float(input("Altura (em metros)....: "))

vlr = pc / (alt ** 2)

if (vlr < 18.5):
    interpretacao = "Magreza"

if ((vlr >= 18.5) and (vlr < 25)):
    interpretacao = "Normal"

if ((vlr >= 25) and (vlr < 30)):
    interpretacao = "Sobrepeso"

if ((vlr >= 30) and (vlr < 40)):
    interpretacao = "Obesidade"

if (vlr >= 40):
    interpretacao = "Obesidade Grave"

print()     
print(f"Paciente: {paciente}")
print(f"Peso Corporal: {pc:.2f} kgs")
print(f"Altura: {alt:.2f} m")
print(f"IMC: {vlr:.2f}")
print(f"Interpretação: {interpretacao}")