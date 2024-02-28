# vectores
import numpy as np

x = [1,2,3]
y = [4,5,6]

suma = np.add (x, y)
resta = np.subtract(x, y)
punto = np.dot (x, y)
cruz = np.cross (x, y)
divicion = np.divide(x, y)

print ("La suma de los vectores es:", suma)
print ("La resta de los vectores es:", resta)
print ("El producto punto de los vectores es:", punto)
print ("El producto cruz de los vectores es:", cruz)
print ("La divicion de los vectores es:", divicion)