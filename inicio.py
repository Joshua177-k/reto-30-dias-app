from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
from progreso import get_usuario

from tema import (
    tema_actual,
    cambiar_tema
)

import progreso
from progreso import progreso_vacio

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

        self.progreso_h = sum(progreso.progreso_global["habitos"]) / 30
        self.progreso_e = sum(progreso.progreso_global["ejercicio"]) / 30
        self.progreso_d = sum(progreso.progreso_global["dinero"]) / 30

        Animation.cancel_all(self.rect_barra_habitos)
        Animation.cancel_all(self.rect_barra_ejercicio)
        Animation.cancel_all(self.rect_barra_dinero)

        anim = Animation(duration=0.4)
        anim.bind(on_progress=self.animar_barras)
        anim.start(self)


    def on_pre_enter(self):
        self.subtitulo.text = f'¡Hola {get_usuario()}!'
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

        progreso.progreso_global = progreso_vacio()

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
