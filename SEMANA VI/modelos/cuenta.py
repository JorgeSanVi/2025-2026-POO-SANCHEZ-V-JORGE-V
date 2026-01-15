class Cuenta:
    # Clase base (padre). De aquí heredan otras cuentas.
    # Encapsulación: el saldo se protege con __saldo (atributo privado).

    def __init__(self, titular: str, numero: str, saldo_inicial: float = 0.0):
        # Atributos públicos
        self.titular = titular
        self.numero = numero

        # Atributo privado (encapsulado)
        self.__saldo = 0.0

        # Mantengo control del saldo desde el inicio usando un método
        self.depositar(saldo_inicial)

    @property
    def saldo(self) -> float:
        # Permito consultar el saldo, pero no modificarlo directamente.
        return self.__saldo

    def depositar(self, monto: float) -> None:
        # Método para aumentar saldo de forma controlada
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        self.__saldo += monto

    def retirar(self, monto: float) -> None:
        # Método para disminuir saldo de forma controlada
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes.")
        self.__saldo -= monto

    def calcular_costo_mensual(self) -> float:
        # Polimorfismo: las clases derivadas sobrescriben este método.
        return 0.0

    def __str__(self) -> str:
        return f"Cuenta({self.numero}) - Titular: {self.titular} - Saldo: ${self.saldo:.2f}"

