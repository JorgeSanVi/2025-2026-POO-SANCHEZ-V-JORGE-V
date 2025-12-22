class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Usuario: {self.nombre} (CI: {self.cedula})"
