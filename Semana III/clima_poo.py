# clima_poo.py
# Programa POO para calcular el promedio semanal del clima (7 días).
# Incluye encapsulamiento (atributos protegidos) y herencia (clase base).

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

class DiaBase:
    """Clase base (herencia): representa un día con su nombre."""
    def __init__(self, nombre: str):
        self._nombre = nombre  # Encapsulamiento: atributo protegido

    def get_nombre(self) -> str:
        return self._nombre

class DiaClima(DiaBase):
    """Clase hija: día + temperatura."""
    def __init__(self, nombre: str, temperatura: float):
        super().__init__(nombre)
        self._temperatura = temperatura  # Encapsulamiento

    def get_temperatura(self) -> float:
        return self._temperatura

class RegistroClima:
    """Administra los datos de la semana y calcula el promedio."""
    def __init__(self):
        self._dias: list[DiaClima] = []  # Encapsulamiento

    def agregar_dia(self, dia: DiaClima) -> None:
        self._dias.append(dia)

    def promedio_semanal(self) -> float:
        if not self._dias:
            return 0.0
        total = sum(d.get_temperatura() for d in self._dias)
        return total / len(self._dias)

    def mostrar_resumen(self) -> None:
        print("\n--- Resumen semanal ---")
        for d in self._dias:
            print(f"{d.get_nombre()}: {d.get_temperatura():.2f} °C")
        print(f"\nPromedio semanal: {self.promedio_semanal():.2f} °C")

def leer_float(mensaje: str) -> float:
    """Función de apoyo para validar entrada numérica."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Escriba un número, por ejemplo: 22.5")

def main() -> None:
    print("Cálculo del promedio semanal del clima (POO)\n")

    registro = RegistroClima()

    for nombre_dia in DIAS_SEMANA:
        temp = leer_float(f"Ingrese la temperatura de {nombre_dia} (°C): ")
        registro.agregar_dia(DiaClima(nombre_dia, temp))

    registro.mostrar_resumen()

if __name__ == "__main__":
    main()
