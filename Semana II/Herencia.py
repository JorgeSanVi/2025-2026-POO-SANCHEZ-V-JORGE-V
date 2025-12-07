# EJEMPLO DE HERENCIA
# La clase Estudiante hereda atributos y métodos de Persona.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad}")


class Estudiante(Persona):  # Hereda de Persona
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_estudiante(self):
        self.mostrar_datos()
        print(f"Carrera: {self.carrera}")


# Bloque principal
if __name__ == "__main__":
    estudiante1 = Estudiante("Jorge", 33, "Ingeniería en TICs")
    estudiante1.mostrar_estudiante()
