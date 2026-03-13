import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Prueba Pygame")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Jugador
x, y = 300, 200
velocidad = 5
tam = 40

# Reloj
reloj = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Dibujar
    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, AZUL, (x, y, tam, tam))
    pygame.display.flip()

    # FPS
    reloj.tick(60)