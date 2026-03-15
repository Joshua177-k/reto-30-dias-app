#IMPORTAR LIBBRERÍAS
import pygame

#Inicializar pygame
pygame.init()

# Estado inicial del juego
estado = "menu"

# Configurar ventana
ANCHO, ALTO = 689, 725

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Pon a Prueba tus reflejos!")

# Posición del semáforo en la ventana 
x, y = 270, 100


# TAMAÑO Y TIPO DE TEXTOS
fuente = pygame.font.SysFont("stencil", 50)         #Botón jugar
fuente_titulo = pygame.font.SysFont("stencil", 45)     #Titulo
fuente_reaction = pygame.font.SysFont("chiller", 80)  #Reacción
fuente_nueva = pygame.font.SysFont("ravie", 34)       # Boton jugar de nuevo
fuente_historial = pygame.font.SysFont("stencil", 40)  # Boton historial
fuente_pj = pygame.font.SysFont("ravie", 40)           # botón de volver al menu en ventana de puntajes 
fuente_puntajes5 = pygame.font.SysFont("stencil", 60)  # 5 puntajes 
fuente_menu = pygame.font.SysFont("ravie", 40)         # Botón volver al menu en ventana del puntaje
fuente_jugar = pygame.font.SysFont("ravie", 40)        # Botón Jugar en ventana de puntajes
fuente_tit_pj = pygame.font.SysFont("stencil", 55)     # Título "puntajes"
fuente_msj = pygame.font.SysFont("seguiemoji", 60)       # Mensaje de Reaccion "todos"



# Estado inicial del semáforo
luz = "rojo"
tiempo_inicio = 0

# Momento en el que el semáforo se pone en verde
tiempo_verde = 0

# Tiempo de reacción del usuario en ms
reaccion = 0



#       LOOP

while True:

#Color fondo de la ventana  
    pantalla.fill((70, 70, 70))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        # Verificar si el clic fue en el botón
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if estado == "menu":
                if 100 < mouse_x < 320 and 515 < mouse_y < 605:
                    estado = "jugando"
                    tiempo_inicio = pygame.time.get_ticks()

                #Detectar clic en botón de puntajes
                elif 375 < mouse_x < 595 and 515 < mouse_y < 605:
                    estado = "historial"

            # Detectar clic en botón de jugar de nuevo
            elif estado == "resultado":
        
                if 200 < mouse_x < 480 and 450 < mouse_y < 530:
                    estado = "jugando"

                    # Resetear variables para nueva partida
                    luz = "rojo"
                    reaccion = 0
                    tiempo_inicio = pygame.time.get_ticks()
                    tiempo_verde = 0

                if 170 < mouse_x < 535 and 550 < mouse_y < 630:
                    estado = "menu"
                    luz = "rojo"
                    reaccion = 0
                    tiempo_verde = 0

            # Pantalla de historial de puntajes
            elif estado == "historial":
                if 170 < mouse_x < 535 and 575 < mouse_y < 655:
                    estado = "menu"
                
                if 200 < mouse_x < 500 and 480 < mouse_y < 560:
                    estado = "jugando"
                    luz = "rojo"
                    reaccion = 0
                    tiempo_inicio = pygame.time.get_ticks()
                    tiempo_verde = 0







        # Detectar cuando el jugador presiona espacio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and luz == "verde" and reaccion == 0:
                reaccion = pygame.time.get_ticks() - tiempo_verde
                estado = "resultado"
                ms = reaccion % 1000
                segundos = (reaccion // 1000) % 60
                minutos = reaccion // 60000
                with open("historial.txt", "a") as archivo:
                    archivo.write(f"{minutos:02d}:{segundos:02d}:{ms:03d}\n")

    if estado == "menu":

        # ------ BOTONES ------

        # Botón de Jugar
        pygame.draw.rect(pantalla, (0, 0, 220), (100, 515, 220, 90), border_radius=24)

        # Botón de historial de records
        pygame.draw.rect(pantalla, (0, 0, 220), (375, 515, 220, 90), border_radius=24)

        # Texto Botón
        texto = fuente.render("¡Jugar!", True, (0, 0, 0))
        pantalla.blit(texto, (113, 540))

        # Texto Historial
        texto_historial = fuente_historial.render("Puntajes", True, (0, 0, 0))
        pantalla.blit(texto_historial, (388, 546))

        # Titulo Ventana
        texto_titulo = fuente_titulo.render("¡PON A PRUEBA TUS REFLEJOS!", True, (255, 255, 255))
        pantalla.blit(texto_titulo, (23, 100))


#   DUBUJO DE ELEMENTOS GRAFICOS

    if estado == "jugando":
        
        # Semaforo
        pygame.draw.rect(pantalla, (30, 30, 30), (x, y, 140,300))

        # Circulo 1
        color_rojo = (255, 0, 0) if luz == "rojo" else (80, 0, 0)
        pygame.draw.circle(pantalla, color_rojo, (340, 150), 40)

        # Circulo 2
        color_amarillo = (255, 255, 0) if luz == "amarillo" else (80, 80, 0)
        pygame.draw.circle(pantalla, color_amarillo, (340, 250), 40)
        
        # Circulo 3
        color_verde = (0, 255, 0) if luz == "verde" else (0, 80, 0)
        pygame.draw.circle(pantalla, color_verde, (340, 350), 40)


        # Logica de cambio de luces del semáforo  
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_inicio > 2000 and luz == "rojo":
            luz = "amarillo"
        elif tiempo_actual - tiempo_inicio > 4000 and luz != "verde":
            luz = "verde"
            tiempo_verde = pygame.time.get_ticks()

        # Convertir milisegundos a formato minutos:segundos:ms
        ms = reaccion % 1000
        segundos = (reaccion // 1000) % 60
        minutos = reaccion // 60000

        texto_reaccion = fuente_reaction.render(f"Tu reacción: {minutos:02d}:{segundos:02d}:{ms:03d}", True, (255, 255, 255))
        pantalla.blit(texto_reaccion, (50,549))


        # Pantalla de resultado
    if estado == "resultado":       

        # Convertir y mostrar tiempo de reacción
        ms = reaccion % 1000

        segundos = (reaccion // 1000) % 60
        minutos = reaccion // 60000
        texto_reaccion = fuente_reaction.render(f"Tu reacción: {minutos:02d}:{segundos:02d}:{ms:03d}", True, (255, 255, 255))
        pantalla.blit(texto_reaccion, (70, 300))

        # Botón de jugar de nuevo
        pygame.draw.rect(pantalla, (0, 0, 220), (170, 450, 365, 80), border_radius=24)
        texto_nuevo = fuente_nueva.render("Jugar de nuevo", True, (0, 0, 0))
        pantalla.blit(texto_nuevo, (185, 475))

        # Botón de volver al menu (venana de puntaje normal)
        pygame.draw.rect(pantalla, (0, 0, 220), (170, 550, 365, 80), border_radius=24)
        texto_mn = fuente_menu.render("MENÚ", True, (0, 0, 0))
        pantalla.blit(texto_mn, (280, 570))

        # Primer mensaje Reaccion
        if reaccion <= 200:
            texto_msj = fuente_msj .render("⚡⚡ Eres un rayo!⚡⚡", True, (0, 255, 0))
            pantalla.blit(texto_msj, (121, 120))

        # Segundo mensaje Reaccion
        elif reaccion <= 400:
            texto_msj = fuente_msj.render("BIENNN!", True, (0, 255, 0))
            pantalla.blit(texto_msj, (121, 120))
        
        # Tercer mensaje Reaccion
        elif reaccion <= 600:
            texto_msj = fuente_msj.render("Puedes hacerlo mejor!!", True, (0, 255, 0))
            pantalla.blit(texto_msj, (99, 120))
        
        # Cuarto mensaje Reaccion
        else:
            texto_msj = fuente_msj.render("M U U U Y  LENtoooo", True, (0, 255, 0))
            pantalla.blit(texto_msj, (88, 120))

        




    if estado == "historial":    
        with open("historial.txt", "r") as archivo:
            lineas = archivo.readlines()
            ultimos = lineas[-5:]
        for i, linea in enumerate(ultimos):
            texto_linea = fuente_puntajes5.render(linea.strip(), True, (0, 255, 0))
            pantalla.blit(texto_linea, (211, 165 + i * 60))

        # Botón de volver al menu (puntajes)
        pygame.draw.rect(pantalla, (0, 0, 220), (200, 575, 300, 80), border_radius=24)
        texto_pj = fuente_pj.render("MENÚ", True, (0, 0, 0))
        pantalla.blit(texto_pj, (272, 589))

        # Botón de jugar (puntajes)
        pygame.draw.rect(pantalla, (0, 0, 220), (200, 480, 300, 80), border_radius=24)
        texto_jugar = fuente_jugar.render("¡JUGAR!", True, (0, 0, 0))
        pantalla.blit(texto_jugar, (254, 503))  

        #titulo puntajes
        texto_titulopj = fuente_tit_pj.render("Puntajes", True, (0, 0, 0))
        pantalla.blit(texto_titulopj, (216  , 70))

    pygame.display.flip()

