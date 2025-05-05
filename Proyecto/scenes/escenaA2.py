import pygame
import sys
from settings import ancho, alto, fps
from utils.textos import cargar_textos
from scenes.final_bueno import FinalBueno  # Este sí se puede dejar arriba

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
        self.fondo_ciudad = pygame.image.load('Proyecto/assets/imagenes/ciudad.jpg')
        self.fondo_ciudad = pygame.transform.scale(self.fondo_ciudad, (ancho, alto))
        self.fondo_noticia = pygame.image.load('Proyecto/assets/imagenes/noticia.jpg')
        self.fondo_noticia = pygame.transform.scale(self.fondo_noticia, (ancho, alto))

        # Botones
        self.boton_ancho = 220
        self.boton_alto = 50
        self.boton_color_base = (0, 0, 0, 100)
        self.boton_color_hover = (0, 0, 0, 255)

        # Botón "Siguiente"
        self.boton_siguiente_rect = pygame.Rect(
            (ancho - self.boton_ancho) // 2,
            alto - 100,
            self.boton_ancho,
            self.boton_alto
        )

        # Botón "Regresar a casa"
        self.boton_regresar_rect = pygame.Rect(
            (ancho - self.boton_ancho) // 2,
            alto - 170,
            self.boton_ancho,
            self.boton_alto
        )

    def dividir_texto(self, texto, fuente, max_ancho):
        palabras = texto.split(' ')
        lineas = []
        linea_actual = ""

        for palabra in palabras:
            test_linea = linea_actual + palabra + " "
            if fuente.size(test_linea)[0] <= max_ancho:
                linea_actual = test_linea
            else:
                lineas.append(linea_actual)
                linea_actual = palabra + " "
        lineas.append(linea_actual)
        return lineas

    def dibujar_texto(self, texto):
        lineas = self.dividir_texto(texto, self.fuente, ancho - 100)
        y = alto // 2 - 50 - (len(lineas) * 20)
        for linea in lineas:
            render = self.fuente.render(linea.strip(), True, (255, 255, 255))
            rect = render.get_rect(center=(ancho // 2, y))
            self.pantalla.blit(render, rect)
            y += self.fuente.get_linesize()

    def dibujar_boton(self, superficie, texto, rect, mouse_pos):
        mouse_encima = rect.collidepoint(mouse_pos)
        boton_surface = pygame.Surface((self.boton_ancho, self.boton_alto), pygame.SRCALPHA)
        color = self.boton_color_hover if mouse_encima else self.boton_color_base
        boton_surface.fill(color)
        superficie.blit(boton_surface, rect)

        texto_render = self.fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_render.get_rect(center=rect.center)
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
                self.pantalla.blit(self.fondo_ciudad, (0, 0))
            else:
                self.pantalla.blit(self.fondo_noticia, (0, 0))

            # Mostrar texto
            if self.indice_dialogo < len(self.dialogos):
                self.dibujar_texto(self.dialogos[self.indice_dialogo])
            else:
                pygame.mixer.music.stop()
                siguiente = FinalBueno()
                siguiente.run()
                return

            # Dibujar botones
            encima_siguiente = self.dibujar_boton(self.pantalla, "Siguiente", self.boton_siguiente_rect, mouse_pos)
            encima_regresar = self.dibujar_boton(self.pantalla, "Regresar a casa", self.boton_regresar_rect, mouse_pos)

            # Acciones
            if encima_siguiente and mouse_click:
                self.indice_dialogo += 1

            if encima_regresar and mouse_click:
                pygame.mixer.music.stop()
                from scenes.escena1 import Escena1  # Import dinámico para evitar circular import
                escena1 = Escena1()
                escena1.run()
                return

            pygame.display.flip()
            self.reloj.tick(fps)


