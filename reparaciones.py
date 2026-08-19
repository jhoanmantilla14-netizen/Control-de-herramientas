import json
import os
from datetime import datetime
from inventario import buscar_herramienta


ARCHIVO_REPARACIONES = "reports/reparaciones.json"


def cargar_reparaciones():
    if not os.path.exists(ARCHIVO_REPARACIONES):
        return []

    with open(ARCHIVO_REPARACIONES, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_reparaciones(reparaciones):
    os.makedirs("reports", exist_ok=True)

    with open(ARCHIVO_REPARACIONES, "w", encoding="utf-8") as archivo:
        json.dump(reparaciones, archivo, indent=4, ensure_ascii=False)


def registrar_reparacion():
    print("\n=== REGISTRAR REPARACIÓN ===")

    try:
        id_herramienta = int(input("ID de la herramienta: "))
    except ValueError:
        print(" El ID debe ser un número.")
        return

    herramienta = buscar_herramienta(id_herramienta)

    if herramienta is None:
        print(" La herramienta no existe en el inventario.")
        return

    if herramienta["estado"] == "En reparación":
        print(" La herramienta ya está en reparación.")
        return

    print(f"\nHerramienta encontrada: {herramienta['nombre']}")
    print(f"Estado actual: {herramienta['estado']}")

    fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
    fecha_fin = input("Fecha estimada de finalización (AAAA-MM-DD): ")
    observaciones = input("Observaciones: ")

    try:
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

        if fin < inicio:
            print(" La fecha de finalización no puede ser anterior a la fecha de inicio.")
            return

    except ValueError:
        print(" Las fechas deben tener el formato AAAA-MM-DD.")
        return

    reparaciones = cargar_reparaciones()

    nueva_reparacion = {
        "id_herramienta": herramienta["id_herramienta"],
        "nombre": herramienta["nombre"],
        "fecha_inicio": fecha_inicio,
        "fecha_finalizacion": fecha_fin,
        "observaciones": observaciones
    }

    reparaciones.append(nueva_reparacion)

    herramienta["estado"] = "En reparación"

    guardar_reparaciones(reparaciones)

    print("\n✓ Reparación registrada correctamente.")
    print("✓ La herramienta ahora está en estado 'En reparación'.")

def mostrar_reparaciones():
    print("\n=== HERRAMIENTAS EN REPARACIÓN ===")

    reparaciones = cargar_reparaciones()

    if not reparaciones:
        print("No hay herramientas en reparación.")
        return

    for reparacion in reparaciones:
        print("\n------------------------------")
        print(f"ID: {reparacion['id_herramienta']}")
        print(f"Nombre: {reparacion['nombre']}")
        print(f"Inicio: {reparacion['fecha_inicio']}")
        print(f"Finalización: {reparacion['fecha_finalizacion']}")
        print(f"Observaciones: {reparacion['observaciones']}")

def actualizar_reparaciones():
    reparaciones = cargar_reparaciones()

    if not reparaciones:
        return

    hoy = datetime.now().date()
    reparaciones_activas = []

    for reparacion in reparaciones:

        fecha_finalizacion = datetime.strptime(
            reparacion["fecha_finalizacion"],
            "%Y-%m-%d"
        ).date()

        if hoy >= fecha_finalizacion:

            herramienta = buscar_herramienta(
                reparacion["id_herramienta"]
            )

            if herramienta:
                herramienta["estado"] = "Activa"

                print(
                    f"\n✓ La herramienta "
                    f"'{herramienta['nombre']}' "
                    f"ya terminó su reparación."
                )

                print("✓ Estado actualizado a 'Activa'.")

        else:
            reparaciones_activas.append(reparacion)

    guardar_reparaciones(reparaciones_activas)