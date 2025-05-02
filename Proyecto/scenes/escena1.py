# Importaciones
import pygame
from pygame.locals import QUIT
import sys
from settings import ancho, alto, fps

# Se crea la clase de escena 1
class Escena1():
    
    def __init__(self):

        # Configuracion de la pantalla de la escena 1
        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption('Escena 1 - Bosque')

        # Configurar fondo de la imagen
        self.reloj = pygame.time.Clock()
        self.fondo = pygame.image.load('Proyecto/assets/imagenes/escena_1.png')
        self.fondo = pygame.transform.scale(self.fondo, (ancho, alto))

    # Funcion para funcionamiento de la escena
    def run(self):
        ejecutando = True

        # Bucle para mantener todo lo de la pantalla en orden:
        while ejecutando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Dibujar el fondo
            self.pantalla.blit(self.fondo, (0, 0))
            pygame.display.flip()
            self.reloj.tick(fps)

