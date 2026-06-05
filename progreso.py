# progreso.py

import json
import os

ARCHIVO = "progreso.json"

usuario_activo = None

progreso_global = {
    "habitos": [False]*30,
    "ejercicio": [False]*30,
    "dinero": [False]*30
}

def progreso_vacio():
    return {
        "habitos": [False]*30,
        "ejercicio": [False]*30,
        "dinero": [False]*30
    }

def guardar_progreso():

    global progreso_global
    global usuario_activo

    try:

        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as f:
                todos = json.load(f)

        else:
            todos = {}

        todos[usuario_activo] = progreso_global

        with open(ARCHIVO, "w") as f:
            json.dump(todos, f, indent=4)

    except Exception as e:
        print(e)

def cargar_progreso():

    global progreso_global
    global usuario_activo

    try:

        if os.path.exists(ARCHIVO):

            with open(ARCHIVO, "r") as f:
                todos = json.load(f)

            if usuario_activo in todos:
                progreso_global = todos[usuario_activo]

            else:
                progreso_global = progreso_vacio()

    except Exception as e:
        print(e)
        
usuario_activo = None

def set_usuario(nombre):
    global usuario_activo
    usuario_activo = nombre
    
def get_usuario():
    return usuario_activo