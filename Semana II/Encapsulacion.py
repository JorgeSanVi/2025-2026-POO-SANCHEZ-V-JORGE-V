# EJEMPLO DE ENCAPSULACIÓN
# Ocultamos el saldo y lo modificamos usando métodos.

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido.")
        elif monto > self.__saldo:
            print("Fondos insuficientes.")
        else:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo restante: ${self.__saldo}")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: ${self.__saldo}")


# Bloque para ejecutar el ejemplo
if __name__ == "__main__":
    cuenta = CuentaBancaria(titular="Jorge", saldo_inicial=100)
    cuenta.mostrar_saldo()
    cuenta.depositar(50)
    cuenta.retirar(30)
    cuenta.retirar(500)
