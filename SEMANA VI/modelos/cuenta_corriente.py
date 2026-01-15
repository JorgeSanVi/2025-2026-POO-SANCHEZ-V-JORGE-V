from modelos.cuenta import Cuenta


class CuentaCorriente(Cuenta):
    # Clase derivada: hereda de Cuenta (herencia).
    # Polimorfismo: sobrescribo calcular_costo_mensual para cobrar mantenimiento.

    def __init__(self, titular: str, numero: str, saldo_inicial: float = 0.0, costo_mantenimiento: float = 2.50):
        super().__init__(titular, numero, saldo_inicial)
        self.costo_mantenimiento = costo_mantenimiento

    def calcular_costo_mensual(self) -> float:
        return self.costo_mantenimiento
