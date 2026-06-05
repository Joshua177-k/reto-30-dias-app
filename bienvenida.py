from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.screenmanager import FadeTransition
from kivy.graphics import Ellipse
from kivy.graphics import Color as KivyColor

import random

from tema import tema_actual
from tareas import frases


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