from modelos.cuenta_ahorro import CuentaAhorro
from modelos.cuenta_corriente import CuentaCorriente
from servicios.banco_servicios import BancoServicio


banco = BancoServicio()

ahorro = CuentaAhorro(titular="Jorge V. Sanchez V.", numero="001", saldo_inicial=1000.0, tasa_interes=0.03)
corriente = CuentaCorriente(titular="Mishell C. Sarango ", numero="002", saldo_inicial=800.0, costo_mantenimiento=2.50)

banco.agregar_cuenta(ahorro)
banco.agregar_cuenta(corriente)

print("=== Estado inicial ===")
for c in banco.cuentas:
    print(c)

ahorro.depositar(220)
corriente.retirar(100)
banco.transferir("001", "002", 30)

ahorro.aplicar_interes()
banco.aplicar_costos_mensuales()

print("\n=== Estado final ===")
for c in banco.cuentas:
    print(c)
