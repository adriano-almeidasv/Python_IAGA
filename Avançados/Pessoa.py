from Data import Data

class Pessoa:
  def __init__(self, nome, sexo, dtNasc):
    self.nome = nome
    self.sexo = sexo
    self.dtNasc = dtNasc

  def getNome(self):
    return self.nome

  def setNome(self, nome):
    self.nome = nome

  def getSexo(self):
    return self.sexo

  def setSexo(self, sexo):
    self.sexo = sexo

  def getDtNasc(self):
    return self.dtNasc

  def setDtNasc(self, dtNasc):
    self.dtNasc = dtNasc

  def __str__(self):   
    result = f"Nome......: {self.nome}\n" + \
             f"Sexo......: {self.sexo}\n" + \
             f"Nascimento: {self.dtNasc.toString(True)}\n"
    
    return(result)
