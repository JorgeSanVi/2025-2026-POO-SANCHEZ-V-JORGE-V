# modelos/cuenta_corriente.py

from modelos.cuenta import Cuenta


class CuentaCorriente(Cuenta):
    # CLASE DERIVADA: hereda de Cuenta (HERENCIA).
    # Polimorfismo: aquí el costo mensual sí existe y cambia según el tipo de cuenta.

    def __init__(self, titular: str, numero: str, saldo_inicial: float = 0.0, costo_mantenimiento: float = 2.50):
        super().__init__(titular, numero, saldo_inicial)
        self.costo_mantenimiento = costo_mantenimiento  # atributo propio

    def calcular_costo_mensual(self) -> float:
        # En cuenta corriente sí se cobra mantenimiento.
        return self.costo_mantenimiento
