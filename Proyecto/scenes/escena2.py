import pygame
import sys
from settings import ancho, alto, fps

# Clase para la escena 2 con una ventana negra
class Escena2():
    
    def __init__(self):
        '''Inicialización de la pantalla de la escena 2'''

        # Detener cualquier música anterior (por ejemplo, Escena1)
        pygame.mixer.music.stop()

        # Cargar e iniciar música del bosque (solo se hace aquí)
        pygame.mixer.music.load('Proyecto/assets/sonidos/musica_bosque.mp3')
        pygame.mixer.music.play(-1, 0.0)  # En bucle

        # Configuración de la pantalla
        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption('Escena 2 - Pantalla Negra')

        # Reloj para controlar el frame rate
        self.reloj = pygame.time.Clock()

    def run(self):
        '''Función para ejecutar la escena'''
        ejecutando = True

        # Bucle principal de la escena
        while ejecutando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ejecutando = False  # Salir al presionar ESPACIO

            # Dibujar la pantalla negra
            self.pantalla.fill((0, 0, 0))  # Llenamos la pantalla de negro

            # Actualizar la pantalla
            pygame.display.flip()
            
            # Controlar la velocidad del juego
            self.reloj.tick(fps)








