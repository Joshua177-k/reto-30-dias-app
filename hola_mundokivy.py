from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

# Opcional: Cambiar color de fondo de la ventana (R, G, B, A)
Window.clearcolor = (0.2, 0.4, 0.6, 1)

class TestApp(App):
    def build(self):
        # Creamos un botón con texto y tamaño específico
        btn = Button(
            text='¡Hola Cindy!\nPresiona aquí',
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size='20sp'
        )
        
        # Le asignamos una función al presionar
        btn.bind(on_press=self.saludar)
        return btn

    def saludar(self, instance):
        instance.text = "¡Funciona perfectamente! 🚀"
        print("Botón presionado en VS Code")

if __name__ == '__main__':
    TestApp().run()