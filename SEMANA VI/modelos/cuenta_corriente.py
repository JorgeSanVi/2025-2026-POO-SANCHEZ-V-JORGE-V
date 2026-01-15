from modelos.cuenta import Cuenta


class CuentaCorriente(Cuenta):
    """
    Yo heredo de Cuenta (herencia) y sobrescribo un método (polimorfismo).
    """

    def __init__(self, titular: str, numero: str, saldo_inicial: float = 0.0, costo_mantenimiento: float = 2.50):
        super().__init__(titular, numero, saldo_inicial)
        self.costo_mantenimiento = costo_mantenimiento

    def calcular_costo_mensual(self) -> float:
        """En corriente yo sí cobro mantenimiento."""
        return self.costo_mantenimiento
