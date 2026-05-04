# Importar librerías necesarias

import tkinter as tk
import random


# CREACIÓN DE VENTANA
ventana = tk.Tk()
ventana.geometry("900x700")
ventana.config(bg="#43A1D1")

# Titulo de ventana 
titulo = tk.Label(ventana, text = "Piedra / Papel / Tijera", font = ("Impact", 54), fg = "#0C5727", bg="#43A1D1")
titulo.pack()

# FUNCIÓN 
def jugar():
    resultado = random.choice(["🪨", "🧻", "✂️"])
    emoji_label.config(text=resultado)



# Botón Principal
boton = tk.Button(ventana, text="JUGAR", font=("Arial", 39), fg="yellow", bg="#531384", command=jugar)

emoji_label = tk.Label(ventana, text="", font=("Arial", 184), bg="#43A1D1")
emoji_label.pack()

boton.pack(pady=100)

ventana.mainloop()