#dibujar nombre
import matplotlib.pyplot as plt

letra_S = [[1, 0.1], [1, 0], [3, 0], [3, 0.5], [1, 0.5], [1, 1], [3, 1], [3, 0.9]]
letra_T = [[4, 1], [6, 1], [5, 1], [5,0]]
letra_E = [[9, 1], [7, 1], [7, 0.5], [9, 0.5], [7, 0.5], [7, 0], [9, 0]]
letra_V = [[10, 1], [11, 0], [12, 1]]
letra_E2 = [[15, 1], [13, 1], [13, 0.5], [15, 0.5], [13, 0.5], [13, 0], [15, 0]]
letra_N = [[16, 0], [16, 1], [18, 0], [18, 1]]

letra_J = [[20, 1], [22, 1], [21, 1], [21, 0], [20, 0], [20, 0.2]]
letra_U = [[23, 1], [23, 0], [25, 0], [25, 1]]
letra_A = [[26, 0], [26, 0.5], [27, 1], [28, 0.5],[26, 0.5], [28, 0.5], [28, 0]]
letra_N2 = [[29, 0], [29, 1], [31, 0], [31, 1]]
# Unir los puntos de cada letra
for letra in [letra_S, letra_T, letra_E, letra_V, letra_E2, letra_N, letra_J, letra_U, letra_A, letra_N2]:
    x = [punto[0] for punto in letra]
    y = [punto[1] for punto in letra]
    plt.plot(x, y, marker='o')

# Configuraciones adicionales
plt.title("NOMBRES")
plt.grid(True)
plt.show()
