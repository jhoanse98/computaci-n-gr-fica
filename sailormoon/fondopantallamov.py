import pygame
import math

anchoimagen=3840
altoimagen=2160
ANCHO=940
ALTO=480
ORIGENX=320
ORIGENY=240
D=[1,1]

if __name__=='__main__':
    pygame.init()
    fin=False
    reloj=pygame.time.Clock()
    overwatch=pygame.image.load('imagen de menu.png')
    cara=pygame.image.load('protagonista1 derecha.png')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.blit(overwatch, [-500,0])
    pantalla.blit(cara,[0,0])
    posicioncara=[0,0]
    pygame.display.flip()
    posicion=[0,0]
    varix=0
    variy=0
    flag1=False
    flag2=False
    flag3=False
    flag4=False
    parada1=True
    parada2=True
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
            flag3=True
            posicioncara[0]=ANCHO-128

        if flag3 and parada1:
            if math.fabs(posicion[0])<=math.fabs(anchoimagen-ANCHO):
                posicion[0]=posicion[0]-varix
                flag3=False
            else:
                posicion[0]=ANCHO-anchoimagen
                flag3=False
                parada1=False

        if  posicioncara[1]<=(ALTO-128) and not(flag2):
            posicioncara[1]=posicioncara[1]+variy
        else:
            flag2=True
            flag4=True
            posicioncara[1]=ALTO-128


        if flag4 and parada2:
            if math.fabs(posicion[1])<=math.fabs(altoimagen-ALTO):
                posicion[1]=posicion[1]-variy
                flag4=False
            else:
                posicion[1]=ALTO-altoimagen
                flag4=False
                parada2=False


        if posicioncara[0]<0:
            posicioncara[0]=0
            parada1=True
            posicion[0]=posicion[0]-varix
            if posicion[0]>=0:
                posicion[0]=0

        if posicioncara[1]<0:
            posicioncara[1]=0
            parada2=True
            posicion[1]=posicion[1]-variy
            if posicion[1]>=0:
                posicion[1]=0

        pantalla.fill([0,0,0])
        pantalla.blit(overwatch,[-50,0])
        pygame.display.flip()
        reloj.tick(15)
