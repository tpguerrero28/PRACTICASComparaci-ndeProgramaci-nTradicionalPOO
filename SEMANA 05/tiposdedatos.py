# Este programa calcula el área de un círculo y realiza conversiones de unidades.

import math

def calcular_area_circulo(radio):
    """
    Esta función recibe el radio de un círculo y devuelve el área.
    :param radio: El radio del círculo (float)
    :return: El área del círculo (float)
    """
    area = math.pi * radio ** 2
    return area

def convertir_a_pulgadas(metros):
    """
    Convierte una medida en metros a pulgadas.
    :param metros: Distancia en metros (float)
    :return: Distancia en pulgadas (float)
    """
    pulgadas = metros * 39.3701
    return pulgadas

# Datos de entrada
radio = float(input("Ingresa el radio del círculo en metros: "))
metros = float(input("Ingresa la longitud en metros para convertir a pulgadas: "))

# Cálculo del área
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados.")

# Conversión de unidades
pulgadas = convertir_a_pulgadas(metros)
print(f"{metros} metros son equivalentes a {pulgadas:.2f} pulgadas.")