# LIBRERÍAS
import tkinter as tk

# Ventana
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.config(bg="#727EFF")
ventana.title("Mi app")


boton = tk.Button(ventana,text="Agregar")
boton.pack()

campo_texto = tk.Entry(ventana)
campo_texto.pack()

lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()


ventana.mainloop()