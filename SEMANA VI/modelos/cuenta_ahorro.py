from modelos.cuenta import Cuenta


class CuentaAhorro(Cuenta):
    """
    Yo heredo de Cuenta (herencia) y sobrescribo un método (polimorfismo).
    """

    def __init__(self, titular: str, numero: str, saldo_inicial: float = 0.0, tasa_interes: float = 0.02):
        super().__init__(titular, numero, saldo_inicial)
        self.tasa_interes = tasa_interes

    def calcular_costo_mensual(self) -> float:
        """En ahorro yo no cobro mantenimiento (ejemplo)."""
        return 0.0

    def aplicar_interes(self) -> None:
        """Método propio de esta clase."""
        interes = self.saldo * self.tasa_interes
        if interes > 0:
            self.depositar(interes)
