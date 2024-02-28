# Matrices
import numpy as np

x = ([1,2,3],[4,5,6],[7,8,9])
y = ([9,8,7],[6,5,4],[3,2,1])

suma = np.add (x, y)
resta = np.subtract (x, y)
punto = np.dot (x, y)
cruz = np.cross (x, y)
divicion = np.divide (x, y)

print("La suma de la matrices es:\n", suma)
print("La resta de la matrices es:\n", resta)
print("El producto punto de la matrices es:\n", punto)
print("El producto cruz de la matrices es:\n", cruz)
print("La divicion de la matrices es:\n", divicion)