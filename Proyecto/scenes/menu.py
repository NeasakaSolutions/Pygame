# IMportaciones:
import pygame
import sys
import os
from pygame.locals import QUIT
# Importacion de las variales globales
from settings import ancho, alto, fps


# Sentencias para la utilizacion correcta de pygame:
pygame.init()
# Para los efectos de sonido
pygame.mixer.init()

class Menu():
    '''Clase que muestra la configuracion del menu'''

    # Constructor de la clase Menu
    def __init__(self):
        '''Funcion que crea la interfaz de la ventana'''

        # Crear la ventana del menu principal:
        self.pantalla = pygame.display.set_mode((ancho, alto))
        # Nombre de la ventana:
        pygame.display.set_caption('Ijole')

        # Configuracion de la musica de fondo:
        # Detener cualquier otro sonido en otro plano:
        pygame.mixer.stop()
        pygame.mixer.music.load('Proyecto/assets/sonidos/musica_fondo_menu.mp3')
        #pygame.mixer.music.load("/home/kali/Documents/Pygame/Proyecto/assets/sonidos/musica_fondo_menu.mp3")
        # Reproducir en bucle infinito:
        pygame.mixer.music.play(-1, 0.0)

        # Configuracion de la imagen de fondo:
        # Cargar la imagen:
        self.fondo = pygame.image.load('Proyecto/assets/imagenes/fondo_menu.jpg').convert()
        # Tamanio de la imagen:
        self.fondo = pygame.transform.scale(self.fondo, (ancho, alto))


    # Funcion para funcionamiento del menu
    def run(self):
        '''Bucle principal del menu'''

        while True:
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Imagen:
            self.pantalla.blit(self.fondo, (0, 0))
            # Renderizado actual de la pantalla
            pygame.display.flip()

            # FPS:
            pygame.time.Clock().tick(fps)

