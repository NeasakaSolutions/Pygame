import os
import pygame
import sys
from settings import ancho, alto, fps
from utils.textos import cargar_textos
from scenes.final_malo import FinalMalo

class Escena2():
    def __init__(self):
        pygame.init()

        # Música
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Proyecto/assets/sonidos/musica_bosque.mp3')
        pygame.mixer.music.play(-1, 0.0)

        # Cargar diálogos
        ruta_base = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta de este archivo
        ruta_dialogos_bosque = os.path.join(ruta_base, "../data/dialogos_bosque.json")
        ruta_dialogos_hoja = os.path.join(ruta_base, "../data/dialogos_bosque_hoja.json")

        self.dialogos = cargar_textos(ruta_dialogos_bosque).get("bosque", [])
        self.dialogos_hoja = cargar_textos(ruta_dialogos_hoja).get("hoja", [])

        self.indice_dialogo = 0
        self.indice_dialogo_hoja = 0
        self.mostrando_hoja = False

        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption('Escena del Bosque')
        self.fuente = pygame.font.Font(None, 36)
        self.reloj = pygame.time.Clock()

        # Fondos
        self.fondo_bosque = pygame.transform.scale(pygame.image.load('Proyecto/assets/imagenes/escena_1.png'), (ancho, alto))
        self.fondo_hoja = pygame.transform.scale(pygame.image.load('Proyecto/assets/imagenes/noticia.jpg'), (ancho, alto))

        # Botones
        self.boton_ancho = 200
        self.boton_alto = 50
        self.boton_color_base = (0, 0, 0, 150)
        self.boton_color_hover = (30, 30, 30, 200)
        self.boton_rect_correr = pygame.Rect((ancho - self.boton_ancho) // 2, alto - 150, self.boton_ancho, self.boton_alto)
        self.boton_rect_acercarse = pygame.Rect((ancho - self.boton_ancho) // 2, alto - 80, self.boton_ancho, self.boton_alto)
        self.boton_rect_siguiente = pygame.Rect((ancho - self.boton_ancho) // 2, alto - 100, self.boton_ancho, self.boton_alto)

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

    def dibujar_texto(self, texto, y_inicio):
        lineas = self.dividir_texto(texto, self.fuente, ancho - 100)
        y = y_inicio
        for linea in lineas:
            render = self.fuente.render(linea.strip(), True, (255, 255, 255))
            rect = render.get_rect(center=(ancho // 2, y))
            self.pantalla.blit(render, rect)
            y += self.fuente.get_linesize()

    def dibujar_boton(self, texto, mouse_pos, boton_rect):
        mouse_encima = boton_rect.collidepoint(mouse_pos)
        color = self.boton_color_hover if mouse_encima else self.boton_color_base

        boton_surface = pygame.Surface((self.boton_ancho, self.boton_alto), pygame.SRCALPHA)
        boton_surface.fill(color)
        self.pantalla.blit(boton_surface, boton_rect)

        texto_render = self.fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_render.get_rect(center=boton_rect.center)
        self.pantalla.blit(texto_render, texto_rect)

        return mouse_encima

    def run(self):
        ejecutando = True

        while ejecutando:
            mouse_click = False
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_click = True

            # Fondo
            if self.mostrando_hoja:
                self.pantalla.blit(self.fondo_hoja, (0, 0))
            else:
                self.pantalla.blit(self.fondo_bosque, (0, 0))

            # Texto
            if self.mostrando_hoja:
                if self.indice_dialogo_hoja < len(self.dialogos_hoja):
                    self.dibujar_texto(self.dialogos_hoja[self.indice_dialogo_hoja], alto // 2 - 50)
            else:
                if self.indice_dialogo < len(self.dialogos):
                    self.dibujar_texto(self.dialogos[self.indice_dialogo], alto // 2 - 50)

            # Botones
            if self.mostrando_hoja:
                if self.indice_dialogo_hoja < len(self.dialogos_hoja):
                    encima_siguiente = self.dibujar_boton("Siguiente", mouse_pos, self.boton_rect_siguiente)
                    if encima_siguiente and mouse_click:
                        self.indice_dialogo_hoja += 1
                        if self.indice_dialogo_hoja >= len(self.dialogos_hoja):
                            pygame.mixer.music.stop()
                            FinalMalo().run()
                            return
            else:
                encima_correr = self.dibujar_boton("Correr", mouse_pos, self.boton_rect_correr)
                encima_acercarse = self.dibujar_boton("Acercarse", mouse_pos, self.boton_rect_acercarse)

                if encima_correr and mouse_click:
                    pygame.mixer.music.stop()
                    from scenes.escena1 import Escena1
                    Escena1().run()
                    return
                elif encima_acercarse and mouse_click:
                    self.mostrando_hoja = True
                    self.indice_dialogo_hoja = 0

            pygame.display.flip()
            self.reloj.tick(fps)














