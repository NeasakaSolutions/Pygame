# Importaciones necesarias
import pygame
from pygame.locals import QUIT
import sys
from settings import ancho, alto, fps
from utils.textos import cargar_textos
from scenes.escena2 import Escena2
from scenes.escenaA2 import EscenaA2 

# Función para dividir texto
def dividir_texto(texto, fuente, ancho_max):
    lineas = []
    palabras = texto.split(" ")
    linea_actual = ""

    for palabra in palabras:
        if fuente.size(linea_actual + " " + palabra)[0] <= ancho_max:
            linea_actual += " " + palabra
        else:
            if linea_actual != "":
                lineas.append(linea_actual)
            linea_actual = palabra

    if linea_actual != "":
        lineas.append(linea_actual)

    return lineas

# Clase Escena1
class Escena1():
    
    def __init__(self):
        '''Inicializa pantalla, fondo, reloj, música y textos'''

        pygame.mixer.music.stop()
        pygame.mixer.music.load('Proyecto/assets/sonidos/fondo_escenas.mp3')
        pygame.mixer.music.play(-1, 0.0)

        self.textos = cargar_textos("dialogos_escena1.json")["escena1"]
        self.fuente = pygame.font.Font(None, 36)

        lineas_linea1 = dividir_texto(self.textos["narrador_linea1"], self.fuente, ancho - 100)
        lineas_linea2 = dividir_texto(self.textos["narrador_linea2"], self.fuente, ancho - 100)

        self.textos_linea1 = [self.fuente.render(linea, True, (0, 0, 0)) for linea in lineas_linea1]
        self.textos_linea2 = [self.fuente.render(linea, True, (0, 0, 0)) for linea in lineas_linea2]

        self.rect_narrador_linea1 = [texto.get_rect(center=(ancho // 2, 100 + 40 * i)) for i, texto in enumerate(self.textos_linea1)]
        self.rect_narrador_linea2 = [texto.get_rect(center=(ancho // 2, 200 + 40 * i)) for i, texto in enumerate(self.textos_linea2)]

        self.texto_instruccion = self.fuente.render(self.textos["instruccion"], True, (0, 0, 0))
        self.rect_instruccion = self.texto_instruccion.get_rect(center=(ancho // 2, 250 + 40 * (len(self.textos_linea1) + len(self.textos_linea2))))

        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption('Escena 1 - Habitación')
        self.reloj = pygame.time.Clock()

        self.fondo = pygame.image.load('Proyecto/assets/imagenes/habitacion.jpg')
        self.fondo = pygame.transform.scale(self.fondo, (ancho, alto))

        # Botones: bosque y ciudad
        self.boton_width, self.boton_height = 220, 50

        self.boton_bosque = pygame.Surface((self.boton_width, self.boton_height), pygame.SRCALPHA)
        self.rect_boton_bosque = self.boton_bosque.get_rect(center=(ancho // 2, alto - 130))

        self.boton_ciudad = pygame.Surface((self.boton_width, self.boton_height), pygame.SRCALPHA)
        self.rect_boton_ciudad = self.boton_ciudad.get_rect(center=(ancho // 2, alto - 60))

    def run(self):
        ejecutando = True

        while ejecutando:
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_click = True

            self.pantalla.blit(self.fondo, (0, 0))

            for i, texto in enumerate(self.textos_linea1):
                self.pantalla.blit(texto, self.rect_narrador_linea1[i])
            for i, texto in enumerate(self.textos_linea2):
                self.pantalla.blit(texto, self.rect_narrador_linea2[i])
            self.pantalla.blit(self.texto_instruccion, self.rect_instruccion)

            # --- Botón "Ir al bosque"
            hover_bosque = self.rect_boton_bosque.collidepoint(mouse_pos)
            alpha_bosque = 200 if hover_bosque else 100
            self.boton_bosque.fill((0, 0, 0, alpha_bosque))
            self.pantalla.blit(self.boton_bosque, self.rect_boton_bosque)

            texto_bosque = self.fuente.render("Ir al bosque", True, (255, 255, 255))
            texto_bosque_rect = texto_bosque.get_rect(center=self.rect_boton_bosque.center)
            self.pantalla.blit(texto_bosque, texto_bosque_rect)

            # --- Botón "Ir a la ciudad"
            hover_ciudad = self.rect_boton_ciudad.collidepoint(mouse_pos)
            alpha_ciudad = 200 if hover_ciudad else 100
            self.boton_ciudad.fill((0, 0, 0, alpha_ciudad))
            self.pantalla.blit(self.boton_ciudad, self.rect_boton_ciudad)

            texto_ciudad = self.fuente.render("Ir a la ciudad", True, (255, 255, 255))
            texto_ciudad_rect = texto_ciudad.get_rect(center=self.rect_boton_ciudad.center)
            self.pantalla.blit(texto_ciudad, texto_ciudad_rect)

            # --- Cambiar de escena si se hace clic
            if hover_bosque and mouse_click:
                pygame.mixer.music.stop()
                escena = Escena2()
                escena.run()
                return
            elif hover_ciudad and mouse_click:
                pygame.mixer.music.stop()
                escena = EscenaA2()
                escena.run()
                return

            pygame.display.flip()
            self.reloj.tick(fps)










