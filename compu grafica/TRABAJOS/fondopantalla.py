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
    x=10
    y=10
    reloj=pygame.time.Clock()
    overwatch=pygame.image.load('overwatch.jpeg')
    cara=pygame.image.load('cara.png')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.blit(overwatch, [0,0])
    pantalla.blit(cara,[10,10])
    pygame.display.flip()
    posicion=[0,0]
    x=0
    y=0
    flag=False
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        moupos=pygame.mouse.get_pos()
        print moupos
        if moupos[0]<100 and not(flag):
                x=-20
        if moupos[0]>100 and moupos[0]<540:
                x=0
                flag=False
        if moupos[0]>540:
                x=20
        if math.fabs(posicion[0])<= math.fabs(ANCHO-anchoimagen):
            posicion[0]=posicion[0]+x
        else:
            flag=True
            x=0
            posicion[0]=(ANCHO-anchoimagen)
        if posicion[0]>=0:
            x=0
            posicion[0]=0

        pantalla.fill([0,0,0])
        pantalla.blit(overwatch,posicion)
        pantalla.blit(cara,[10,10])
        pygame.display.flip()
        reloj.tick(10)

        #MOVER LA PANTALLA Y QUE LA IMAGEN NO SE SALGA DEL EXTREMO
        #PONER UN OBJETO Y CUANDO LLEGUE AL EXTREMO DE LA PANTALLA MOVER LA PANTALLA
        #COGER UN OBJETO Y QUE EL MOUSE SEA ESE OBJETO (CENTRADO)
