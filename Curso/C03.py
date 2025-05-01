# Importaciones de librerias:
import pygame
import sys
from pygame.locals import QUIT

# Dimensiones de la ventana:
ancho = 400
alto = 300

# Sentencia obligatoria antes de usar pygame
pygame.init()

# Creacion de la bola
class Bolita():
    '''Clase que determina los parametros y comportamientos de la bola dentro del juego'''
    def __init__(self):
        '''Contructor que recibe al constructor padre.'''
        pygame.sprit.Sprite.__initi__(self)

# Creacion de la ventana
ventana = pygame.display.set_mode((ancho, alto))
# Nombre de la ventana
pygame.display.set_caption('Hola Mundo')


while True:
    # Eventos (Mouse o teclado)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # La ventana se actualizara
    pygame.display.update()


    