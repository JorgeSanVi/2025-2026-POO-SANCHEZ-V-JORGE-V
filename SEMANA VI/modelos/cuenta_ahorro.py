# modelos/cuenta_ahorro.py

from modelos.cuenta import Cuenta


class CuentaAhorro(Cuenta):
    # Esta es una CLASE DERIVADA: hereda de Cuenta (HERENCIA).
    # Polimorfismo: sobrescribo calcular_costo_mensual con un comportamiento propio.

    def __init__(self, titular: str, numero: str, saldo_inicial: float = 0.0, tasa_interes: float = 0.02):
        super().__init__(titular, numero, saldo_inicial)
        self.tasa_interes = tasa_interes  # atributo propio de esta clase

    def calcular_costo_mensual(self) -> float:
        # En este ejemplo, la cuenta de ahorro no cobra mantenimiento.
        return 0.0

    def aplicar_interes(self) -> None:
        # Método propio: calcula interés y lo deposita usando el método encapsulado.
        interes = self.saldo * self.tasa_interes
        if interes > 0:
            self.depositar(interes)
