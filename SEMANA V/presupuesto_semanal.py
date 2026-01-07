# Programa: Presupuesto semanal (registro básico)
# Descripción: Registro un ingreso semanal y varios gastos. Luego calculo el total gastado,
# el saldo restante y muestro alertas según el porcentaje gastado y si existe déficit.
# Tipos de datos usados: str, int, float, bool.

def solicitar_float(mensaje):
    # Pido un número decimal y valido la entrada para evitar errores.
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Entrada no válida. Ingresa un número (ejemplo: 10.50).")


def solicitar_int(mensaje):
    # Pido un número entero y valido la entrada.
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Entrada no válida. Ingresa un número entero (ejemplo: 3).")


def solicitar_si_no(mensaje):
    # Convierto una respuesta sí/no a un valor booleano (True/False).
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Respuesta no válida. Escribe 's' para sí o 'n' para no.")


def registrar_gastos(cantidad_gastos):
    # Registro gastos como una lista de tuplas: (descripcion, monto, es_necesario).
    gastos = []

    for i in range(1, cantidad_gastos + 1):
        print(f"\nGasto #{i}")
        descripcion = input("Descripción del gasto: ").strip()  # str
        monto = solicitar_float("Monto del gasto ($): ")        # float
        es_necesario = solicitar_si_no("¿Es un gasto necesario? (s/n): ")  # bool

        gastos.append((descripcion, monto, es_necesario))

    return gastos


def calcular_resumen(ingreso_semanal, gastos):
    # Calculo total gastado, total necesario, saldo restante y porcentaje gastado.
    total_gastado = 0.0
    total_necesario = 0.0

    for descripcion, monto, es_necesario in gastos:
        total_gastado += monto
        if es_necesario:
            total_necesario += monto

    saldo_restante = ingreso_semanal - total_gastado

    # Si el ingreso es 0, evito dividir para no generar error.
    if ingreso_semanal > 0:
        porcentaje_gastado = (total_gastado / ingreso_semanal) * 100
    else:
        porcentaje_gastado = 0.0

    return total_gastado, total_necesario, saldo_restante, porcentaje_gastado


def main():
    print("=== Presupuesto semanal ===")

    nombre_usuario = input("Ingresa tu nombre: ").strip()  # str
    ingreso_semanal = solicitar_float("Ingresa tu ingreso semanal ($): ")  # float
    cantidad_gastos = solicitar_int("¿Cuántos gastos vas a registrar?: ")  # int

    gastos = registrar_gastos(cantidad_gastos)

    total_gastado, total_necesario, saldo_restante, porcentaje_gastado = calcular_resumen(
        ingreso_semanal, gastos
    )

    # Alertas separadas para que no se mezclen los mensajes.
    supera_limite = porcentaje_gastado >= 80  # bool
    esta_en_deficit = saldo_restante < 0      # bool

    print("\n=== Resumen ===")
    print(f"Usuario: {nombre_usuario}")
    print(f"Ingreso semanal:   ${ingreso_semanal:.2f}")
    print(f"Total gastado:     ${total_gastado:.2f}")
    print(f"Gasto necesario:   ${total_necesario:.2f}")
    print(f"Saldo restante:    ${saldo_restante:.2f}")
    print(f"Porcentaje gastado: {porcentaje_gastado:.1f}%")

    if supera_limite:
        print("Alerta: Estás gastando el 80% o más de tu ingreso semanal.")
    else:
        print("Resultado: Tu gasto está por debajo del 80% del ingreso semanal.")

    if esta_en_deficit:
        print("Observación: Estás en déficit (gastaste más de lo que ingresaste).")
    else:
        print("Observación: No estás en déficit (tu saldo es positivo o cero).")

    print("Fin del programa.")


main()


