# numero random
import random
#descricpion
x = int(input("Cantidad de numeros a generar:"))
min = int(input("Rango minímo: "))
max = int(input("Rango máximo: "))

for _ in range(x):
    print(f"Números random:", random.randint (min, max))