'''MURO'''

# Importaciones de librerias:
import pygame
import sys
from pygame.locals import QUIT
from pygame.sprite import Sprite, Group

# Dimensiones de la ventana:
ancho = 640
alto = 480
color_azul = (0, 0, 64)

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
        # Establecer velocidad:
        self.speed = [3, 3]

    # Funcion mover la bolita:
    def update(self):
        '''Funcion que determina el movimiento de la bolita'''

        #Evitar que salga por debajo:
        if self.rect.bottom >= alto:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ancho:
            self.speed[0] = -self.speed[0]
        elif self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

        # Mover con base a posicion actual y velocidad
        self.rect.move_ip(self.speed)

# Creacion de la Paleta
class Paleta(pygame.sprite.Sprite):
    '''Clase para la manipulacion de la paleta'''

    # Funcion constructor
    def __init__(self):
        '''Contructor que recibe al constructor padre.'''

        pygame.sprite.Sprite.__init__(self)
        # Carga de la imagen:
        self.image = pygame.image.load('Curso/Imagenes/paleta.png')
        # Obtener el rectangulo de la imagen:
        self.rect = self.image.get_rect()
        # Posicion inicial centrada en la pantalla en x:
        self.rect.midbottom = (ancho / 2, alto - 20)
        # Establecer velocidad:
        self.speed = [0, 0]

    def update(self, evento):
        '''Funcion que recibe informacion del evento en teclado y manipula la paleta'''

        # Buscar si se presiono alguna tecla
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ancho:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        
        # Mover con base a posicion actual y velocidad
        self.rect.move_ip(self.speed)

# Creacion del ladrillo
class Ladrillo(pygame.sprite.Sprite):
    '''Clase para el manejo del ladrillo'''

    # Funcion constructor
    def __init__(self, posicion):
        '''Contructor que recibe al constructor padre.'''

        pygame.sprite.Sprite.__init__(self)
        # Carga de la imagen:
        self.image = pygame.image.load('Curso/Imagenes/ladrillo.png')
        # Obtener el rectangulo de la imagen:
        self.rect = self.image.get_rect()
        # Posicion inicial:
        self.rect.topleft = posicion

# Creacion de la clase muro:
class Muro(pygame.sprite.Group):
    '''Clase que creara un grupo de ladrillos para la simulacion del muro'''

    # FUncion constructor
    def __init__(self, cantidad_ladrillos):
        '''Llamamos la constructor padre'''
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 0
        # Bucle para crear los ladrillos:
        for i in range(cantidad_ladrillos):
            # Creacion del ladrillo
            ladrillo = Ladrillo((pos_x, pos_y))
            # Se agrega el objeto al muro
            self.add(ladrillo)

            pos_x += ladrillo.rect.width
            if pos_x >= ancho:
                pos_x = 0
                pos_y += ladrillo.rect.height

# Creacion de la ventana
pantalla = pygame.display.set_mode((ancho, alto))
# Nombre de la ventana
pygame.display.set_caption('Juego de ladrillos')
# Crear el reloj:
reloj = pygame.time.Clock()
# Ajustar repeticion de la paleta:
pygame.key.set_repeat(30)

# Iteracion de los objetos
bolita = Bolita()
paleta = Paleta()
muro = Muro(48) # Cantidad de ladrillos

while True:
    # Establecer los FPS:
    reloj.tick(60)

    # Revisar todos los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        # Buscar eventos del teclado:
        elif evento.type == pygame.KEYDOWN:
            paleta.update(evento)

    # Actualizar posicion de la bolita:
    bolita.update()
    # Colision entre bolita y paleta:
    if pygame.sprite.collide_rect(bolita, paleta):
        bolita.speed[1] = -bolita.speed[1]
    
    # COlision de la bolita con el muro:
    lista = pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            # Invierte direccion en x
            bolita.speed[0] = -bolita.speed[0]
        else:
            # Invierte direccion en y
            bolita.speed[1] = -bolita.speed[1]

        # Se elimina el ladrillo
        muro.remove(ladrillo)

    # Rellenar la pantalla
    pantalla.fill(color_azul)
    # Dibujar bolita en pantalla:
    pantalla.blit(bolita.image, bolita.rect)
    # Dibujar paleta en pantalla:
    pantalla.blit(paleta.image, paleta.rect)
    # Dibujar los ladrillos:
    muro.draw(pantalla)
    # La ventana se actualizara
    pygame.display.flip()