import json
import os

ARCHIVO_USUARIOS = "usuarios.json"

def cargar_usuarios():

    try:

        if os.path.exists(ARCHIVO_USUARIOS):

            with open(ARCHIVO_USUARIOS, "r") as f:
                return json.load(f)

        return {}

    except:
        return {}

def registrar_usuario(nombre, contrasena):

    usuarios = cargar_usuarios()

    if nombre in usuarios:
        return False, "El usuario ya existe"

    usuarios[nombre] = contrasena

    with open(ARCHIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

    return True, "Registro exitoso"

def iniciar_sesion(nombre, contrasena):

    usuarios = cargar_usuarios()

    if nombre not in usuarios:
        return False, "Usuario no encontrado"

    if usuarios[nombre] != contrasena:
        return False, "Contraseña incorrecta"

    return True, "Login exitoso"