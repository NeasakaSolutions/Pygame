# Importaciones de librerias:
import pygame
import sys
from pygame.locals import QUIT

# Dimensiones de la ventana:
ancho = 400
alto = 300

'''Colores primarios:
White == 0 
RGB (RED, GREEN, BLUE)'''

color = (0, 140, 60)
color2 = pygame.Color('#FF7809')

# Sentencia obligaoria para el uso de pygame
pygame.init()

# Ventana
ventana = pygame.display.set_mode((ancho, alto))
# Titulo de la ventana
pygame.display.set_caption('Ijole')

while True:
    ventana.fill(color2)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()




