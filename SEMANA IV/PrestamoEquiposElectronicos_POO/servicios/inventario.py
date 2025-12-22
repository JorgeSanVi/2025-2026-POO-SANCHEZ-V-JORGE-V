class Inventario:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def listar_equipos(self):
        if not self.equipos:
            return "No hay equipos registrados."
        return "\n".join(str(equipo) for equipo in self.equipos)

    def prestar(self, codigo, usuario):
        for equipo in self.equipos:
            if equipo.codigo == codigo:
                if equipo.prestar():
                    return f"Equipo prestado a {usuario.nombre}"
                else:
                    return "El equipo ya está prestado"
        return "Equipo no encontrado"

    def devolver(self, codigo):
        for equipo in self.equipos:
            if equipo.codigo == codigo:
                if equipo.devolver():
                    return "Equipo devuelto correctamente"
                else:
                    return "El equipo no estaba prestado"
        return "Equipo no encontrado"
