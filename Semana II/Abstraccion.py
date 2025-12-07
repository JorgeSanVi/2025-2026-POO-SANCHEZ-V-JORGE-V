# EJEMPLO DE ABSTRACCIÓN
# Mostramos solo la información esencial de un usuario.

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo  # dato esencial

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} - Correo: {self.correo}")


# Bloque para ejecutar el ejemplo
if __name__ == "__main__":
    usuario1 = Usuario(nombre="Jorge", correo="jv.sanchezv@uea.edu.ec")
    usuario1.mostrar_info()

