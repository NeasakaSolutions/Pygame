# Importaciones de librerias:
import pygame
import sys
from pygame.locals import QUIT

# Dimensiones de la ventana:
ancho = 640
alto = 480

# Sentencia obligatoria antes de usar pygame
pygame.init()

# Creacion de la bola
class Bolita(pygame.sprite.Sprite):
    '''Clase para la manipulacion de la bolita'''

    # Funcion constructor
    def __init__(self):
        '''Contructor que recibe al constructor padre.'''
        pygame.sprite.Sprite.__init__(self)
        # Carga de la imagen:
        self.image = pygame.image.load('Curso/Imagenes/bolita.png')
        # Obtener el rectangulo de la imagen:
        self.rect = self.image.get_rect()
        # Posicion inicial centrada en la pantalla
        self.rect.centerx = ancho / 2
        self.rect.centery = alto / 2

# Creacion de la ventana
pantalla = pygame.display.set_mode((ancho, alto))
# Nombre de la ventana
pygame.display.set_caption('Juego de ladrillos')

# Iteracion del objeto
bolita = Bolita()

while True:
    # Eventos (Mouse o teclado)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar bolita en pantalla:
    pantalla.blit(bolita.image, bolita.rect)
    # La ventana se actualizara
    pygame.display.update()


    