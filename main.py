from reparaciones import (
    registrar_reparacion,
    mostrar_reparaciones,
    actualizar_reparaciones
)


def menu():
    actualizar_reparaciones()

    while True:

        print("\n==============================")
        print("   CONTROL DE HERRAMIENTAS")
        print("==============================")
        print("1. Registrar reparación")
        print("2. Ver herramientas en reparación")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_reparacion()

        elif opcion == "2":
            mostrar_reparaciones()

        elif opcion == "3":
            print("\nPrograma finalizado.")
            break

        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    menu()