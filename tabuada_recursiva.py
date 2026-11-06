def tabuada(n, i):
    if (i <= 10):
       print(f"{n} x {i} = {n*i}")
       i = i + 1
       tabuada(n, i)
    else:
       print()
# módulo principal
tabuada(5, 1)
tabuada(7, 1)
tabuada(9, 1)
