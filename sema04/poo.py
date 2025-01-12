# Clase CuentaBancaria que representa una cuenta bancaria con saldo y operaciones
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa la cuenta con un titular y un saldo inicial."""
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """Deposita una cantidad en la cuenta."""
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Has depositado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta si hay suficiente saldo."""
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Has retirado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")

    def mostrar_saldo(self):
        """Muestra el saldo actual de la cuenta."""
        print(f"Saldo actual de la cuenta de {self.titular}: {self.saldo}")


# Crear una cuenta bancaria
cuenta1 = CuentaBancaria("TANIA GUERRERO", 5400)

# Mostrar saldo inicial
cuenta1.mostrar_saldo()

# Realizar un depósito
cuenta1.depositar(800)

# Realizar un retiro
cuenta1.retirar(670)

# Mostrar el saldo final
cuenta1.mostrar_saldo()