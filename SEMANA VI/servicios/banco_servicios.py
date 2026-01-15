from modelos.cuenta import Cuenta


class BancoServicio:
    # Lógica del sistema (servicios). Administro cuentas y operaciones.

    def __init__(self):
        self.cuentas: list[Cuenta] = []

    def agregar_cuenta(self, cuenta: Cuenta) -> None:
        # Agrego cuentas y valido que no se repitan por número.
        if self.buscar_cuenta(cuenta.numero) is not None:
            raise ValueError("Ya existe una cuenta con ese número.")
        self.cuentas.append(cuenta)

    def buscar_cuenta(self, numero: str) -> Cuenta | None:
        # Busco una cuenta por su número.
        for c in self.cuentas:
            if c.numero == numero:
                return c
        return None

    def transferir(self, numero_origen: str, numero_destino: str, monto: float) -> None:
        # Transferencia usando métodos públicos (respeta la encapsulación del saldo).
        origen = self.buscar_cuenta(numero_origen)
        destino = self.buscar_cuenta(numero_destino)

        if origen is None or destino is None:
            raise ValueError("Cuenta de origen o destino no existe.")

        origen.retirar(monto)
        destino.depositar(monto)

    def aplicar_costos_mensuales(self) -> None:
        # Polimorfismo: cada cuenta calcula el costo según su tipo.
        for cuenta in self.cuentas:
            costo = cuenta.calcular_costo_mensual()
            if costo > 0:
                cuenta.retirar(costo)
