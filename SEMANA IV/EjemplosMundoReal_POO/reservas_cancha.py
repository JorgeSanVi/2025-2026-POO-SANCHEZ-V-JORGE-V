# Ejemplo del mundo real: Sistema de reservas de una cancha
# Aplicación de Programación Orientada a Objetos (POO)

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Cancha:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = ["08:00", "10:00", "14:00"]

    def mostrar_horarios(self):
        return self.horarios

    def reservar(self, hora):
        if hora in self.horarios:
            self.horarios.remove(hora)
            return True
        return False


class Reserva:
    def __init__(self, cliente, cancha, hora):
        self.cliente = cliente
        self.cancha = cancha
        self.hora = hora


# --- PROGRAMA PRINCIPAL ---
cliente1 = Cliente("Jorge")
cancha1 = Cancha("Cancha Central")

print("=== SISTEMA DE RESERVAS ===")

reserva_confirmada = False

while not reserva_confirmada:
    print("Horarios disponibles:", cancha1.mostrar_horarios())
    hora = input("Ingrese la hora que desea reservar: ")

    if cancha1.reservar(hora):
        reserva = Reserva(cliente1, cancha1, hora)
        print(f"Reserva confirmada para {cliente1.nombre} a las {hora}")
        reserva_confirmada = True
    else:
        print("Horario no disponible, intente nuevamente.\n")
