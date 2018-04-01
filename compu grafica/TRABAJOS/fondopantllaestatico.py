import pygame
import math

anchoimagen=3840
altoimagen=2160
ANCHO=640
ALTO=480
ORIGENX=320
ORIGENY=240
D=[1,1]

if __name__=='__main__':
    pygame.init()
    fin=False
    reloj=pygame.time.Clock()
    overwatch=pygame.image.load('overwatch.jpeg')
    cara=pygame.image.load('index.jpeg')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.blit(overwatch, [0,0])
    pantalla.blit(cara,[0,0])
    posicioncara=[0,0]
    pygame.display.flip()
    posicion=[0,0]
    varix=0
    variy=0
    print a, b
    flag1=False
    flag2=False
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    varix=20
                if event.key == pygame.K_LEFT:
                    varix=-20
                    flag1=False
                if event.key == pygame.K_UP:
                    variy=-20
                    flag2=False
                if event.key == pygame.K_DOWN:
                    variy=20
            if event.type == pygame.KEYUP:
                varix=0
                variy=0
        if posicioncara[0]<=(ANCHO-128) and not(flag1):
            posicioncara[0]=posicioncara[0]+varix
        else:
            flag1=True
            posicioncara[0]=ANCHO-128
        if  posicioncara[1]<=(ALTO-128) and not(flag2):
            posicioncara[1]=posicioncara[1]+variy
        else:
            flag2=True
            posicioncara[1]=ALTO-128
        if posicioncara[0]<0:
            posicioncara[0]=0
        if posicioncara[1]<0:
            posicioncara[1]=0

        pantalla.fill([0,0,0])
        pantalla.blit(overwatch,posicion)
        pantalla.blit(cara,posicioncara)
        pygame.display.flip()
        reloj.tick(15)
