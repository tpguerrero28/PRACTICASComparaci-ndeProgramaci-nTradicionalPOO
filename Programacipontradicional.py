# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Solicitar 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Programa para calcular el promedio semanal del clima.")
    temperaturas = ingresar_temperaturas()  # Ingresar las temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcular el promedio
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Llamar a la función principal
if __name__ == "__main__":
    main()