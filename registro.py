from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import FadeTransition

from tema import tema_actual
from progreso import cargar_progreso
from usuarios import registrar_usuario

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
            from progreso import cargar_progreso, set_usuario
            set_usuario(nombre)
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

        self.label_mensaje.text = ''
        self.label_mensaje.color = (1, 0.3, 0.3, 1)

        self.campo_usuario.text = ''
        self.campo_contrasena.text = ''
        self.campo_confirmar.text = ''

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
