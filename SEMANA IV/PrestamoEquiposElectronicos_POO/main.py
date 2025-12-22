from modelos.equipo import Equipo
from modelos.usuario import Usuario
from servicios.inventario import Inventario


def main():
    inventario = Inventario()

    print("=== SISTEMA DE PRÉSTAMO DE EQUIPOS ===")

    # Ingreso de datos del equipo
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    codigo_equipo = input("Ingrese el código del equipo: ")
    equipo = Equipo(nombre_equipo, codigo_equipo)

    inventario.agregar_equipo(equipo)

    # Ingreso de datos del usuario
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    cedula_usuario = input("Ingrese la cédula del usuario: ")
    usuario = Usuario(nombre_usuario, cedula_usuario)

    # Menú simple
    opcion = ""

    while opcion != "3":
        print("\n--- MENÚ ---")
        print("1. Prestar equipo")
        print("2. Devolver equipo")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(inventario.prestar(codigo_equipo, usuario))
        elif opcion == "2":
            print(inventario.devolver(codigo_equipo))
        elif opcion == "3":
            print("Saliendo del sistema...")
        else:
            print("Opción inválida, intente nuevamente.")

        print("\nEstado actual del inventario:")
        print(inventario.listar_equipos())


if __name__ == "__main__":
    main()
