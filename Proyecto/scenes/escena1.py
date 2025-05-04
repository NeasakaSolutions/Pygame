# Importaciones necesarias
import pygame
from pygame.locals import QUIT, KEYDOWN
import sys
from settings import ancho, alto, fps
from utils.textos import cargar_textos
from scenes.escena2 import Escena2  # Asegúrate de importar la clase Escena2

# Función para dividir el texto en varias líneas según el ancho
def dividir_texto(texto, fuente, ancho_max):
    lineas = []
    palabras = texto.split(" ")
    linea_actual = ""

    for palabra in palabras:
        # Añadir la palabra a la línea actual
        if fuente.size(linea_actual + " " + palabra)[0] <= ancho_max:
            linea_actual += " " + palabra
        else:
            # Si la línea actual excede el ancho, añadirla a la lista de líneas
            if linea_actual != "":
                lineas.append(linea_actual)
            # Comenzamos una nueva línea con la palabra actual
            linea_actual = palabra

    # Añadir la última línea si existe
    if linea_actual != "":
        lineas.append(linea_actual)

    return lineas

# Se crea la clase de escena 1
class Escena1():
    
    def __init__(self):
        '''Función que inicializa pantalla, fondos, reloj, y textos'''

        # Cargar el json:
        self.textos = cargar_textos("dialogos_escena1.json")["escena1"]

        # Configuración de los textos:
        self.fuente = pygame.font.Font(None, 36)

        # Dividir los textos para evitar que se desborden
        lineas_linea1 = dividir_texto(self.textos["narrador_linea1"], self.fuente, ancho - 100)
        lineas_linea2 = dividir_texto(self.textos["narrador_linea2"], self.fuente, ancho - 100)

        # Configuración de las líneas de texto
        self.textos_linea1 = [self.fuente.render(linea, True, (0, 0, 0)) for linea in lineas_linea1]
        self.textos_linea2 = [self.fuente.render(linea, True, (0, 0, 0)) for linea in lineas_linea2]

        # Posicionamiento de las líneas
        self.rect_narrador_linea1 = [texto.get_rect(center=(ancho // 2, 100 + 40 * i)) for i, texto in enumerate(self.textos_linea1)]
        self.rect_narrador_linea2 = [texto.get_rect(center=(ancho // 2, 200 + 40 * i)) for i, texto in enumerate(self.textos_linea2)]

        # Renderizar la instrucción
        self.texto_instruccion = self.fuente.render(self.textos["instruccion"], True, (0, 0, 0))
        self.rect_instruccion = self.texto_instruccion.get_rect(center=(ancho // 2, 250 + 40 * (len(self.textos_linea1) + len(self.textos_linea2))))

        # Configuración de la pantalla de la escena 1
        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption('Escena 1 - Habitacion')

        # Configurar fondo de la imagen
        self.reloj = pygame.time.Clock()
        self.fondo = pygame.image.load('Proyecto/assets/imagenes/habitacion.jpg')
        self.fondo = pygame.transform.scale(self.fondo, (ancho, alto))

    # Función para funcionamiento de la escena
    def run(self):
        ejecutando = True

        # Bucle para mantener todo lo de la pantalla en orden:
        while ejecutando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Detectar si se presiona la tecla ESPACIO
                if event.type == KEYDOWN and event.key == pygame.K_SPACE:
                    # Al presionar la tecla ESPACIO, cambiar a la escena 2
                    escena = Escena2()
                    escena.run()
                    return  

            # Dibujos
            # Dibujar el fondo
            self.pantalla.blit(self.fondo, (0, 0))
            
            # Dibujar las líneas de texto
            for i, texto in enumerate(self.textos_linea1):
                self.pantalla.blit(texto, self.rect_narrador_linea1[i])
            for i, texto in enumerate(self.textos_linea2):
                self.pantalla.blit(texto, self.rect_narrador_linea2[i])
            
            # Dibujar la instrucción
            self.pantalla.blit(self.texto_instruccion, self.rect_instruccion)

            # Pantalla siempre activa
            pygame.display.flip()
            # Renderizar a la velocidad adecuada
            self.reloj.tick(fps)






