# IMportaciones:
import pygame
import sys
from pygame.locals import QUIT
from scenes.escena1 import Escena1
from settings import ancho, alto, fps

# Sentencia para funcionamiento de pygame
pygame.init()
# Sentencia para funcionamiento de la musica con pygame
pygame.mixer.init()

# Clase menu (Ventana principal):
class Menu:
    '''Clase con las configuraciones de la ventana principal'''

    # Funcion contructor de la clase menu:
    def __init__(self):
        '''Configuracion de los botones, ventana y musica de fondo'''

        self.reloj = pygame.time.Clock()
        # Tamanio de la ventana:
        self.pantalla = pygame.display.set_mode((ancho, alto))
        # Texto de arriba en la ventana:
        pygame.display.set_caption('Ijole')

        # Llamando a la funcion de reproducir musica:
        self.reproducir_musica()

        # COnfiguracion del fondo
        self.fondo = pygame.image.load('Proyecto/assets/imagenes/fondo_menu.jpg').convert()
        self.fondo = pygame.transform.scale(self.fondo, (ancho, alto))

        # Configuracion de los botones:
        self.boton_ancho = 200
        self.boton_alto = 50
        self.boton_inicio_rect = pygame.Rect((ancho // 2 - self.boton_ancho // 2, 175), (self.boton_ancho, self.boton_alto))
        self.boton_salir_rect = pygame.Rect((ancho // 2 - self.boton_ancho // 2, 275), (self.boton_ancho, self.boton_alto))

        self.fuente = pygame.font.SysFont("arial", 30)

    # Funcion para iniciar la musica de fondo:
    def reproducir_musica(self):
        '''Carga e inicia la musica, se configuro asi para detener la musica al cerrar la ventana menu'''

        pygame.mixer.music.load('Proyecto/assets/sonidos/musica_fondo_menu.mp3')
        pygame.mixer.music.play(-1, 0.0)

    # Funcion para establecer los botones:
    def dibujar_boton(self, rect, texto, mouse_pos):
        '''Funcion que configura los botones para que se vean mas perros'''

        if rect.collidepoint(mouse_pos):
            color = (0, 0, 0)
            alpha = 255
        else:
            color = (0, 0, 0)
            alpha = 100

        boton_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        boton_surface.fill((*color, alpha))
        self.pantalla.blit(boton_surface, rect.topleft)

        texto_surface = self.fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect(center=rect.center)
        self.pantalla.blit(texto_surface, texto_rect)

    # Funcion para iniciar el menu:
    def run(self):
        '''Funcion que inicia la ventana del menu y dibuja todas las configuraciones'''
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Comportamiento de los botones
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_inicio_rect.collidepoint(event.pos):
                        # Detener la musica del menu:
                        pygame.mixer.music.stop()
                        escena = Escena1()
                        escena.run()
                        # Reanudar musica al volver al menu
                        self.reproducir_musica()
                    elif self.boton_salir_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            # Area de dibujo:
            self.pantalla.blit(self.fondo, (0, 0))
            self.dibujar_boton(self.boton_inicio_rect, "Inicio", mouse_pos)
            self.dibujar_boton(self.boton_salir_rect, "Salir", mouse_pos)

            pygame.display.flip()
            self.reloj.tick(fps)



