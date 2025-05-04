import pygame
import sys
from settings import ancho, alto, fps
from utils.textos import cargar_textos
from scenes.escenaA3 import EscenaA3

class EscenaA2():
    def __init__(self):
        '''Inicializa la escena de la ciudad'''

        pygame.mixer.music.stop()
        pygame.mixer.music.load('Proyecto/assets/sonidos/musica_bosque.mp3')
        pygame.mixer.music.play(-1, 0.0)

        self.dialogos = cargar_textos("dialogos_escenaA2.json")["escenaA2"]
        self.indice_dialogo = 0

        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption('Escena A2 - Ciudad')

        self.fuente = pygame.font.Font(None, 36)
        self.reloj = pygame.time.Clock()

        # Fondos
        self.fondo_ciudad1 = pygame.image.load('Proyecto/assets/imagenes/fondo_menu.jpg')
        self.fondo_ciudad1 = pygame.transform.scale(self.fondo_ciudad1, (ancho, alto))
        self.fondo_ciudad2 = pygame.image.load('Proyecto/assets/imagenes/escena_1.png')
        self.fondo_ciudad2 = pygame.transform.scale(self.fondo_ciudad2, (ancho, alto))

        # Botón
        self.boton_ancho = 200
        self.boton_alto = 50
        self.boton_color_base = (0, 0, 0, 100)
        self.boton_color_hover = (0, 0, 0, 255)
        self.boton_rect = pygame.Rect((ancho - self.boton_ancho) // 2, alto - 100, self.boton_ancho, self.boton_alto)

    def dibujar_texto(self, texto):
        render = self.fuente.render(texto, True, (255, 255, 255))
        rect = render.get_rect(center=(ancho // 2, alto // 2 - 50))
        self.pantalla.blit(render, rect)

    def dibujar_boton(self, superficie, texto, mouse_pos):
        mouse_encima = self.boton_rect.collidepoint(mouse_pos)
        boton_surface = pygame.Surface((self.boton_ancho, self.boton_alto), pygame.SRCALPHA)
        color = self.boton_color_hover if mouse_encima else self.boton_color_base
        boton_surface.fill(color)
        superficie.blit(boton_surface, self.boton_rect)

        texto_render = self.fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_render.get_rect(center=self.boton_rect.center)
        superficie.blit(texto_render, texto_rect)

        return mouse_encima

    def run(self):
        ejecutando = True

        while ejecutando:
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_click = True

            # Elegir fondo según diálogo actual
            if self.indice_dialogo <= 1:
                self.pantalla.blit(self.fondo_ciudad1, (0, 0))
            else:
                self.pantalla.blit(self.fondo_ciudad2, (0, 0))

            # Mostrar texto
            if self.indice_dialogo < len(self.dialogos):
                self.dibujar_texto(self.dialogos[self.indice_dialogo])
            else:
                pygame.mixer.music.stop()
                siguiente = EscenaA3()
                siguiente.run()
                return

            # Botón
            encima = self.dibujar_boton(self.pantalla, "Siguiente", mouse_pos)

            if encima and mouse_click:
                self.indice_dialogo += 1

            pygame.display.flip()
            self.reloj.tick(fps)