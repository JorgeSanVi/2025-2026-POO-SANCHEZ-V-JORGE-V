# EJEMPLO DE POLIMORFISMO
# Dos clases tienen el mismo método, pero funcionan diferente.

class NotificacionEmail:
    def notificar(self, mensaje):
        print(f"[EMAIL] {mensaje}")


class NotificacionSMS:
    def notificar(self, mensaje):
        print(f"[SMS] {mensaje}")


# Función que aplica polimorfismo
def enviar_notificacion(objeto, mensaje):
    objeto.notificar(mensaje)


# Bloque principal
if __name__ == "__main__":
    email = NotificacionEmail()
    sms = NotificacionSMS()

    enviar_notificacion(email, "Tu tarea de POO vence 07/12/2025.")
    enviar_notificacion(sms, "Tienes un mensaje nuevo.")
