from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import FadeTransition

from datetime import datetime

from tema import tema_actual
import progreso
from progreso import cargar_progreso
from usuarios import iniciar_sesion




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
            progreso.set_usuario(nombre)
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