
from Pessoa import Pessoa
from Calculadora_IMC import calcular_IMC, interpretar_IMC

class PacienteIMC(Pessoa):
  def __init__(self, nome, sexo, dtNasc, pc, alt):
    super().__init__(nome, sexo, dtNasc);
    self.pc = pc;
    self.alt = alt;

  def getPC(self):
    return self.pc

  def setPC(self, pc):
    self.pc = pc

  def getAlt(self):
    return self.alt

  def setAlt(self, alt):
    self.alt = alt

  def __str__(self):
    vlr_IMC = calcular_IMC(self.pc, self.alt)

    interpretacao = interpretar_IMC(vlr_IMC)
# trocando o '.' pela ',' na saída
    pc = f"{self.pc:.3f}".replace(".", ",")
    alt = f"{self.alt:.2f}".replace(".", ",")
    vlr_IMC = f"{vlr_IMC:.2f}".replace(".", ",")

    result = super().__str__() + \
               f"Peso......: {pc} kgs\n" + \
               f"Altura....: {alt} m\n" + \
               f"IMC.......: {vlr_IMC} <<< {interpretacao} >>>\n"  
    return(result)
