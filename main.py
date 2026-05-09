from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation
import json
import os
from datetime import datetime
from kivy.uix.textinput import TextInput
import random 
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color as KivyColor
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.floatlayout import FloatLayout


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


frases = [
    "Disciplina.\nConstancia.\nResultados.",
    "El éxito...\nse construye...\ncada día.",
    "Pequeños pasos.\nGrandes destinos.",
    "Hoy es\nel mejor día\npara empezar.",
    "La motivación\nte arranca.\nEl hábito\nte mantiene.",
    "No pares.\nNunca pares.",
    "Un día más.\nUn paso más.",
    "Tú decides.\nTú actúas.\nTú logras.",
    "El cambio\nempieza hoy.",
    "Constancia\nes poder."
]

# 🔹 30 tareas por categoría
tareas_habitos = [
{"dia":"1","tarea":"Leer 10 páginas"},
{"dia":"2","tarea":"Tomar 2L de agua"},
{"dia":"3","tarea":"No usar el celular al despertar"},
{"dia":"4","tarea":"Dormir antes de las 10pm"},
{"dia":"5","tarea":"Hacer tu cama"},
{"dia":"6","tarea":"Escribir 3 metas"},
{"dia":"7","tarea":"Evitar redes sociales 2h"},
{"dia":"8","tarea":"Comer sin distracciones"},
{"dia":"9","tarea":"Escuchar un podcast"},
{"dia":"10","tarea":"Meditar 5 minutos"},
{"dia":"11","tarea":"Agradecer 3 cosas"},
{"dia":"12","tarea":"No azúcar hoy"},
{"dia":"13","tarea":"Organizar tu espacio"},
{"dia":"14","tarea":"Leer 15 páginas"},
{"dia":"15","tarea":"Despertar temprano"},
{"dia":"16","tarea":"Tomar agua al despertar"},
{"dia":"17","tarea":"No procrastinar 1h"},
{"dia":"18","tarea":"Planear tu día"},
{"dia":"19","tarea":"Aprender algo nuevo"},
{"dia":"20","tarea":"Evitar quejas"},
{"dia":"21","tarea":"Respirar profundo 5 min"},
{"dia":"22","tarea":"No redes en la noche"},
{"dia":"23","tarea":"Comer saludable"},
{"dia":"24","tarea":"Leer 20 páginas"},
{"dia":"25","tarea":"Dormir 8 horas"},
{"dia":"26","tarea":"Beber agua constantemente"},
{"dia":"27","tarea":"Revisar tus metas"},
{"dia":"28","tarea":"No distracciones al estudiar"},
{"dia":"29","tarea":"Ordenar tu habitación"},
{"dia":"30","tarea":"Reflexionar tu progreso"}
]

tareas_dinero = [
{"dia":"1","tarea":"Ahorrar $5.000"},
{"dia":"2","tarea":"No gastar en cosas innecesarias"},
{"dia":"3","tarea":"Anotar todos tus gastos"},
{"dia":"4","tarea":"Buscar una idea de negocio"},
{"dia":"5","tarea":"Ahorrar $10.000"},
{"dia":"6","tarea":"Ver un video de finanzas"},
{"dia":"7","tarea":"No comprar dulces ni antojos"},
{"dia":"8","tarea":"Ahorrar $5.000"},
{"dia":"9","tarea":"Pensar cómo ganar dinero"},
{"dia":"10","tarea":"Leer sobre dinero o inversiones"},
{"dia":"11","tarea":"Ahorrar $15.000"},
{"dia":"12","tarea":"No gastar nada hoy"},
{"dia":"13","tarea":"Vender algo que no uses"},
{"dia":"14","tarea":"Ahorrar $5.000"},
{"dia":"15","tarea":"Aprender sobre inversión"},
{"dia":"16","tarea":"No comprar impulsivamente"},
{"dia":"17","tarea":"Ahorrar $10.000"},
{"dia":"18","tarea":"Revisar tus gastos"},
{"dia":"19","tarea":"Buscar un cliente"},
{"dia":"20","tarea":"Ahorrar $20.000"},
{"dia":"21","tarea":"Ver un podcast de dinero"},
{"dia":"22","tarea":"No gastar en antojos"},
{"dia":"23","tarea":"Ahorrar $5.000"},
{"dia":"24","tarea":"Pensar en un negocio"},
{"dia":"25","tarea":"Ahorrar $15.000"},
{"dia":"26","tarea":"Aprender sobre ventas"},
{"dia":"27","tarea":"No gastar hoy"},
{"dia":"28","tarea":"Ahorrar $10.000"},
{"dia":"29","tarea":"Revisar tu progreso"},
{"dia":"30","tarea":"Crear tu plan financiero"}
]

tareas_ejercicio = [
{"dia":"1","tarea":"20 flexiones"},
{"dia":"2","tarea":"30 sentadillas"},
{"dia":"3","tarea":"Plancha 30 segundos"},
{"dia":"4","tarea":"Correr 1 km"},
{"dia":"5","tarea":"20 abdominales"},
{"dia":"6","tarea":"Saltar cuerda 2 min"},
{"dia":"7","tarea":"30 jumping jacks"},
{"dia":"8","tarea":"25 flexiones"},
{"dia":"9","tarea":"40 sentadillas"},
{"dia":"10","tarea":"Plancha 45 seg"},
{"dia":"11","tarea":"Correr 2 km"},
{"dia":"12","tarea":"30 abdominales"},
{"dia":"13","tarea":"Saltar cuerda 3 min"},
{"dia":"14","tarea":"40 jumping jacks"},
{"dia":"15","tarea":"30 flexiones"},
{"dia":"16","tarea":"50 sentadillas"},
{"dia":"17","tarea":"Plancha 1 min"},
{"dia":"18","tarea":"Correr 3 km"},
{"dia":"19","tarea":"40 abdominales"},
{"dia":"20","tarea":"Saltar cuerda 5 min"},
{"dia":"21","tarea":"50 jumping jacks"},
{"dia":"22","tarea":"35 flexiones"},
{"dia":"23","tarea":"60 sentadillas"},
{"dia":"24","tarea":"Plancha 1:30 min"},
{"dia":"25","tarea":"Correr 4 km"},
{"dia":"26","tarea":"50 abdominales"},
{"dia":"27","tarea":"Saltar cuerda 6 min"},
{"dia":"28","tarea":"60 jumping jacks"},
{"dia":"29","tarea":"40 flexiones"},
{"dia":"30","tarea":"Entrenamiento completo"}
]

progreso_global = {
    "habitos": [False]*30,
    "ejercicio": [False]*30,
    "dinero": [False]*30
}
ARCHIVO = "progreso.json"
ARCHIVO_USUARIOS = "usuarios.json"

usuario_activo = None

def progreso_vacio():
    return {
        "habitos": [False]*30,
        "ejercicio": [False]*30,
        "dinero": [False]*30
    }

def guardar_progreso():
    try:
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as f:
                todos = json.load(f)
        else:
            todos = {}

        todos[usuario_activo] = progreso_global
        
        with open(ARCHIVO, "w") as f:
            json.dump(todos, f, indent=4)

    except (json.JSONDecodeError, IOError) as e:
        print(f"[ADVERTENCIA] No se pudo guardar progreso: {e}")


def cargar_usuarios():
    try:
        if os.path.exists(ARCHIVO_USUARIOS):
            with open(ARCHIVO_USUARIOS, "r") as f:
                return json.load(f)
        return {}
    except (json.JSONDecodeError, IOError) as e:
        print(f"[ADVERTENCIA] No se pudo cargar usuarios: {e}")
        return {}

def registrar_usuario(nombre, contrasena):
    usuarios = cargar_usuarios()

    if nombre in usuarios:
        return False, "El usuario ya existe"

    usuarios[nombre] = contrasena

    try:
        with open(ARCHIVO_USUARIOS, "w") as f:
            json.dump(usuarios, f, indent=4)
        return True, "Registro exitoso"
    except IOError as e:
        return False, f"Error al guardar: {e}"

def iniciar_sesion(nombre, contrasena):
    usuarios = cargar_usuarios()

    if nombre not in usuarios:
        return False, "Usuario no encontrado"

    if usuarios[nombre] != contrasena:
        return False, "Contraseña incorrecta"

    return True, "Login exitoso"


def cargar_progreso():
    global progreso_global

    try:
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as f:
                todos = json.load(f)

            if usuario_activo in todos:
                data = todos[usuario_activo]
                for clave in progreso_global:
                    if isinstance(data.get(clave), list) and len(data[clave]) == 30:
                        progreso_global[clave] = data[clave]
            else:
                progreso_global = progreso_vacio()
        else:
            progreso_global = progreso_vacio()

    except (json.JSONDecodeError, IOError) as e:
        print(f"[ADVERTENCIA] No se pudo cargar progreso: {e}")
        progreso_global = progreso_vacio()


# 🔹 SISTEMA DE PARTÍCULAS
class FondoParticulas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.particulas = []
        Clock.schedule_once(self.iniciar, 0.1)

    def iniciar(self, dt):
        self.canvas.clear()
        self.particulas = []

        for _ in range(40):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            tamanio = random.uniform(2, 6)
            velocidad = random.uniform(0.2, 0.8)
            opacidad = random.uniform(0.1, 0.5)
            tipo = random.choice(['blanco', 'azul', 'cyan'])

            self.particulas.append({
                'x': x,
                'y': y,
                'tamanio': tamanio,
                'velocidad': velocidad,
                'opacidad': opacidad,
                'tipo': tipo
            })

        Clock.schedule_interval(self.actualizar, 1/60)

    def actualizar(self, dt):
        self.canvas.clear()

        with self.canvas:

            for p in self.particulas:
                p['y'] += p['velocidad']

                if p['y'] > self.height + 10:
                    p['y'] = -10
                    p['x'] = random.uniform(0, self.width)

                if p['tipo'] == 'blanco':
                    KivyColor(1, 1, 1, p['opacidad'])
                elif p['tipo'] == 'azul':
                    KivyColor(0.2, 0.5, 1, p['opacidad'])
                elif p['tipo'] == 'cyan':
                    KivyColor(0, 0.8, 1, p['opacidad'])

                Ellipse(
                    pos=(p['x'] - p['tamanio']/2, p['y'] - p['tamanio']/2),
                    size=(p['tamanio'], p['tamanio'])
                )

    def detener(self):
        Clock.unschedule(self.actualizar)


# 🔹 MENÚ PRINCIPAL
class Inicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        layout = self.layout

        with layout.canvas.before:  
            Color(*tema_actual["fondo"])  # fondo oscuro elegante
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        btn_back = Button(
            text='<',
            font_size=31,
            size_hint=(None, None),
            size=(50, 50),
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=tema_actual["texto"]  
        )

        btn_back.bind(on_press=lambda x: self.ir_bienvenida())

        top_bar = BoxLayout(size_hint_y=None, height=60, padding=[0, 10, 0, 0])

        btn_tema = Button(
            text='🌙',
            font_size=18,
            size_hint=(None, None),
            size=(60, 40),
            background_normal='',
            background_color=tema_actual["fondo_secundario"],
            color=tema_actual["texto"],
        )

        btn_tema.bind(on_press=self.toggle_tema)


        btn_cerrar = Button(
    text='Salir',
    font_size=16,
    size_hint=(None, None),
    size=(70, 40),
    background_normal='',
    background_color=(0.6, 0.1, 0.1, 1),
    color=(1, 1, 1, 1)
)

        btn_cerrar.bind(on_press=self.cerrar_sesion)

        top_bar.add_widget(btn_back)
        top_bar.add_widget(Label(size_hint_x=1))
        top_bar.add_widget(btn_tema)
        top_bar.add_widget(btn_cerrar)

        layout.add_widget(top_bar)

        layout.bind(size=self.update_rect, pos=self.update_rect)

        self.titulo = Label(
            text='Mi Reto 30 Días',
            font_size=48,
            bold = True,
            color=tema_actual["texto"],
            size_hint_y=None,
            height=80
)
        self.subtitulo = Label(
        text='Desafíos diarios',
        font_size=24,
        bold=True,
        color=(0.2, 0.5, 1, 1),
        size_hint_y=None,
        height=40
    )

        self.titulo.bind(size=self.titulo.setter('text_size'))


        # 🔹 CARD HÁBITOS
        card1_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=130)

        self.card1 = Button(
            text='Desafios Hábitos',
            font_size=24,
            size_hint_y=None,
            height=120,
            background_normal='',
            background_color=tema_actual["boton"],
            color=tema_actual["texto"],
        )

        self.label_h = Label(
            text="0%",
            size_hint_y=None,
            height=20,
            color=tema_actual["texto"]
        )

        with self.card1.canvas.before:
            Color(0, 0, 0, 0.4)
            sombra1 = Rectangle(pos=(self.card1.x, self.card1.y - 5), size=self.card1.size)

        self.card1.bind(
            pos=lambda inst, val: self.update_sombra(inst, sombra1),
            size=lambda inst, val: self.update_sombra(inst, sombra1)
        )

        # 🔹 Barra progreso
        barra = BoxLayout(size_hint_y=None, height=10)

        with barra.canvas.before:
            Color(0, 0.6, 1, 1)
            self.rect_barra_habitos = Rectangle(size=(0, 10), pos=barra.pos)

        barra.bind(pos=self.update_pos_barras, size=self.update_barras)

        self.card1.bind(on_press=lambda x: self.animar_card(x))
        self.card1.bind(on_press=lambda x: self.cambiar('habitos'))

        card1_layout.add_widget(self.card1)
        card1_layout.add_widget(self.label_h)
        card1_layout.add_widget(barra)

        #Card ejercicio
        card2_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=150)

        self.card2 = Button(
            text='Desafios Ejercicio',
            font_size=24,
            size_hint_y=None,
            height=120,
            background_normal='',
            background_color=tema_actual["boton"],
            color=tema_actual["texto"]
        )

        self.label_e = Label(
            text="0%",
            size_hint_y=None,
            height=20,
            color=tema_actual["texto"]
        )

        barra2 = BoxLayout(size_hint_y=None, height=10)

        with barra2.canvas.before:
            Color(0, 1, 0.5, 1)
            self.rect_barra_ejercicio = Rectangle(size=(0, 10), pos=barra2.pos)

        barra2.bind(pos=self.update_pos_barras, size=self.update_barras)

        self.card2.bind(on_press=lambda x: self.animar_card(x))
        self.card2.bind(on_press=lambda x: self.cambiar('ejercicio'))

        card2_layout.add_widget(self.card2)
        card2_layout.add_widget(self.label_e)
        card2_layout.add_widget(barra2)


        # 🔹 CARD DINERO
        card3_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=150)

        self.card3 = Button(
            text='Desafios Dinero',
            font_size=24,
            size_hint_y=None,
            height=120,
            background_normal='',
            background_color=tema_actual["boton"],
            color=tema_actual["texto"]
        )

        self.label_d = Label(
            text="0%",
            size_hint_y=None,
            height=20,
            color=tema_actual["texto"]
        )

        barra3 = BoxLayout(size_hint_y=None, height=10)

        with barra3.canvas.before:
            Color(1, 0.7, 0, 1)
            self.rect_barra_dinero = Rectangle(size=(0, 10), pos=barra3.pos)

        barra3.bind(pos=self.update_pos_barras, size=self.update_barras)

        self.card3.bind(on_press=lambda x: self.animar_card(x))
        self.card3.bind(on_press=lambda x: self.cambiar('dinero'))

        card3_layout.add_widget(self.card3)
        card3_layout.add_widget(self.label_d)
        card3_layout.add_widget(barra3)


        # 🔹 AGREGAR EN ORDEN CORRECTO
        layout.add_widget(self.titulo)
        layout.add_widget(self.subtitulo)
        layout.add_widget(card1_layout)
        layout.add_widget(card2_layout)
        layout.add_widget(card3_layout)

        self.barra1 = barra
        self.barra2 = barra2
        self.barra3 = barra3

        self.add_widget(layout)
       

    def update_sombra(self, instance, sombra):
        sombra.pos = (instance.x, instance.y - 5)
        sombra.size = instance.size

    def animar_card(self, instance):

        color_original = tema_actual["boton"]

        anim = Animation(
            background_color=(0.25, 0.25, 0.4, 1),
            duration=0.1
        ) + Animation(
            background_color=color_original,
            duration=0.2
        )

        anim.start(instance)

    def cambiar(self, pantalla):
        self.manager.transition = FadeTransition(duration=0.15)
        self.manager.current = pantalla

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos


    def update_pos_barras(self, *args):
        self.rect_barra_habitos.pos = self.barra1.pos
        self.rect_barra_ejercicio.pos = self.barra2.pos
        self.rect_barra_dinero.pos = self.barra3.pos

    def update_barras(self, *args):

        self.progreso_h = sum(progreso_global["habitos"]) / 30
        self.progreso_e = sum(progreso_global["ejercicio"]) / 30
        self.progreso_d = sum(progreso_global["dinero"]) / 30

        Animation.cancel_all(self.rect_barra_habitos)
        Animation.cancel_all(self.rect_barra_ejercicio)
        Animation.cancel_all(self.rect_barra_dinero)

        anim = Animation(duration=0.4)
        anim.bind(on_progress=self.animar_barras)
        anim.start(self)


    def on_pre_enter(self):
        self.subtitulo.text = f'¡Hola {usuario_activo}! '
        Clock.schedule_once(self.update_barras, 0.1)

    def ir_bienvenida(self):
        self.manager.transition = FadeTransition(duration=0.15)
        self.manager.current = 'bienvenida'

    def toggle_tema(self, instance):
        cambiar_tema()

        for pantalla in self.manager.screens:

            if hasattr(pantalla, "actualizar_tema"):
                pantalla.actualizar_tema()


    def cerrar_sesion(self, instance):
        global usuario_activo, progreso_global

        usuario_activo = None
        progreso_global = progreso_vacio()

        self.manager.transition = FadeTransition(duration=0.15)
        self.manager.current = 'login'

    def animar_barras(self, animation, widget, progress):

        self.rect_barra_habitos.size = (
            self.barra1.width * self.progreso_h * progress,
            10
        )

        self.rect_barra_ejercicio.size = (
            self.barra2.width * self.progreso_e * progress,
            10
        )

        self.rect_barra_dinero.size = (
            self.barra3.width * self.progreso_d * progress,
            10
        )

        # porcentajes
        self.label_h.text = f"{int(self.progreso_h * 100)}%"
        self.label_e.text = f"{int(self.progreso_e * 100)}%"
        self.label_d.text = f"{int(self.progreso_d * 100)}%"

    def actualizar_tema(self):

        # fondo
        self.layout.canvas.before.clear()

        with self.layout.canvas.before:
            Color(*tema_actual["fondo"])
            self.rect = Rectangle(
                size=self.layout.size,
                pos=self.layout.pos
            )

        # cards
        self.card1.background_color = tema_actual["boton"]
        self.card2.background_color = tema_actual["boton"]
        self.card3.background_color = tema_actual["boton"]

        # texto cards
        self.card1.color = tema_actual["texto"]
        self.card2.color = tema_actual["texto"]
        self.card3.color = tema_actual["texto"]

        # porcentajes
        self.label_h.color = tema_actual["texto"]
        self.label_e.color = tema_actual["texto"]
        self.label_d.color = tema_actual["texto"]

        # títulos
        self.titulo.color = tema_actual["texto"]
        self.subtitulo.color = (0.2, 0.5, 1, 1)

        # actualizar fondo dinámico
        self.layout.bind(size=self.update_rect, pos=self.update_rect)


# 🔹 PANTALLA DE RETO
class PantallaReto(Screen):
    def __init__(self, titulo_texto, tareas, **kwargs):
        super().__init__(**kwargs)



        self.completados = 0

        scroll = ScrollView()

        self.layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15,
            size_hint_y=None
        )

        self.layout.bind(minimum_height=self.layout.setter('height'))


        with self.layout.canvas.before:
            Color(*tema_actual["fondo"])
            self.rect = Rectangle(
                size=self.layout.size,
                pos=self.layout.pos
            )

        self.layout.bind(size=self.update_rect, pos=self.update_rect)

        # 🔹 TÍTULO
        self.titulo = Label(text=titulo_texto, font_size=35, size_hint_y=None, height=60)
        self.layout.add_widget(self.titulo)

        # 🔹 PROGRESO
        self.label_progreso = Label(
            text='0/30 Completados',
            font_size=20,
            size_hint_y=None,
            height=40
        )

        self.layout.add_widget(self.label_progreso)

        # 🔹 BARRA PROGRESO REAL
        self.barra_bg = BoxLayout(size_hint_y=None, height=15)

        with self.barra_bg.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            self.rect_bg = Rectangle(size=self.barra_bg.size, pos=self.barra_bg.pos)

            Color(0, 0.6, 1, 1)
            self.rect_barra = Rectangle(size=(0, 15), pos=self.barra_bg.pos)

        self.barra_bg.bind(pos=self.update_barra, size=self.update_barra)

        self.layout.add_widget(self.barra_bg)


        # 🔹 FILTROS
        self.filtro_actual = 'todas'

        fila_filtros = BoxLayout(size_hint_y=None, height=45, spacing=10)

        self.btn_todas = Button(
            text='Todas',
            background_normal='',
            background_color=(0.2, 0.5, 1, 1),
            font_size=18
        )

        self.btn_pendientes = Button(
            text='Pendientes',
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1),
            font_size=18
        )

        self.btn_completadas = Button(
            text='Completadas',
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1),
            font_size=18
        )

        self.btn_todas.bind(on_press=lambda x: self.aplicar_filtro('todas'))
        self.btn_pendientes.bind(on_press=lambda x: self.aplicar_filtro('pendientes'))
        self.btn_completadas.bind(on_press=lambda x: self.aplicar_filtro('completadas'))

        fila_filtros.add_widget(self.btn_todas)
        fila_filtros.add_widget(self.btn_pendientes)
        fila_filtros.add_widget(self.btn_completadas)

        self.layout.add_widget(fila_filtros)


        self.filas = []

        # 🔹 LISTA DE TAREAS
        for i, tarea in enumerate(tareas):

            fila = BoxLayout(
                size_hint_y=None,
                height=85,
                padding=10,
                spacing=10
            )

            desbloqueado = (
                i == 0 or progreso_global[self.name][i - 1]
            )

            completado = progreso_global[self.name][i]

            # 🔓 RETO DESBLOQUEADO
            if desbloqueado:

                texto = (
                    f"[b]{tarea['tarea']}[/b]\n"
                    f"[size=14][color=aaaaaa]Día {tarea['dia']}[/color][/size]"
                )

                label = Label(
                    text=texto,
                    halign='left',
                    valign='middle',
                    markup=True,
                    opacity=1
                )

                label.bind(
                    size=lambda instance, value: setattr(instance, 'text_size', value)
                )

                label.bind(size=label.setter('text_size'))

                btn = Button(
                    text='Completar',
                    size_hint_x=0.32,
                    background_normal='',
                    background_color=(0.0, 0.35, 0.7, 1)
                )

                if completado:
                    btn.text = "Completado"
                    btn.background_color = (0.2, 0.7, 1, 1)
                    btn.opacity = 0.7

                btn.index = i
                btn.bind(on_press=self.completar)

            # 🔒 RETO BLOQUEADO
            else:

                label = Label(
                    text=f" Día {tarea['dia']}",
                    markup=True,
                    halign='center',
                    valign='middle',
                    color=(0.5, 0.5, 0.5, 1)
                )

                label.bind(size=label.setter('text_size'))

                btn = Button(
                    text='🔒',
                    disabled=True,
                    size_hint_x=0.32,
                    background_normal='',
                    background_color=(0.05, 0.05, 0.05, 1),
                    opacity=0.6
                )

            fila.add_widget(label)
            fila.add_widget(btn)

            self.filas.append((fila, i))

            self.layout.add_widget(fila)

        # 🔹 BOTÓN VOLVER
        btn_volver = Button(
            text='Volver al menú',
            size_hint_y=None, 
            height=80,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1),
            font_size=20,
            halign='center',
        )

        self.label_progreso.text = f"{self.completados}/30 completados"

        btn_volver.bind(on_press=self.volver)

        self.layout.add_widget(btn_volver)

        scroll.add_widget(self.layout)
        self.add_widget(scroll)

        Clock.schedule_once(lambda dt: self.actualizar_barra(), 0.1)

    def completar(self, instance):

        i = instance.index

        # ✅ QUITAR completado
        if progreso_global[self.name][i]:

            progreso_global[self.name][i] = False

            instance.text = "Completar"

            Animation(
                background_color=(0.0, 0.35, 0.7, 1),
                duration=0.2
            ).start(instance)

            Animation(
                opacity=1,
                duration=0.2
            ).start(instance)

            self.completados -= 1

        # ✅ MARCAR completado
        else:

            progreso_global[self.name][i] = True

            instance.text = "Completado"

            Animation(
                background_color=(0.2, 0.7, 1, 1),
                duration=0.2
            ).start(instance)

            Animation(
                opacity=0.7,
                duration=0.3
            ).start(instance)

            self.completados += 1

            # 🔓 desbloquear siguiente reto
            if i + 1 < len(self.filas):

                siguiente_fila, _ = self.filas[i + 1]

                btn = siguiente_fila.children[0]
                label = siguiente_fila.children[1]

                if btn.disabled:

                    tarea_siguiente = (
                        tareas_habitos[i + 1]["tarea"]
                        if self.name == "habitos"
                        else tareas_ejercicio[i + 1]["tarea"]
                        if self.name == "ejercicio"
                        else tareas_dinero[i + 1]["tarea"]
                    )

                    label.text = (
                        f"[b]{tarea_siguiente}[/b]\n"
                        f"[size=14][color=aaaaaa]Día {i + 2}[/color][/size]"
                    )

                    label.markup = True
                    label.color = (1, 1, 1, 1)

                    btn.disabled = False
                    btn.text = "Completar"

                    btn.background_color = (0.0, 0.35, 0.7, 1)
                    btn.opacity = 1
                    btn.color = (1, 1, 1, 1)

                    btn.index = i + 1
                    btn.bind(on_press=self.completar)

                    Animation(opacity=1, duration=0.4).start(siguiente_fila)

        # ✅ evitar negativos
        if self.completados < 0:
            self.completados = 0

        # actualizar texto
        self.completados = sum(progreso_global[self.name])
        self.label_progreso.text = f"{self.completados}/30 completados"

        # guardar
        guardar_progreso()

        # actualizar barra
        self.actualizar_barra()

        self.aplicar_filtro(self.filtro_actual)

        # 🏆 completó los 30
        if self.completados == 30:
            self.mostrar_felicitacion()

    def mostrar_felicitacion(self):

        overlay = FloatLayout(size=self.size, pos=self.pos)

        with overlay.canvas.before:
            Color(0, 0, 0, 0.85)
            self.rect_overlay = Rectangle(size=overlay.size, pos=overlay.pos)

        mensaje = Label(
            text='🏆\n¡Reto completado!\n¡Lo lograste!',
            font_size=36,
            bold=True,
            halign='center',
            color=(1, 0.8, 0.2, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )

        btn_cerrar = Button(
            text='¡Seguir adelante!',
            font_size=20,
            size_hint=(0.6, None),
            height=60,
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
        )

        btn_cerrar.bind(on_press=lambda x: self.remove_widget(overlay))

        overlay.add_widget(mensaje)
        overlay.add_widget(btn_cerrar)

        self.add_widget(overlay)

        anim = Animation(opacity=0, duration=0) + Animation(opacity=1, duration=0.5)
        anim.start(overlay)


    def update_barra(self, instance, value):
        self.rect_barra.pos = instance.pos
        self.rect_bg.pos = instance.pos
        self.rect_bg.size = instance.size

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos
    

    def on_pre_enter(self):
        self.completados = sum(progreso_global[self.name])
        self.label_progreso.text = f"{self.completados}/30 completados"
        self.actualizar_barra()
        self.actualizar_botones()
    

    def actualizar_botones(self):
        for fila, i in self.filas:
            btn = fila.children[0]

            if btn.disabled:
                continue

            if progreso_global[self.name][i]:
                btn.text = "Completado"
                btn.background_color = (0.2, 0.7, 1, 1)
                btn.opacity = 0.7
            else:
                btn.text = "Completar"
                btn.background_color = (0.0, 0.35, 0.7, 1)
                btn.opacity = 1


    def mostrar_fila(self, fila):
        fila.opacity = 1
        fila.height = 85
        fila.disabled = False

    def ocultar_fila(self, fila):
        fila.opacity = 0
        fila.height = 0
        fila.disabled = True


        
    def aplicar_filtro(self, filtro):

        self.filtro_actual = filtro

        # colores botones
        self.btn_todas.background_color = (0.1, 0.1, 0.15, 1)
        self.btn_pendientes.background_color = (0.1, 0.1, 0.15, 1)
        self.btn_completadas.background_color = (0.1, 0.1, 0.15, 1)

        if filtro == 'todas':
            self.btn_todas.background_color = (0.2, 0.5, 1, 1)

        elif filtro == 'pendientes':
            self.btn_pendientes.background_color = (0.2, 0.5, 1, 1)

        elif filtro == 'completadas':
            self.btn_completadas.background_color = (0.2, 0.5, 1, 1)

        # mostrar / ocultar filas
        for fila, i in self.filas:

            completada = progreso_global[self.name][i]

            if filtro == 'todas':
                self.mostrar_fila(fila)

            elif filtro == 'pendientes':

                if completada:
                    self.ocultar_fila(fila)
                else:
                    self.mostrar_fila(fila)

            elif filtro == 'completadas':

                if completada:
                    self.mostrar_fila(fila)
                else:
                    self.ocultar_fila(fila)


    def volver(self, instance):
        self.manager.transition = FadeTransition(duration=0.15)
        self.manager.current = 'inicio'

    def actualizar_barra(self):
        progreso = self.completados / 30  # porcentaje

        # ancho según progreso
        ancho = self.barra_bg.width * progreso

        self.rect_barra.size = (ancho, self.barra_bg.height)


    def actualizar_tema(self):

        # fondo principal
        self.layout.canvas.before.clear()

        with self.layout.canvas.before:
            Color(*tema_actual["fondo"])
            self.rect = Rectangle(
                size=self.layout.size,
                pos=self.layout.pos
            )

        # título y progreso
        self.titulo.color = tema_actual["texto"]
        self.label_progreso.color = tema_actual["texto"]

        # botones filtros
        self.btn_todas.color = tema_actual["texto"]
        self.btn_pendientes.color = tema_actual["texto"]
        self.btn_completadas.color = tema_actual["texto"]

        # actualizar filas de tareas
        for fila, i in self.filas:

            label = fila.children[1]
            btn = fila.children[0]

            label.color = tema_actual["texto"]

            if progreso_global[self.name][i]:
                btn.background_color = (0.2, 0.7, 1, 1)
            else:
                btn.background_color = (0.0, 0.35, 0.7, 1)

            btn.color = tema_actual["texto"]

        # actualizar fondo barra
        self.barra_bg.canvas.before.clear()

        with self.barra_bg.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            self.rect_bg = Rectangle(
                size=self.barra_bg.size,
                pos=self.barra_bg.pos
            )

            Color(0, 0.6, 1, 1)
            self.rect_barra = Rectangle(
                size=self.rect_barra.size,
                pos=self.barra_bg.pos
            )

        self.barra_bg.bind(
            pos=self.update_barra,
            size=self.update_barra
        )


# 🔹 PANTALLA LOGIN
class PantallaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=60, spacing=20)
        layout = self.layout

        with self.layout.canvas.before:
            Color(*tema_actual["fondo"])
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self.update_rect, pos=self.update_rect)


        hora = datetime.now().hour

        if hora < 12:
            saludo = "Buenos días"
        elif hora < 19:
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"

        # TÍTULO
        self.titulo = Label(
            text=saludo,
            font_size=48,
            bold=True,
            size_hint_y=None,
            height=80
        )

        self.subtitulo = Label(
            text='Inicia sesión para continuar',
            font_size=20,
            color=(0.7, 0.7, 0.7, 1),
            size_hint_y=None,
            height=40
        )

        # CAMPOS

        self.campo_usuario = TextInput(
            hint_text='Usuario',
            multiline=False,
            size_hint_y=None,
            height=55,
            font_size=18,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )

        self.campo_contrasena = TextInput(
            hint_text='Contraseña',
            multiline=False,
            password=True,
            size_hint_y=None,
            height=55,
            font_size=18,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )

        fila_contrasena = BoxLayout(size_hint_y=None, height=55)

        btn_ojo = Button(
            text='👁',
            font_size=20,
            size_hint_x=None,
            width=55,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
            )

        btn_ojo.bind(on_press=self.toggle_contrasena)

        fila_contrasena.add_widget(self.campo_contrasena)
        fila_contrasena.add_widget(btn_ojo)

        # MENSAJE DE ERROR
        self.label_error = Label(
            text='',
            font_size=16,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        # BOTONES
        btn_entrar = Button(
            text='Iniciar sesión',
            font_size=20,
            size_hint_y=None,
            height=60,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
        )

        btn_registro = Button(
            text='¿No tienes cuenta? Regístrate',
            font_size=16,
            size_hint_y=None,
            height=45,
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(0.5, 0.8, 1, 1)
        )

        btn_entrar.bind(on_press=self.entrar)
        btn_registro.bind(on_press=self.ir_registro)

        layout.add_widget(self.titulo)
        layout.add_widget(self.subtitulo)
        layout.add_widget(self.campo_usuario)
        layout.add_widget(fila_contrasena)
        layout.add_widget(self.label_error)
        layout.add_widget(btn_entrar)
        layout.add_widget(btn_registro)

        self.add_widget(layout)

    def entrar(self, instance):
        global usuario_activo

        if getattr(self, 'bloqueado', False):
            self.label_error.text = "Demasiados intentos. Espera 5 segundos..."
            self.shake(self.campo_usuario)
            self.shake(self.campo_contrasena)
            return

        nombre = self.campo_usuario.text.strip()
        contrasena = self.campo_contrasena.text.strip()

        if not nombre or not contrasena:
            self.label_error.text = "Completa todos los campos"
            self.shake(self.campo_usuario)
            self.shake(self.campo_contrasena)
            return

        exito, mensaje = iniciar_sesion(nombre, contrasena)

        if exito:
            usuario_activo = nombre
            cargar_progreso()
            self.label_error.text = ''
            self.manager.transition = FadeTransition(duration=0.15)
            self.manager.current = 'bienvenida'

        else:
                self.intentos = getattr(self, 'intentos', 0) + 1
                self.label_error.text = mensaje
                self.shake(self.campo_usuario)
                self.shake(self.campo_contrasena)

                if self.intentos >= 3:
                    self.bloqueado = True
                    self.label_error.text = "Demasiados intentos. Espera 5 segundos..."
                    Clock.schedule_once(self.desbloquear, 5)

    def desbloquear(self, dt):
        self.bloqueado = False
        self.intentos = 0
        self.label_error.text = "Ya puedes intentar de nuevo"

    def on_pre_enter(self):

        self.layout.opacity = 1

        widgets = [
            self.titulo,
            self.subtitulo,
            self.campo_usuario,
            self.campo_contrasena,
            self.label_error
        ]

        for widget in widgets:
            widget.opacity = 1

        self.campo_usuario.text = ''
        self.campo_contrasena.text = ''
        self.label_error.text = ''

        self.intentos = 0
        self.bloqueado = False

    def ir_registro(self, instance):

        self.manager.transition = FadeTransition(duration=0.15)

        self.animar_salida_login(
            self.cambiar_a_registro
        )

    def cambiar_a_registro(self, *args):

        self.manager.current = 'registro'


    def animar_salida_login(self, callback):

        widgets = [
            self.titulo,
            self.subtitulo,
            self.campo_usuario,
            self.campo_contrasena,
            self.label_error
        ]

        duracion = 0.25

        for widget in widgets:
            Animation(
                opacity=0,
                duration=duracion
            ).start(widget)

        anim_btn = Animation(
            opacity=0,
            duration=duracion
        )

        anim_btn.bind(on_complete=lambda *x: callback())

        anim_btn.start(self.layout)


    def shake(self, widget):
        original_x = widget.x
        anim = (
            Animation(x=original_x + 10, duration=0.05) +
            Animation(x=original_x - 10, duration=0.05) +
            Animation(x=original_x + 8, duration=0.05) +
            Animation(x=original_x - 8, duration=0.05) +
            Animation(x=original_x + 5, duration=0.05) +
            Animation(x=original_x, duration=0.05)
        )
        anim.start(widget)

    def toggle_contrasena(self, instance):
        self.campo_contrasena.password = not self.campo_contrasena.password
        instance.text = '👁' if self.campo_contrasena.password else '🙈'


    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def actualizar_tema(self):

        self.layout.canvas.before.clear()

        with self.layout.canvas.before:
            Color(*tema_actual["fondo"])
            self.rect = Rectangle(
                size=self.layout.size,
                pos=self.layout.pos
            )

        self.titulo.color = tema_actual["texto"]

        self.subtitulo.color = tema_actual["texto_secundario"]

        self.campo_usuario.background_color = tema_actual["boton"]
        self.campo_contrasena.background_color = tema_actual["boton"]

        self.campo_usuario.foreground_color = tema_actual["texto"]
        self.campo_contrasena.foreground_color = tema_actual["texto"]

        self.layout.bind(size=self.update_rect, pos=self.update_rect)


    # 🔹 PANTALLA REGISTRO
class PantallaRegistro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=60, spacing=20)
        layout = self.layout

        with layout.canvas.before:
            Color(*tema_actual["fondo"])
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self.update_rect, pos=self.update_rect)

        # TÍTULO
        self.titulo = Label(
            text='Crear cuenta',
            font_size=48,
            bold=True,
            size_hint_y=None,
            height=80
        )

        self.subtitulo = Label(
            text='Completa los datos para registrarte',
            font_size=20,
            color=(0.7, 0.7, 0.7, 1),
            size_hint_y=None,
            height=40
        )

        # CAMPOS

        self.campo_usuario = TextInput(
            hint_text='Elige un usuario',
            multiline=False,
            size_hint_y=None,
            height=55,
            font_size=18,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )

        self.campo_contrasena = TextInput(
            hint_text='Elige una contraseña',
            multiline=False,
            password=True,
            size_hint_y=None,
            height=55,
            font_size=18,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )

        self.campo_confirmar = TextInput(
            hint_text='Confirma tu contraseña',
            multiline=False,
            password=True,
            size_hint_y=None,
            height=55,
            font_size=18,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )

        # MENSAJE
        self.label_mensaje = Label(
            text='',
            font_size=16,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        # BOTONES
        btn_registrar = Button(
            text='Registrarse',
            font_size=20,
            size_hint_y=None,
            height=60,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
        )

        btn_volver = Button(
            text='¿Ya tienes cuenta? Inicia sesión',
            font_size=16,
            size_hint_y=None,
            height=45,
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(0.5, 0.8, 1, 1)
        )

        self.btn_registrar = btn_registrar
        btn_registrar.bind(on_press=self.registrar)
        btn_volver.bind(on_press=self.ir_login)

        layout.add_widget(self.titulo)
        layout.add_widget(self.subtitulo)
        layout.add_widget(self.campo_usuario)
        layout.add_widget(self.campo_contrasena)
        layout.add_widget(self.campo_confirmar)
        layout.add_widget(self.label_mensaje)
        layout.add_widget(btn_registrar)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def registrar(self, instance):
        global usuario_activo

        nombre = self.campo_usuario.text.strip()
        contrasena = self.campo_contrasena.text.strip()
        confirmar = self.campo_confirmar.text.strip()

        # Validaciones
        if not nombre or not contrasena or not confirmar:
            self.label_mensaje.text = "Completa todos los campos"
            return


        if ' ' in nombre:
            self.label_mensaje.text = "El usuario no puede tener espacios"
            return

        caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
        if not all(c in caracteres_validos for c in nombre):
            self.label_mensaje.text = "Solo letras, números y guión bajo (_)"
            return


        if len(nombre) < 3:
            self.label_mensaje.text = "El usuario debe tener mínimo 3 caracteres"
            return

        if len(contrasena) < 4:
            self.label_mensaje.text = "La contraseña debe tener mínimo 4 caracteres"
            return

        if contrasena != confirmar:
            self.label_mensaje.text = "Las contraseñas no coinciden"
            return

        exito, mensaje = registrar_usuario(nombre, contrasena)
        if exito:
            usuario_activo = nombre
            cargar_progreso()
            self.label_mensaje.color = (0.3, 1, 0.3, 1)
            self.label_mensaje.text = "¡Registro exitoso!"
            anim = (
                Animation(background_color=(0.0, 0.8, 0.3, 1), duration=0.15) +
                Animation(background_color=(0.0, 0.5, 0.2, 1), duration=0.15) +
                Animation(background_color=(0.0, 0.8, 0.3, 1), duration=0.15) +
                Animation(background_color=(0.1, 0.1, 0.15, 1), duration=0.2)
            )
            anim.start(self.btn_registrar)
            Clock.schedule_once(lambda dt: self.ir_bienvenida(), 0.7)

        else:
            self.label_mensaje.text = mensaje

    def ir_bienvenida(self):
        self.manager.transition = FadeTransition(duration=0.15)
        self.manager.current = 'bienvenida'


    def ir_login(self, instance):
        self.manager.transition = FadeTransition(duration=0.15)
        self.manager.current = 'login'

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos


    def on_pre_enter(self):

        self.layout.opacity = 1

        widgets = [
            self.titulo,
            self.subtitulo,
            self.campo_usuario,
            self.campo_contrasena,
            self.campo_confirmar,
            self.label_mensaje
        ]

        for widget in widgets:
            widget.opacity = 0

        Clock.schedule_once(self.animar_entrada, 0.05)


    def animar_entrada(self, dt):

        widgets = [
            self.titulo,
            self.subtitulo,
            self.campo_usuario,
            self.campo_contrasena,
            self.campo_confirmar,
            self.label_mensaje
        ]

        delay = 0

        for widget in widgets:

            anim = Animation(
                opacity=1,
                duration=0.35
            )

            anim.start(widget)

            delay += 0.03


# 🔹 BIENVENIDA PRO CON BOTÓN
class Bienvenida(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        layout = self.layout

        # 🔥 Fondo oscuro
        with self.canvas.before:
            Color(*tema_actual["fondo_secundario"])
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self.update_rect, pos=self.update_rect)

        # 🔥 TÍTULO
        self.titulo = Label(
            text='Reto 30 Días',
            font_size=60,
            bold=True,
            opacity=0
        )

        # 🔥 SUBTÍTULO
        self.subtitulo = Label(
            text='Construye disciplina cada día',
            font_size=28,
            color=(0.7, 0.7, 0.7, 1),
            opacity=0
        )

        # 🔥 FRASE
        self.frase = Label(
            text='',
            font_size=24,
            color=(0.5, 0.8, 1, 1),
            opacity=1,
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=120
        )
        self.frase.bind(size=self.frase.setter('text_size'))

        # 🔥 BOTÓN COMENZAR
        self.btn = Button(
            text='Comenzar',
            font_size=22,
            size_hint_y=None,
            height=80,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1),
            opacity=0
        )

        self.btn.bind(on_press=self.entrar)
        self.btn.bind(on_press=self.animar_boton)

        # Agregar todo
        layout.add_widget(self.titulo)
        layout.add_widget(self.subtitulo)
        layout.add_widget(self.frase)
        layout.add_widget(self.btn)

        self.add_widget(layout)

        # 🔥 FONDO PARTÍCULAS
        self.particulas = []

        with self.canvas.before:
            Color(*tema_actual["fondo_secundario"])
            self.fondo_rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.actualizar_fondo, pos=self.actualizar_fondo)

        # 🔥 Animación entrada
        Clock.schedule_once(self.animar, 0.5)

    def on_pre_enter(self):
        self.titulo.text = 'Reto 30 Días'
        self.frase_completa = random.choice(frases)
        self.frase.text = ''
        self.indice_letra = 0
        self.titulo.opacity = 0
        self.subtitulo.opacity = 0
        self.frase.opacity = 1
        self.btn.opacity = 0
        Clock.schedule_once(self.iniciar_particulas, 0.1)
        Clock.schedule_once(self.animar_titulo, 0.3)

    def on_leave(self):
        self.particulas_activas = False
        Clock.unschedule(self.actualizar_particulas)
        Clock.unschedule(self.escribir_letra)
        self.canvas.after.clear()

    def iniciar_particulas(self, dt):
        self.particulas_activas = True
        self.particulas = []

        for _ in range(40):
            self.particulas.append({
                'x': random.uniform(0, self.width),
                'y': random.uniform(0, self.height),
                'tamanio': random.uniform(1, 4),
                'velocidad': random.uniform(0.1, 0.4),
                'opacidad': random.uniform(0.15, 0.45),
                'tipo': random.choice(['blanco', 'azul', 'cyan'])
            })
        Clock.schedule_interval(self.actualizar_particulas, 1/60)

    def actualizar_particulas(self, dt):
        if not getattr(self, 'particulas_activas', False):
            return
        self.canvas.after.clear()

        with self.canvas.after:

            for p in self.particulas:

                p['y'] += p['velocidad']

                if p['y'] > self.height + 10:
                    p['y'] = -10
                    p['x'] = random.uniform(0, self.width)

                if p['tipo'] == 'blanco':
                    KivyColor(1, 1, 1, p['opacidad'])

                elif p['tipo'] == 'azul':
                    KivyColor(0.2, 0.5, 1, p['opacidad'])

                elif p['tipo'] == 'cyan':
                    KivyColor(0, 0.8, 1, p['opacidad'])

                Ellipse(
                    pos=(p['x'], p['y']),
                    size=(p['tamanio'], p['tamanio'])
                )


    def animar_titulo(self, dt):
        Animation(opacity=1, duration=0.8).start(self.titulo)
        Animation(opacity=1, duration=0.8).start(self.subtitulo)
        Clock.schedule_once(self.iniciar_escritura, 1.0)

    def iniciar_escritura(self, dt):
        self.indice_letra = 0
        self.frase.text = ''
        Clock.schedule_interval(self.escribir_letra, 0.05)

    def escribir_letra(self, dt):
        if self.indice_letra < len(self.frase_completa):
            self.indice_letra += 1
            self.frase.text = self.frase_completa[:self.indice_letra] + '|'
        else:
            self.frase.text = self.frase_completa
            Clock.unschedule(self.escribir_letra)
            Clock.schedule_once(self.mostrar_boton, 0.5)

    def mostrar_boton(self, dt):
        Animation(opacity=1, duration=0.6).start(self.btn)

    # 🔥 Animación de entrada (mantener por compatibilidad)
    def animar(self, dt):
        Animation(opacity=1, duration=1).start(self.titulo)
        Animation(opacity=1, duration=1).start(self.subtitulo)
        Animation(opacity=1, duration=1).start(self.frase)
        Animation(opacity=1, duration=1).start(self.btn)

    # 🔥 Animación botón
    def animar_boton(self, instance):
        anim = Animation(background_color=(0.25, 0.25, 0.4, 1), duration=0.1) + \
               Animation(background_color=(0.1, 0.1, 0.15, 1), duration=0.2)
        anim.start(instance)


    # 🔥 Ir al menú
    def entrar(self, instance):
        self.manager.transition = FadeTransition(duration=0.15)
        self.manager.current = 'inicio'

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def actualizar_fondo(self, *args):
        self.fondo_rect.size = self.size
        self.fondo_rect.pos = self.pos


    def actualizar_tema(self):

        self.canvas.before.clear()

        with self.canvas.before:
            Color(*tema_actual["fondo_secundario"])
            self.rect = Rectangle(size=self.size, pos=self.pos)
            Color(*tema_actual["fondo_secundario"])
            self.fondo_rect = Rectangle(size=self.size, pos=self.pos)

            self.rect = Rectangle(
                size=self.layout.size,
                pos=self.layout.pos
            )

        self.titulo.color = tema_actual["texto"]

        self.subtitulo.color = tema_actual["texto_secundario"]

        self.btn.background_color = tema_actual["boton"]

        self.layout.bind(size=self.update_rect, pos=self.update_rect)


# 🔹 APP
class vntn1(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(PantallaLogin(name='login'))
        sm.add_widget(PantallaRegistro(name='registro'))
        sm.add_widget(Bienvenida(name='bienvenida'))
        sm.add_widget(Inicio(name='inicio'))

        sm.add_widget(PantallaReto("Reto Hábitos", tareas_habitos, name='habitos'))
        sm.add_widget(PantallaReto("Reto Ejercicio", tareas_ejercicio, name='ejercicio'))
        sm.add_widget(PantallaReto("Reto Dinero", tareas_dinero, name='dinero'))

        return sm

vntn1().run()