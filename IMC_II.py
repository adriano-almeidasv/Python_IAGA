paciente = input("Nome do Paciente......: ")
pc = float(input("Peso Corporal (em kgs): "))
alt = float(input("Altura (em metros)....: "))

vlr_IMC = pc / (alt ** 2)

if (vlr_IMC < 18.5):
   interpretacao = "Magreza"
else:
   if (vlr_IMC < 25.0):
      interpretacao = "Normal"
   else:
      if (vlr_IMC < 30.0):
         interpretacao = "Sobrepeso"
      else:
         if (vlr_IMC < 40.0):
            interpretacao = "Obesidade"
         else:
            interpretacao = "Obesidade Grave"

print()
print(f"Nome do Paciente: {paciente}")
print(f"Peso Corporal...: {pc:.3f} kgs")
print(f"Altura..........: {alt:.2f} m")
print(f"IMC.............: {vlr_IMC:.2f} <<< {interpretacao} >>>")
