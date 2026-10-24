while True:
   s = input("Informe uma String (FIM para encerrar)?\n")
   if (s.upper() == "FIM"):
      break

   print()

   for i in range(len(s)):
      for j in range(i+1):
         print(s[j], end="|")
      print()

   print()
