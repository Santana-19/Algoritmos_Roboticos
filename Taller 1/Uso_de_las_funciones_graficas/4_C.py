# Grafica vector 3d
import matplotlib.pyplot as plt
import numpy as np

x = float(input("introdusca la posicion del vector en X: "))
y = float(input("introdusca la posicion del vector en Y: "))
z = float(input("introdusca la posicion del vector en Z: "))

# Sistema de coordenadas en 3D
ax = plt.axes(projection='3d')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# dibujar origen con los ejes
ax.plot([0, 1], [0, 0], [0, 0], 'r--', label='Eje X')
ax.plot([0, 0], [0, 1], [0, 0], 'g--', label='Eje Y')
ax.plot([0, 0], [0, 0], [0, 1], 'b--', label='Eje Z')

# dibujar vector 
ax.quiver(0, 0, 0, x, y, z, color='red', label='Vector r')
ax.legend()
plt.show()