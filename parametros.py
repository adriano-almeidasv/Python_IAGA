def digaOla():
   print("Olá")

def digaOlaPara(nome):
   print("Olá Sr(a).", nome)

def boasVindas(nome, sexo):
   if (sexo == 'm') or (sexo == 'M'):
      print("Seja bem-vindo Sr.", nome)
   else:
      print("Seja bem-vinda Sra.", nome)
# módulo principal
digaOla()
print()
digaOlaPara("Juca Bala")
print()
boasVindas("Juca Bala", "M")
boasVindas("Maria do Socorro", "F")
