import pygame
import random
import math
blanco=[255,255,255]
negro=[0,0,0]
ANCHO=1024
ALTO=620

def distancia(p1,p2):
    return math.sqrt((p1.rect.x -p2.rect.x)**2 +(p1.rect.y-p2.rect.y)**2)

def acercar(dist, enemigo, jugador):
    if dist > 200:
        if jugador.rect.x < enemigo.rect.x and enemigo.rect.x > 150:
            enemigo.left()
        elif jugador.rect.x > enemigo.rect.x and enemigo.rect.x < ANCHO -250:
            enemigo.right()
    else:
        enemigo.golpear()

class fondo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("stage11.png")
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=-50
        self.varx=0
        self.vary=0
        self.mov=True

    def update(self):
        self.rect.x=self.rect.x-self.varx
        self.rect.y=self.rect.y+self.vary

    def movefondo(self):
        self.rect.x=self.rect.x-self.varx


class jugador(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.varx=0
        self.vary=0
        self.i=0
        self.rect.x=0
        self.rect.y=250
        self.accion=0
        self.dir=True
        self.mov=False
        self.cambiodir=0
        self.flag=True

    def update(self):
        if self.dir:
            self.accion=self.accion
        else:
            if self.flag:
                self.accion=self.accion+self.cambiodir
                self.flag=False
                print self.accion
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.image=self.m[self.accion][self.i]
        self.i+=1
        if self.i>=len(self.m[self.accion]):
            self.i=0
            if self.dir:
                if not (self.accion==0) and self.mov:
                    self.accion=0
            else:
                if not (self.accion==8) and self.mov:
                    self.accion=8

class enemigos(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=150
        self.varx=0
        self.vary=0
        self.distancia=0
        self.i=0
        self.accion=0
        self.mov=True
        self.derecha=True
        self.izquierda=False
        self.Tespera=random.randrange(40,120)

    def update(self):
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.image=self.m[self.accion][self.i]
        self.i+=1
        if(self.Tespera>0):
            self.Tespera-=1
        if self.i>=len(self.m[self.accion]):
            self.i=0
            if self.derecha:
                self.accion=0
                self.varx=0
            if self.izquierda:
                self.accion=5
                self.varx=0

    def left(self):
        self.izquierda=True
        self.derecha=False
        self.accion=6
        self.varx=-5


    def right(self):
        self.derecha=True
        self.izquierda=False
        self.accion=1
        self.varx=5

    def golpear(self):
        if self.derecha:
            if(self.Tespera<=0):
                self.accion=2
                self.Tespera=random.randrange(40,120)
                self.varx=0
                self.i=0

        if self.izquierda:
            if(self.Tespera<=0):
                self.accion=7
                self.Tespera=random.randrange(40,120)
                self.varx=0
                self.i=0

def recortar(max_x, max_y, archivo, vector):
    imagen=pygame.image.load(archivo)
    info=imagen.get_rect()
    an_imagen=info[2]
    al_imagen=info[3]
    an_image_corte= an_imagen/max_x
    al_image_corte= al_imagen/max_y
    mapa=[]
    for i in range(max_y):
        mapis=[]
        for j in range(vector[i]):
            cuadro=imagen.subsurface(j*an_image_corte, i*al_image_corte, an_image_corte, al_image_corte)
            mapis.append(cuadro)
        mapa.append(mapis)
    return mapa


def juego():
    pygame.init()
    fin=False
    c=0
    parada=True
    reloj = pygame.time.Clock()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    flag=True
    flag2=True

    protagonista1sprite='protagonista1.png'
    protagonista1=recortar(11,16,protagonista1sprite,[1,11,10,8,7,7,11,7,1,11,10,8,7,7,11,7])
    jugador1=jugador(protagonista1)

    fondito=fondo()
    fondos=pygame.sprite.Group()
    fondos.add(fondito)

    enemigo1sprite='reptilfinal.png'
    enemigo1=recortar(6,10, enemigo1sprite, [5,6,5,6,6,5,6,5,6,6])
    enemigoo=enemigos(enemigo1)

    enemigooos=pygame.sprite.Group()
    enemigooos.add(enemigoo)
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    jugadores.add(jugador1)
    todos.add(fondito)
    todos.add(jugador1)
    todos.add(enemigoo)

    pause = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador1.mov=False
                    jugador1.dir=True
                    jugador1.accion=1
                    jugador1.varx=20
                    parada =True
                    flag=True
                if event.key == pygame.K_LEFT:
                    jugador1.mov=False
                    jugador1.dir=False
                    jugador1.flag=True
                    jugador1.cambiodir=8
                    jugador1.accion=1
                    jugador1.varx=-10
                    parada=False
                    flag=False

                if event.key == pygame.K_UP:
                    if jugador1.dir:
                        flag2=True
                        jugador1.mov=False
                        jugador1.accion=1
                        jugador1.vary=-5
                        print jugador1.rect.y
                    else:
                        jugador1.mov=False
                        jugador1.flag=True
                        jugador1.accion=1
                        jugador1.vary=-5
                        jugador1.cambiodir=8
                if event.key == pygame.K_DOWN:
                    if jugador1.dir:
                        flag2=False
                        jugador1.mov=False
                        jugador1.accion=1
                        jugador1.vary=+5
                        print jugador1.accion, 'je ne sais'
                    else:
                        jugador1.mov=False
                        jugador1.flag=True
                        jugador1.accion=1
                        jugador1.vary=5
                        jugador1.cambiodir=8
                        print jugador1.accion, 'hola'

                if event.key == pygame.K_s:
                    if jugador1.dir:
                        jugador1.accion=2
                        jugador1.i=0
                    else:
                        jugador1.flag=True
                        jugador1.accion=2
                        jugador1.cambiodir=8
                if event.key == pygame.K_c:
                    if jugador1.dir:
                        jugador1.accion=4
                        jugador1.i=0
                    else:
                        jugador1.flag=True
                        jugador1.accion=4
                        jugador1.cambiodir=8
                if event.key == pygame.K_p:
                    if not pause:
                        pause=True
                    else:
                        pause=False
            if event.type == pygame.KEYUP:
                jugador1.varx=0
                jugador1.vary=0
                jugador1.mov=True
                parada=False
                flag=False
        print jugador1.rect.x
        if jugador1.rect.x>512 and parada:
            fondito.varx=10
            jugador1.varx=0
            fondito.movefondo()
            if math.fabs(fondito.rect.x)>math.fabs(ANCHO-3254) and parada:
                fondito.varx=0
                fondito.rect.x=ANCHO-3264
                parada=False
        else:
            fondito.varx=0

        if fondito.rect.x==ANCHO-3264 and flag:
            parada=False
            jugador1.varx=10

        if jugador1.rect.x<=-100 and not flag:
            jugador1.varx=0

        if jugador1.rect.y<=180 and flag2:
            jugador1.vary=0




        if not pause:
            todos.update()
            pantalla.fill(negro)
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(7)
        else:
            pygame.display.flip()
        distance=distancia(jugador1, enemigoo)
        acercar(distance, enemigoo,jugador1)
