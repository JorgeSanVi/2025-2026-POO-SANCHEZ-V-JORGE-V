# main.py

from modelos.cuenta_ahorro import CuentaAhorro
from modelos.cuenta_corriente import CuentaCorriente
from servicios.banco_servicios import BancoServicio

# Aquí creo instancias (objetos) y demuestro el funcionamiento del sistema.

banco = BancoServicio()

# Instancias de clases derivadas (HERENCIA)
ahorro = CuentaAhorro(titular="Jorge Sanchez", numero="001", saldo_inicial=1000.0, tasa_interes=0.03)
corriente = CuentaCorriente(titular="Mishell Sarango", numero="002", saldo_inicial=800.0, costo_mantenimiento=2.50)

# Agrego objetos al sistema
banco.agregar_cuenta(ahorro)
banco.agregar_cuenta(corriente)

print("=== Estado inicial ===")
for c in banco.cuentas:
    print(c)

# Uso de métodos para operar el saldo (ENCAPSULACIÓN)
ahorro.depositar(220)
corriente.retirar(100)

# Transferencia entre cuentas
banco.transferir(numero_origen="001", numero_destino="002", monto=30)

# Método propio de la cuenta de ahorro
ahorro.aplicar_interes()

# Aplico costos mensuales usando POLIMORFISMO
banco.aplicar_costos_mensuales()

print("\n=== Estado final ===")
for c in banco.cuentas:
    print(c)

