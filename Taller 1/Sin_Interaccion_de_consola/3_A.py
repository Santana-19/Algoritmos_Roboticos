# convercion de coordenadas rectangulares a cilindricas
# convercion de coordenadas rectangulares a esfericas

import math

def rectangular_a_cilindricas(x, y, z):
    r = math.sqrt(x**2 + y**2)
    tan_theta = y / x
    z = z
    return round(r,2), round(tan_theta,2), z

def rectangulares_a_esfericas (x, y, z):
    rho = math.sqrt(x**2 + y**2 + z**2)
    tan_theta = math.atan2(y, x)
    phi = math.acos(z / rho)
    return round(rho,2),round(tan_theta,2), round(phi,2)

x, y, z = 7, 14, 8
coor_cil = rectangular_a_cilindricas (x, y, z)
coor_esf = rectangulares_a_esfericas (x, y, z)
print(f"Coordenades Cilindricas",coor_cil)
print(f"Coordenadas Esfericas",coor_esf)