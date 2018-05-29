import pygame
import random
blanco=[255,255,255]
negro=[0,0,0]
ANCHO=1024
ALTO=384



class jugador(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.varx=0
        self.vary=0
        self.i=0
        self.accion=0
        self.mov=True

    def update(self):
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.image=self.m[3][self.i]
        self.i+=1
        if self.i>=len(self.m[2]):
            self.i=0
            if not(self.accion == 1) and self.mov:
                self.accion=1

class bolaenergia(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.varx=0
        self.vary=0
        self.i=0
        self.accion=4

    def update(self):
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.image=self.m[self.accion][self.i]
        self.i+=0
        if self.i>=len(self.m[self.accion]):
            self.i=0



if __name__ == '__main__':
    pygame.init()
    fin=False
    c=0
    reloj = pygame.time.Clock()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    kens=(pygame.image.load('reptil.png')).convert()
    info=kens.get_rect()
    an_ken=info[2]
    al_ken=info[3]
    an_image_corte= int(an_ken/6)
    al_image_corte= int(al_ken/5)
    ken=[]
    columnas=[5,6,5,6,6]
    for i in range(5):
        kenny=[]
        for j in range(columnas[i]):
            cuadro=kens.subsurface(j*an_image_corte, i*al_image_corte, an_image_corte, al_image_corte)
            kenny.append(cuadro)
        ken.append(kenny)

    jugador1=jugador(ken)
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    energia=pygame.sprite.Group()
    jugadores.add(jugador1)
    todos.add(jugador1)
    pause = False
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador1.mov=False
                    jugador1.accion=3
                    jugador1.i=0
                    jugador1.varx=2
                if event.key == pygame.K_LEFT:
                    jugador1.varx=-2
                if event.key == pygame.K_UP:
                    jugador1.vary=-2
                if event.key == pygame.K_DOWN:
                    jugador1.vary=2
                if event.key == pygame.K_s:
                    jugador1.accion=8
                    jugador1.i=0
                if event.key == pygame.K_c:
                    jugador1.accion=6
                    jugador1.i=0
                if event.key == pygame.K_z:
                    jugador1.accion=7
                    jugador1.i=0
                if event.key == pygame.K_x:
                    jugador1.accion=9
                    jugador1.i=0
                if event.key == pygame.K_SPACE:
                    jugador1.accion=2
                    jugador1.i=0
                if event.key == pygame.K_a:
                    jugador1.accion=0
                    balaenergia1=bolaenergia(ken)
                    energia.add(balaenergia1)
                    balaenergia1.varx=2
                    balaenergia1.rect.x=jugador1.rect.x+50
                    balaenergia1.rect.y=jugador1.rect.y
                    todos.add(balaenergia1)
                    jugador1.i=0
                if event.key == pygame.K_p:
                    if not pause:
                        pause=True
                    else:
                        pause=False
            if event.type == pygame.KEYUP:
                jugador1.mov=True
                jugador1.varx=0
                jugador1.vary=0

        if not pause:
            todos.update()
            pantalla.fill(negro)
            todos.draw(pantalla)


            """pantalla.blit(ken[1], [20,20])"""
            pygame.display.flip()
            reloj.tick(5)
        else:
            """pantalla.fill(negro)"""
            """pantalla.blit(ken[1], [20,20])"""
            pygame.display.flip()
