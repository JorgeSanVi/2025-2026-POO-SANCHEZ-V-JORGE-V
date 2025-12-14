# clima_tradicional.py
# Programa tradicional para calcular el promedio semanal del clima (7 días).

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def leer_temperatura(dia: str) -> float:
    """Pide y valida una temperatura numérica para un día."""
    while True:
        try:
            valor = float(input(f"Ingrese la temperatura de {dia} (°C): "))
            return valor
        except ValueError:
            print("Entrada inválida. Escriba un número, por ejemplo: 22.5")

def ingresar_temperaturas_semana() -> list[float]:
    """Guarda las temperaturas de los 7 días en una lista."""
    temps = []
    for dia in DIAS_SEMANA:
        temps.append(leer_temperatura(dia))
    return temps

def calcular_promedio(valores: list[float]) -> float:
    """Calcula el promedio de una lista de números."""
    if not valores:
        return 0.0
    return sum(valores) / len(valores)

def mostrar_resumen(temperaturas: list[float]) -> None:
    """Muestra temperaturas diarias y promedio final."""
    print("\n--- Resumen semanal ---")
    for dia, temp in zip(DIAS_SEMANA, temperaturas):
        print(f"{dia}: {temp:.2f} °C")
    promedio = calcular_promedio(temperaturas)
    print(f"\nPromedio semanal: {promedio:.2f} °C")

def main() -> None:
    print("Cálculo del promedio semanal del clima (Programación Tradicional)\n")
    temperaturas = ingresar_temperaturas_semana()
    mostrar_resumen(temperaturas)

if __name__ == "__main__":
    main()
