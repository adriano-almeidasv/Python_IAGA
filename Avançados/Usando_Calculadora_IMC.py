from Geral import confirmou, cls 
from Calculadora_IMC import toString

while True:
    paciente = input("Digite o nome do paciente: (ou <FIM> para encerrar) ")
    if paciente.upper() == "<FIM>":
        break
    pc = float(input("Digite o peso corporal (kgs): "))
    alt = float(input("Digite a altura (m): "))

    if confirmou("Deseja calcular o IMC do paciente? (S/N) "):
        from Calculadora_IMC import toString
        print(toString(paciente, pc, alt))

    print()