
from Calculadora_IMC import toString
from Geral import cls, parada

meu_Paciente = {"paciente": "",
                "pc": 0.0,
                "alt": 0.0}
while(True):
    cls()

    meu_Paciente["paciente"] = input("Nome do Paciente (FIM para encerrar):\n")
    if (meu_Paciente["paciente"].upper() == "FIM"):
        break

    print()
    meu_Paciente["pc"] = float(input("Peso Corporal (em kgs): "))
    meu_Paciente["alt"] = float(input("Altura (em metros)....: "))

    print()
    print(toString(meu_Paciente["paciente"], meu_Paciente["pc"], meu_Paciente["alt"]))
    parada()
