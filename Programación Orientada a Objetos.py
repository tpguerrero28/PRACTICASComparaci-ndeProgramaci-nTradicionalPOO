class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas

    # Método para ingresar las temperaturas de los 7 días
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio de las temperaturas
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método para mostrar el promedio semanal
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Función principal
def main():
    print("Programa orientado a objetos para calcular el promedio semanal del clima.")
    clima = ClimaSemanal()  # Crear una instancia de la clase ClimaSemanal
    clima.ingresar_temperaturas()  # Ingresar las temperaturas
    clima.mostrar_promedio()  # Mostrar el promedio semanal

# Llamar a la función principal
if __name__ == "__main__":
    main()