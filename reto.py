from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import FadeTransition

from tema import tema_actual

import progreso
from progreso import guardar_progreso

from tareas import (
    tareas_habitos,
    tareas_ejercicio,
    tareas_dinero
)

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

        # 🔹 BARRA SUPERIOR
        top_bar = BoxLayout(
            size_hint_y=None,
            height=60,
            spacing=10
        )

        btn_volver_top = Button(
            text='<',
            font_size=28,
            size_hint=(None, None),
            size=(50, 50),
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
        )

        btn_volver_top.bind(on_press=self.volver)

        self.titulo = Label(
            text=titulo_texto,
            font_size=35
        )

        top_bar.add_widget(btn_volver_top)
        top_bar.add_widget(self.titulo)

        self.layout.add_widget(top_bar)


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
                i == 0 or progreso.progreso_global[self.name][i - 1]
            )

            completado = progreso.progreso_global[self.name][i]

            # 🔓 RETO DESBLOQUEADO
            if desbloqueado:

                texto = (
                    f"[b]{tarea['tarea']}[/b]\n"
                    f"[size=14][color=aaaaaa]Día {tarea['dia']}[/color][/size]"
                )

                label = Label(
                    text=texto,
                    halign='center',
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
        if progreso.progreso_global[self.name][i]:

            progreso.progreso_global[self.name][i] = False

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

            progreso.progreso_global[self.name][i] = True

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
        self.completados = sum(progreso.progreso_global[self.name])
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
        self.completados = sum(progreso.progreso_global[self.name])
        self.label_progreso.text = f"{self.completados}/30 completados"
        self.actualizar_barra()
        self.actualizar_botones()
    

    def actualizar_botones(self):
        for fila, i in self.filas:
            btn = fila.children[0]

            if btn.disabled:
                continue

            if progreso.progreso_global[self.name][i]:
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
        color_apagado = (0.05, 0.05, 0.08, 1)

        self.btn_todas.background_color = color_apagado
        self.btn_pendientes.background_color = color_apagado
        self.btn_completadas.background_color = color_apagado

        if filtro == 'todas':
            self.btn_todas.background_color = (0.2, 0.7, 1, 1)

        elif filtro == 'pendientes':
            self.btn_pendientes.background_color = (0.2, 0.7, 1, 1)

        elif filtro == 'completadas':
            self.btn_completadas.background_color = (0.2, 0.7, 1, 1)

        # mostrar / ocultar filas
        for fila, i in self.filas:

            completada = progreso.progreso_global[self.name][i]

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

            if progreso.progreso_global[self.name][i]:
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