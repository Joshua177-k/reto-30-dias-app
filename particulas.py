# particulas.py

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Ellipse
from kivy.graphics import Color as KivyColor

import random


class FondoParticulas(Widget):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.particulas = []

        Clock.schedule_once(self.iniciar, 0.1)

    def iniciar(self, dt):

        self.canvas.clear()

        self.particulas = []

        for _ in range(40):

            self.particulas.append({

                'x': random.uniform(0, self.width),
                'y': random.uniform(0, self.height),
                'tamanio': random.uniform(2, 6),
                'velocidad': random.uniform(0.2, 0.8),
                'opacidad': random.uniform(0.1, 0.5)

            })

        Clock.schedule_interval(self.actualizar, 1/60)

    def actualizar(self, dt):

        self.canvas.clear()

        with self.canvas:

            for p in self.particulas:

                p['y'] += p['velocidad']

                if p['y'] > self.height:
                    p['y'] = 0

                KivyColor(1, 1, 1, p['opacidad'])

                Ellipse(
                    pos=(p['x'], p['y']),
                    size=(p['tamanio'], p['tamanio'])
                )