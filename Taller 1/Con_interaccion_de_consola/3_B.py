# Volumenes

import math

print("ingresa el salido que deseas evaluar")

while opcion:

    opcion = input("Seleccione para calcular el volumen\n1. Prisma\n2. Pirámide\n3. Cono truncado\n4. Cilindro\nSolido: ")

    if opcion == "1":

        b = float(input("Ingrese el valor de la base: "))
        a = float(input("Ingrese el valor de la altura: "))
        v = b * a
        print(f"El volumen del solido prisma es: {v:.2f}")

    if opcion == "2":

        b = float(input("Ingrese el valor de la base: "))
        a = float(input("Ingrese el valor de la altura: "))
        v = (1/3) * b * a
        print(f"El volumen de la pirámide es: {v:.2f}")

    if opcion == "3":

        r = float(input("Ingrese el valor del radio: "))
        a = float(input("Ingrese el valor de la altura: "))
        r2 = float(input("Ingrese el radio menor del cono truncado: "))
        v = (math.pi * a / 3) * (r*2 + r2*2 + (r * r2))
        print(f"El volumen del cono truncado es: {v:.2f}")

    if opcion  == "4":

        r = float(input("Ingrese el valor del radio: "))
        a = float(input("Ingrese el valor de la altura: "))
        v = math.pi * r**2 * a
        print(f"El volumen del cilindro es: {v:.2f}")



