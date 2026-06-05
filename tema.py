# tema.py

tema_oscuro = {
    "fondo": (0.02, 0.02, 0.06, 1),
    "fondo_secundario": (0.05, 0.05, 0.08, 1),
    "boton": (0.1, 0.1, 0.15, 1),
    "boton_secundario": (0.2, 0.5, 1, 1),
    "texto": (1, 1, 1, 1),
    "texto_secundario": (0.7, 0.7, 0.7, 1)
}

tema_claro = {
    "fondo": (0.93, 0.93, 0.93, 1),
    "fondo_secundario": (1, 1, 1, 1),
    "boton": (1, 1, 1, 1),
    "boton_secundario": (0.2, 0.5, 1, 1),
    "texto": (0, 0, 0, 1),
    "texto_secundario": (0.3, 0.3, 0.3, 1)
}

tema_actual = tema_oscuro

def cambiar_tema():
    global tema_actual

    if tema_actual == tema_oscuro:
        tema_actual = tema_claro
    else:
        tema_actual = tema_oscuro