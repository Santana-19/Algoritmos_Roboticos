import numpy as np
import matplotlib.pyplot as plt

# Coeficientes de funcion de trasferencias
a0 = float(input("ingrese el valor de a0: "))
a1 = float(input("ingrese el valor de a1: "))
a2 = float(input("ingrese el valor de a2: "))
b1 = float(input("ingrese el valor de b1: "))
b2 = float(input("ingrese el valor de b2: "))

# tipo de sistema
s = np.roots([a2, a1, a0])
if np.min(np.abs(s)) < 1e-6:
    print("El sistemas es criticamente amortiguado.")
elif np.min(np.abs(s)) < 1:
    print("El sistema es subamortiguado.")
else:
    print("El sistema es sobreamortiguado.")

# calcular funcion de transferencia
def h(s):
    return a0 / (s**2 + b1 * s + b2)

# grafica
w = np.logspace(-2, 2, 1000)
mag, phase = np.abs(h(1j * w)), np.angle(h(1j * w))

plt.figure()
plt.semilogx(w, mag)
plt.title("Respuestas de magnitud")
plt.xlabel("Frecuencia (rad/s)")
plt.ylabel("Magnitudes")

plt.figure()
plt.semilogx(w, phase)
plt.title("Respuesta de la fase")
plt.xlabel("Frecuencia (rad/s)")
plt.ylabel("Fase (radians)")

plt.show()