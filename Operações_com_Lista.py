
a = [int(item) for item in input().split(" ")]

print()
item = int(input("Item a ser procurado: "))

print()

print(a)
print("Soma  =", sum(a))
print("Média =", sum(a) / len(a))
print("Menor =", min(a))
print("Maior =", max(a))

print()
print(f"O item {item} existe {a.count(item)} vez(es) na lista.")


