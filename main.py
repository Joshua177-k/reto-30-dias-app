from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
from kivy.animation import Animation

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


# 🔹 MENÚ PRINCIPAL
class Inicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=25)

        with layout.canvas.before:  
            Color(0.05, 0.05, 0.08, 1)  # fondo oscuro elegante
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self.update_rect, pos=self.update_rect)

        titulo = Label(
            text='Mi Reto 30 Días',
            font_size=48,
            bold = True,
            size_hint_y=None,
            height=80
)
        subtitulo = Label(
            text='Desafíos diarios',
            font_size=22,
            color=(0.7, 0.7, 0.7, 1),
            size_hint_y=None,
            height=40
        )

        titulo.bind(size=titulo.setter('text_size'))

        card1 = Button(
            text='Reto Hábitos',
            font_size=24,
            size_hint_y=None,
            height=120,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
)      
        card1.bind(on_press=lambda x: self.animar_card(x))
        card1.bind(on_press=lambda x: self.cambiar('habitos'))

        card2 = Button(
            text='Reto Ejercicio',
            font_size=24,
            size_hint_y=None,
            height=120,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
)
        card2.bind(on_press=lambda x: self.animar_card(x))
        card2.bind(on_press=lambda x: self.cambiar('ejercicio'))

        card3 = Button(
            text='Reto Dinero',
            font_size=24,
            size_hint_y=None,
            height=120,
            background_normal='',
            background_color=(0.1, 0.1, 0.15, 1)
)
        card3.bind(on_press=lambda x: self.animar_card(x))
        card3.bind(on_press=lambda x: self.cambiar('dinero'))

        layout.add_widget(titulo)
        layout.add_widget(subtitulo)
        layout.add_widget(card1)
        layout.add_widget(card2)
        layout.add_widget(card3)

        self.add_widget(layout)

    def animar_card(self, instance):
        
        #Animación al presionar
        anim = Animation(background_color=(0.25, 0.25, 0.4, 1), duration=0.1) + \
               Animation(background_color=(0.1, 0.1, 0.15, 1), duration=0.2)
        anim.start(instance)

    def cambiar(self, pantalla):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = pantalla

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

# 🔹 PANTALLA DE RETO
class PantallaReto(Screen):
    def __init__(self, titulo_texto, tareas, **kwargs):
        super().__init__(**kwargs)

        self.sonido = SoundLoader.load('click.mp3')

        self.completados = 0

        scroll = ScrollView()

        self.layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15,
            size_hint_y=None
        )

        self.layout.bind(minimum_height=self.layout.setter('height'))

        # 🔹 TÍTULO
        titulo = Label(text=titulo_texto, font_size=35, size_hint_y=None, height=60)
        self.layout.add_widget(titulo)

        # 🔹 PROGRESO
        self.label_progreso = Label(
            text='0/30 completados',
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.layout.add_widget(self.label_progreso)

        # 🔹 LISTA DE TAREAS
        for tarea in tareas:
            texto = f"Día {tarea['dia']}: {tarea['tarea']}"

            fila = BoxLayout(size_hint_y=None, height=70, padding=10)

            label = Label(
                text=texto,
                halign='left',
                valign='middle'
            )
            label.bind(size=label.setter('text_size'))

            btn = Button(
                text='Completar',
                size_hint_x=0.3,
                background_normal='',
                background_color= "#3890E8D7"
            )

            btn.bind(on_press=self.completar)

            fila.add_widget(label)
            fila.add_widget(btn)

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

        btn_volver.bind(on_press=self.volver)

        self.layout.add_widget(btn_volver)

        scroll.add_widget(self.layout)
        self.add_widget(scroll)

    def completar(self, instance):
        if self.sonido:
            self.sonido.play()

        if instance.text != "✔ Completado":
            instance.text = "✔ Completado"
            anim = Animation(background_color=("#0A55A0D6"), duration=0.3)
            anim.start(instance)
            instance.background_color = ("#0A55A0D6")

            self.completados += 1
            self.label_progreso.text = f"{self.completados}/30 completados"

    def volver(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'inicio'


# 🔹 BIENVENIDA
class Bienvenida(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout()
        texto = Label(text='APP DE RETOS', font_size=50)

        layout.add_widget(texto)
        self.add_widget(layout)

        Clock.schedule_once(self.ir_menu, 2)

    def ir_menu(self, dt):
        self.manager.current = 'inicio'


# 🔹 APP
class vntn1(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(Bienvenida(name='bienvenida'))
        sm.add_widget(Inicio(name='inicio'))

        sm.add_widget(PantallaReto("Reto Hábitos", tareas_habitos, name='habitos'))
        sm.add_widget(PantallaReto("Reto Ejercicio", tareas_ejercicio, name='ejercicio'))
        sm.add_widget(PantallaReto("Reto Dinero", tareas_dinero, name='dinero'))

        return sm


vntn1().run()