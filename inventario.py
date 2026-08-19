herramientas = [
    {
        "id_herramienta": 1,
        "nombre": "Taladro",
        "estado": "Activa"
    },
    {
        "id_herramienta": 2,
        "nombre": "Martillo",
        "estado": "Activa"
    },
    {
        "id_herramienta": 3,
        "nombre": "Destornillador",
        "estado": "Activa"
    },
    {
        "id_herramienta": 4,
        "nombre": "Sierra",
        "estado": "Activa"
    }
]


def buscar_herramienta(id_herramienta):
    for herramienta in herramientas:
        if herramienta["id_herramienta"] == id_herramienta:
            return herramienta

    return None