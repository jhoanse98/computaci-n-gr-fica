import pygame
import math

ANCHO=640
ALTO=480
ORIGENX=320
ORIGENY=240
D=[1,1]

if __name__=='__main__':
    pygame.init()
    fin=False
    x=10
    y=10
    reloj=pygame.time.Clock()
    cara=pygame.image.load('cara.png')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.blit(cara, [10,10])
    posicion=[10,10]
    x=0
    y=0
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                    x+=2
            if event.key == pygame.K_LEFT:
                    x-=2
            if event.key == pygame.K_UP:
                y+=-2
            if event.key == pygame.K_DOWN:
                y+=2
        if event.type == pygame.KEYUP:
            x=0
            y=0
        print posicion
        pantalla.fill([0,0,0])
        if posicion[0]<= (ANCHO-128):
            posicion[0]=posicion[0]+x
        else:
            posicion[0]=ANCHO-128
        if posicion[1]<= (ALTO-128):
            posicion[1]=posicion[1]+y
        else:
            posicion[1]=ALTO-128

        pantalla.blit(cara, posicion)
        pygame.display.flip()
        reloj.tick(10)
