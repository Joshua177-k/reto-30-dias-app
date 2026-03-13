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
fuente = pygame.font.SysFont("bauhaus93", 58)         #Botón jugar
fuente_titulo = pygame.font.SysFont("jokerman", 40)     #Titulo
fuente_reaction = pygame.font.SysFont("chiller", 80)  #Reacción
fuente_nueva = pygame.font.SysFont("ravie", 34)       # Boton jugar de nuevo

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
                if 200 < mouse_x < 480 and 450 < mouse_y < 580:
                    estado = "jugando"
                    tiempo_inicio = pygame.time.get_ticks()

            # Detectar clic en botón de jugar de nuevo
            if estado == "resultado":
        
                if 200 < mouse_x < 480 and 450 < mouse_y < 530:
                    estado = "jugando"

                    # Resetear variables para nueva partida
                    luz = "rojo"
                    reaccion = 0
                    tiempo_inicio = pygame.time.get_ticks()
                    tiempo_verde = 0
                 

        # Detectar cuando el jugador presiona espacio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and luz == "verde" and reaccion == 0:
                reaccion = pygame.time.get_ticks() - tiempo_verde
                estado = "resultado"
        

    if estado == "menu":
        # Botón de Jugar
        pygame.draw.rect(pantalla, (0, 180, 220), (200, 450, 280, 130))

        # Texto Botón
        texto = fuente.render("¡Jugar!", True, (0, 0, 0))
        pantalla.blit(texto, (247, 480))

        # Titulo Ventana
        texto_titulo = fuente_titulo.render("¡PON A PRUEBA TUS REFLEJOS!", True, (255, 255, 255))
        pantalla.blit(texto_titulo, (27, 100))


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
        pygame.draw.rect(pantalla, (0, 180, 220), (170, 450, 365, 80))
        texto_nuevo = fuente_nueva.render("Jugar de nuevo", True, (0, 0, 0))
        pantalla.blit(texto_nuevo, (185, 465))

    pygame.display.flip()

