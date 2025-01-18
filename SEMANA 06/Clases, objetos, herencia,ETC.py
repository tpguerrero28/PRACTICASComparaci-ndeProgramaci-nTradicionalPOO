# Clase base (clase)
class Vehiculo:
    def __init__(self, marca, modelo):
        # Atributos protegidos
        self._marca = marca
        self._modelo = modelo

    # Método para mostrar información del vehículo
    def informacion(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}"

    # Método general para arrancar el vehículo
    def arrancar(self):
        print(f"El vehículo {self._marca} {self._modelo} está arrancando...")


# Clase derivada (Clase Hija) que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self._puertas = puertas

    # Sobrescritura del método arrancar (Polimorfismo)
    def arrancar(self):
        print(f"El coche {self._marca} {self._modelo} con {self._puertas} puertas está arrancando...")


# Clase derivada (Clase Hija) que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self._tipo = tipo

    # Sobrescritura del método arrancar (Polimorfismo)
    def arrancar(self):
        print(f"La motocicleta {self._marca} {self._modelo} tipo {self._tipo} está arrancando...")


# Clase para manejar una flota de vehículos
class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def arrancar_vehiculos(self):
        for vehiculo in self.vehiculos:
            vehiculo.arrancar()  # Polimorfismo: se invoca el método adecuado dependiendo del tipo de vehículo


# Crear instancias de las clases
coche = Coche("RENAULD", "SANDERO", 4)
motocicleta = Motocicleta("DAYTONA", "GTR 200 CC", "DEPORTIVA")

# Crear una flota y agregar vehículos
flota = Flota()
flota.agregar_vehiculo(coche)
flota.agregar_vehiculo(motocicleta)

# Mostrar la información de los vehículos
print(coche.informacion())
print(motocicleta.informacion())

# Arrancar todos los vehículos en la flota
flota.arrancar_vehiculos()