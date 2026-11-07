
def calcular_IMC(pc, alt):
    return(pc / (alt ** 2))

def interpretar_IMC(vlr_IMC):
    if (vlr_IMC < 18.5):
        return("Magreza")
    elif (vlr_IMC < 25.0):
        return("Normal")
    elif (vlr_IMC < 30.0):
        return("Sobrepeso")
    elif (vlr_IMC < 40.0):
        return("Obesidade")
    else:
        return("Obesidade Grave")

def toString(paciente, pc, alt):
    vlr_IMC = calcular_IMC(pc, alt)
    result = f"Nome do Paciente: {paciente}\n" + \
             f"Peso Corporal...: {pc:.3f} kgs\n" + \
             f"Altura..........: {alt:.2f} m\n" + \
             f"IMC.............: {vlr_IMC:.2f} <<< {interpretar_IMC(vlr_IMC)} >>>\n"
    return(result)
