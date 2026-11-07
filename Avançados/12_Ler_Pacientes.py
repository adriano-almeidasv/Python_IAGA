from pathlib import Path

import Calculadora_IMC

arquivo = Path(__file__).with_name("pacientes.txt")

with arquivo.open("r", encoding="utf-8") as pacientes:
    for numero_linha, linha in enumerate(pacientes, start=1):
        if not linha.strip():
            continue

        partes = [parte.strip() for parte in linha.split(";")]
        if len(partes) != 3:
            raise ValueError(
                f"Formato inválido na linha {numero_linha} de {arquivo.name}: "
                "esperado nome; peso; altura."
            )

        paciente = partes[0]
        try:
            pc = float(partes[1])
            alt = float(partes[2])
        except ValueError as erro:
            raise ValueError(
                f"Peso ou altura inválido na linha {numero_linha} de {arquivo.name}."
            ) from erro

        print(Calculadora_IMC.toString(paciente, pc, alt))
