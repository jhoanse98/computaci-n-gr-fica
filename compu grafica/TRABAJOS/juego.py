##Sprite Movimiento de Bloque (JUGADOR)

import pygame
import random


ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
BLANCO=(255,255,255)
NEGRO=(0,0,0)


ANCHO=800
ALTO=600

class Jugador(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        #Variable (Variacion en X) como se mueve el jugadores
        self.var_x=0


    def update(self):
        self.rect.x+=self.var_x

        if self.rect.x>= ANCHO - self.rect.width:
            self.var_x=0

        elif (self.rect.x<=0):
            self.var_x=0

class Rival(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.y=0
        #Variable (Variacion en X) como se mueve los rivales
        self.var_x=0
        #Variable (Variacion en Y) como se mueve los rivales
        self.var_y=1
        self.temporizador=random.randrange(10000)


#Los movimientos de los jugadores deben estar en la clase
    def update(self):
        if self.temporizador >0:
            self.temporizador -= 1
        else:
            self.rect.y+=self.var_y

class Linea(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()


class Cvida(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.var_x=0
        self.var_y=0



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    jp=Jugador (10,20)   #Variable tipo Bloque
    l=Linea(800,1)
    fuente=pygame.font.Font(None,36)
    #  Los sprite se manejan por grupos
    line= pygame.sprite.Group()
    line.add(l)
    l.rect.x=0
    l.rect.y=480

    general= pygame.sprite.Group() #creamos un grupo de sprite llamado general
    general.add(jp)
    jp.rect.x=400
    jp.rect.y=460

    Cuvida= pygame.sprite.Group() #creamos un grupo de sprite llamado general

    pos_x=150
    for i in range(3):
        pos_y=525
        Vida=Cvida(30,30)
        Vida.rect.x=pos_x
        Vida.rect.y=pos_y
        pos_x+=50
        Cuvida.add(Vida)
        general.add(Vida)


    ptos=0
    vida=3

    rivales=pygame.sprite.Group() #creamos un grupo de sprite llamado rivales
    n=1000
    for i in range(n):
        r=Rival(20,20)
        #Para que la posicion donde aparece sea random
        r.rect.x=random.randrange(10,ANCHO - 20)
        r.rect.y=(-400)
        rivales.add(r)
        general.add(r)
        line.add(r)

    reloj=pygame.time.Clock()
    fin_juego=False
    fin=False
    while not fin:
        #Dentro del for deben estar todos los eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x=10
                    jp.var_y=0
                if event.key == pygame.K_LEFT:
                    jp.var_x=-10
                    jp.var_y=0
            #Es un evento cuando la tecla se levanta
            if event.type == pygame.KEYUP:
                jp.var_x=0
                jp.var_y=0

            if event.type == pygame.QUIT:
                fin=True

        #Gestion de colision
        #Cuando esta en False el objeto no se destruye, pero si incrementa el contador de puntos
        #Cuando esta en True el objeto se destruye
        pos_x1=250
        pos_y1=525
        ls_col=pygame.sprite.spritecollide(jp, rivales, True)
        for elemento in ls_col:
            vida=vida-1
            print (vida)


        ls_col=pygame.sprite.spritecollide(l, rivales, True)
        for elemento in ls_col:
             ptos+=1
             print ptos #Variable puntos (almacena puntos obtenidos)

        if vida == 0:
            fin_juego=True


        if not fin_juego:

           general.update()
           rivales.update()
           line.update()
           pantalla.fill(BLANCO)
           general.draw(pantalla)

           if vida==2:
             pygame.draw.rect(pantalla, NEGRO, (250, 525, 30, 30))

           if vida==1:
              pygame.draw.rect(pantalla, NEGRO, (250, 525, 30, 30))
              pygame.draw.rect(pantalla, NEGRO, (200, 525, 30, 30))

           texto1=fuente.render("VIDA: ",True, NEGRO)
           texto2=fuente.render(str(vida),True, NEGRO)
           pantalla.blit(texto1,[40,530])
           pantalla.blit(texto2,[120,530])

           pygame.draw.line(pantalla, NEGRO, (0,480), (800,480),10)
           pygame.draw.line(pantalla, NEGRO, (50,500), (750,500),5)
           pygame.display.flip()
           #Despues de esta parte se controla los movimientos el tiempo que lleva
           reloj.tick(60)

        else:
           texto=fuente.render("Fin de juego", True, BLANCO)
           pantalla.fill(NEGRO)
           pantalla.blit(texto,[320,300])
           pygame.display.flip()
