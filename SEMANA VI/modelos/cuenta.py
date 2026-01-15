class Cuenta:
    """
    Yo uso esta clase como base (clase padre).
    Aquí aplico encapsulación usando __saldo (atributo privado).
    """

    def __init__(self, titular: str, numero: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.numero = numero
        self.__saldo = 0.0
        self.depositar(saldo_inicial)

    @property
    def saldo(self) -> float:
        """Yo permito consultar el saldo sin modificarlo directamente."""
        return self.__saldo

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        self.__saldo += monto

    def retirar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes.")
        self.__saldo -= monto

    def calcular_costo_mensual(self) -> float:
        """
        Este método lo uso para polimorfismo.
        Cada clase derivada lo implementa de forma diferente.
        """
        return 0.0

    def __str__(self) -> str:
        return f"Cuenta({self.numero}) - Titular: {self.titular} - Saldo: ${self.saldo:.2f}"
