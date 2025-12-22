class Equipo:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.prestado = False

    def prestar(self):
        if self.prestado:
            return False
        self.prestado = True
        return True

    def devolver(self):
        if not self.prestado:
            return False
        self.prestado = False
        return True

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.nombre} (Código: {self.codigo}) - {estado}"
