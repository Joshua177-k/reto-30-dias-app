from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage # Importamos Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle

# Clase base para pantallas con fondo azul oscuro
class BlueScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(255, 0, 0, 1)  # Azul marino de fondo
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


# 1. Clase personalizada para botones CON COLOR
class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', bcolor=(0, 0, 255, 1), **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
        self.background_color = bcolor # Establece el color (R, G, B, A)
        self.background_normal = ''     # Esto hace que el color sea más vibrante/plano

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
    
# 2. Pantalla Principal
class MainScr(BlueScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        # --- SECCIÓN DE IMAGEN ---
        # Opción A: Imagen local 
        # logo = Image(source='tu_imagen.png', size_hint=(1, 0.5))
        
        # Opción B: Imagen desde internet (útil para pruebas rápidas)
        logo = AsyncImage(
            source='futbol.jpg',
            size_hint=(1, 0.4)
        )
        layout.add_widget(logo)
        # -------------------------

        layout.add_widget(Label(text='MENÚ PRINCIPAL', font_size='28sp', bold=True, size_hint=(1, 0.2)))
        
        layout.add_widget(ScrButton(self, direction='down', goal='first', text="Verde", bcolor=(0.2, 0.8, 0.2, 1)))
        layout.add_widget(ScrButton(self, direction='left', goal='second', text="Amarillo", bcolor=(1, 0.8, 0, 1)))
        
        self.add_widget(layout)

# 3. Primera Pantalla
class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn = Button(text='Elección: 1')
        btn_back = ScrButton(self, direction='up', goal='main', text="Back")
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)

# 4. Segunda Pantalla (Completada)
class SecondScr(BlueScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        l = BoxLayout(orientation='vertical')
        l.add_widget(Label(text="Pantalla 2"))
        l.add_widget(Button(text="Volver", on_press=lambda x: setattr(self.manager, 'current', 'main')))
        self.add_widget(l)

# 5. Pantallas Genéricas (Para que no de error al presionar 3 o 4)
class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ScrButton(self, direction='down', goal='main', text="Pantalla 3 - Volver"))

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ScrButton(self, direction='left', goal='main', text="Pantalla 4 - Volver"))

# 6. Clase Principal de la Aplicación
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm

if __name__ == '__main__':
    MyApp().run()