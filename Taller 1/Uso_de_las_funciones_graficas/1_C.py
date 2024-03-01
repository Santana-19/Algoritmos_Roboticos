# Grafica de PT100

import numpy as np
import matplotlib.pyplot as plt

constante_pt100 = 0.385

temperatura = np.arange(-200, 200)

resistances = constante_pt100 * temperatura + 100

plt.figure(figsize=(10, 5))
plt.plot(temperatura, resistances, label="PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (ohms)")
plt.title('Comportamiento de un sensor PT100 (-200°C a 200°C)')
plt.grid(True)
plt.show()