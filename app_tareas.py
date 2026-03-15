

tareas = []

#Función que imprime menú
def mostrar_menu():
    # MENÚ
    print("1. Ver Tareas")
    print("2. Agregar Tareas")
    print("3. Eliminar Tarea")
    print("4. Salir")
    
def ver_tareas():
    if not tareas:
        print("✖️ No hay tareas 😊")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(i, tarea)

def agregar_tareas():
    nueva_tarea = input("Escribe la tarea 📄")
    print("✅ ¡Tarea agregada!")
    tareas.append(nueva_tarea)



def eliminar_tarea():
    ver_tareas()
    numero_usuario = int(input("Escribe el numero de tarea que deseas eliminar"))
    indice = numero_usuario - 1
    tareas.pop(indice)
    print("✅ ¡Tarea eliminada!")





while True:
    mostrar_menu()
    opcion = input("Escoge un numero:")

    if opcion == "1":
        ver_tareas()

    elif opcion == "2":
        agregar_tareas()

    elif opcion == "3":
        eliminar_tarea()

    elif opcion == "4":
        break


    