class Calculadora:
    # Constructor (__init__) - Inicializa los números con los que se trabajará
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Calculadora creada con los números {self.num1} y {self.num2}.")

    #  multiplicación
    def multiplicar(self):
        resultado = self.num1 * self.num2
        print(f"El resultado de la multiplicación es: {resultado}")
        return resultado

    #  división
    def dividir(self):
        if self.num2 != 0:
            resultado = self.num1 / self.num2
            print(f"El resultado de la división es: {resultado}")
            return resultado
        else:
            print("Error: No se puede dividir por cero.")
            return None

    # Destructor (__del__) - Se llama cuando el objeto se elimina
    def __del__(self):
        print(f"El objeto de la calculadora con los números {self.num1} y {self.num2} ha sido destruido.")

# Crear un objeto de la clase Calculadora
calculadora = Calculadora(25, 15)

# Realizar operaciones de multiplicación y división
calculadora.multiplicar()  # Resultado de la multiplicación
calculadora.dividir()      # Resultado de la división

# Eliminar el objeto manualmente para llamar al destructor
del calculadora