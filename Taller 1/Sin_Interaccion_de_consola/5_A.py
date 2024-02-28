import numpy as np

def rotacion_x(angulo: float, matriz: np.ndarray) -> np.ndarray:

    cosa = np.cos(angulo)
    sina = np.sin(angulo)

    rotar_x = np.array([
        [1, 0, 0],
        [0, cosa, -sina],
        [0, sina, cosa]
    ])

    return np.dot(rotar_x, matriz)

def rotacion_y(angulo: float, matriz: np.ndarray) -> np.ndarray:

    cosa = np.cos(angulo)
    sina = np.sin(angulo)

    rotar_y = np.array([
        [cosa, 0, sina],
        [0, 1, 0],
        [-sina, 0, cosa]
    ])

    return np.dot(rotar_y, matriz)

def rotacion_z(angulo: float, matriz: np.ndarray) -> np.ndarray:
    
    cosa = np.cos(angulo)
    sina = np.sin(angulo)

    rotar_z = np.array([
        [cosa, -sina, 0],
        [sina, cosa, 0],
        [0, 0, 1]
    ])

    return np.dot(rotar_z, matriz)

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

angulo = np.pi/2  

rotacion = rotacion_x(angulo, matriz)
rotacion = rotacion_y(angulo, matriz)
rotacion = rotacion_z(angulo, matriz)
print(rotacion)