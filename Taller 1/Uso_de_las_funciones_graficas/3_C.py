#Carga y Descarga
import numpy as np
import matplotlib.pyplot as plt

# Función para resolver la EDO
def solve_rc_circuit(V, R, C, t_end):
    # Constante de tiempo
    τ = R * C
    # Ecuación diferencial de primer orden
    def dV_dt(t, V):
        return -(1/τ) * V + (1/τ) * I(t)
    # Condición inicial
    V0 = V
    # Resolver la EDO
    t = np.linspace(0, t_end, 1000)
    V = np.zeros(t.shape)
    V[0] = V0
    for i in range(1, len(t)):
        V[i] = V[i-1] + (dV_dt(t[i-1], V[i-1]) - (1/τ) * V[i-1]) * (t[i] - t[i-1])
    return t, V

# Función para calcular la corriente
def I(t):
    if t < 0:
        return 0
    elif t < 1:
        return t
    else:
        return 1

# Solicitar valores por teclado
V = float(input("Ingrese el voltaje (V): "))
R = float(input("Ingrese la resistencia (Ω): "))
C = float(input("Ingrese la capacitancia (μF): "))
t_end = float(input("Ingrese el tiempo final (s): "))

# Resolver la EDO y graficar
t, V = solve_rc_circuit(V, R, C, t_end)
plt.plot(t, V)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.title('Comportamiento del circuito RC')
plt.show()