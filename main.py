from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window      # <-- agrega esta
from kivy.utils import platform

if platform != 'android':
    Window.size = (400, 700)
    
from login import PantallaLogin
from registro import PantallaRegistro
from bienvenida import Bienvenida
from inicio import Inicio
from reto import PantallaReto

from tareas import (
    tareas_habitos,
    tareas_ejercicio,
    tareas_dinero
)

class Reto30App(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(PantallaLogin(name='login'))
        sm.add_widget(PantallaRegistro(name='registro'))
        sm.add_widget(Bienvenida(name='bienvenida'))
        sm.add_widget(Inicio(name='inicio'))

        sm.add_widget(
            PantallaReto(
                "Reto Hábitos",
                tareas_habitos,
                name='habitos'
            )
        )

        sm.add_widget(
            PantallaReto(
                "Reto Ejercicio",
                tareas_ejercicio,
                name='ejercicio'
            )
        )

        sm.add_widget(
            PantallaReto(
                "Reto Dinero",
                tareas_dinero,
                name='dinero'
            )
        )

        return sm

Reto30App().run()