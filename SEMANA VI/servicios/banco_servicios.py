from modelos.cuenta import Cuenta


class BancoServicio:
    """
    Yo separo la lógica del sistema en la carpeta servicios.
    """

    def __init__(self):
        self.cuentas: list[Cuenta] = []

    def agregar_cuenta(self, cuenta: Cuenta) -> None:
        if self.buscar_cuenta(cuenta.numero) is not None:
            raise ValueError("Ya existe una cuenta con ese número.")
        self.cuentas.append(cuenta)

    def buscar_cuenta(self, numero: str) -> Cuenta | None:
        for c in self.cuentas:
            if c.numero == numero:
                return c
        return None

    def transferir(self, numero_origen: str, numero_destino: str, monto: float) -> None:
        origen = self.buscar_cuenta(numero_origen)
        destino = self.buscar_cuenta(numero_destino)

        if origen is None or destino is None:
            raise ValueError("Cuenta de origen o destino no existe.")

        origen.retirar(monto)
        destino.depositar(monto)

    def aplicar_costos_mensuales(self) -> None:
        """
        Aquí demuestro polimorfismo:
        recorro cuentas y uso calcular_costo_mensual(),
        pero cada tipo de cuenta lo calcula distinto.
        """
        for cuenta in self.cuentas:
            costo = cuenta.calcular_costo_mensual()
            if costo > 0:
                cuenta.retirar(costo)
