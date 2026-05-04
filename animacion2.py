from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class AnimatedButton(Button):

    def animacion_rebote(self):
        # Efecto de salto y rebote con cambio de color de letra
        orig_y = self.pos_hint.get('center_y', 0.5)
        anim = Animation(pos_hint={'center_y': orig_y + 0.2}, duration=0.2, t='out_quad')
        anim += Animation(pos_hint={'center_y': orig_y}, color=(1, 0, 0, 1), duration=1, t='out_bounce')
        anim += Animation(color=(1, 1, 1, 1), duration=0.5)
        anim.start(self)

    def animacion_original(self):
        # Cambios de tamaño, posición lateral y colores de fondo
        start_color = self.background_color
        start_size_h = self.size_hint
        start_pos_hint = self.pos_hint.copy()
        start_font_size = self.font_size

        animate = Animation(background_color=(0, 0, 1, 1), duration=1.5)
        animate += Animation(size_hint=(0.4, 0.4))
        animate += Animation(font_size=35)
        animate += Animation(size_hint=(.3, .1), font_size=14, background_color=(1, 1, 0, 1), duration=1.5)
        animate += Animation(pos_hint={'center_x': 0.8}, background_color=(0, 1, 1, 1))
        animate += Animation(pos_hint={'center_x': 0.2}, background_color=(0, 0, 1, 1), duration=0.5)
        
        back = Animation(background_color=start_color, size_hint=start_size_h, 
                         pos_hint=start_pos_hint, font_size=start_font_size)
        
        (animate + back).start(self)

    def animacion_pulso(self):
        # Guardar tamaño original
        orig_size = self.size_hint

        # Animación de agrandar + bajar opacidad
        anim = Animation(size_hint=(orig_size[0] + 0.05, orig_size[1] + 0.05),
                         opacity=0.6,
                         duration=0.4)

        # Volver a normal
        anim += Animation(size_hint=orig_size,
                          opacity=1,
                          duration=0.4)

        # Repetir infinito
        anim.repeat = True
        anim.start(self)


class MyApp(App):
    def build(self):
        layout = FloatLayout()
        
        txt = Label(text='Tres botones con efectos distintos', 
                    pos_hint={'center_x': 0.5, 'center_y': 0.8})

        # BOTÓN 1: Rebote
        btn1 = AnimatedButton(text='Rebote y Letras', 
                              size_hint=(0.3, 0.1), 
                              pos_hint={'center_x': 0.5, 'center_y': 0.6})
        btn1.bind(on_press=lambda x: btn1.animacion_rebote())

        # BOTÓN 2: Secuencia original
        btn2 = AnimatedButton(text='Efecto Original', 
                              size_hint=(0.3, 0.1), 
                              pos_hint={'center_x': 0.5, 'center_y': 0.4})
        btn2.bind(on_press=lambda x: btn2.animacion_original())

        # BOTÓN 3: Pulso (nuevo)
        btn3 = AnimatedButton(text='Pulso PRO', 
                              size_hint=(0.3, 0.1), 
                              pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn3.bind(on_press=lambda x: btn3.animacion_pulso())

        layout.add_widget(txt)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout


if __name__ == '__main__':
    MyApp().run()