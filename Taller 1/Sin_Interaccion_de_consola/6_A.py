#fuerza de avance y retroceso

import math

dc = 100
dv = 20
p = 6

#avance
area_c = math.pi * ((dc**2)/4)
area_a = area_c * (p/10)

#retroceso
area_v = math.pi*((dc**2 - dv**2) / 4)
area_r = area_v * (p/10)

print("La fuerza de avance es de:", round(area_a,2))
print("La fuerza de retroceso es de:", round(area_r,2))


