import pygame
import math

ANCHO=640
ALTO=480
ORIGENX=320
ORIGENY=240

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.flip()
    reloj=pygame.time.Clock()
    a=False
    b=False
    c=False
    d=False
    fin=False
    pos=[0,330]
    pantalla.fill([0,0,0])
    pygame.draw.circle(pantalla, [0,255,0], pos, 5, 1)
    #pygame.draw.circle(pantalla, [0,0,0], [X-10,Y], 30, 1)
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    a=True
                    b=False
                    c=False
                    d=False
                if event.key == pygame.K_LEFT:
                    b=True
                    d=False
                    c=False
                    a=False
                if event.key == pygame.K_UP:
                    c=True
                    b=False
                    d=False
                    a=False
                if event.key == pygame.K_DOWN:
                    d=True
                    b=False
                    c=False
                    a=False
        if a:
            pos[0]+=10
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla, [0,255,0], pos, 5, 1)
            pygame.display.flip()
        if b:
            pos[0]-=10
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla, [0,255,0], pos, 5, 1)
            pygame.display.flip()
        if c:
            pos[1]-=10
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla, [0,255,0], pos, 5, 1)
            pygame.display.flip()

        if d:
            pos[1]+=10
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla, [0,255,0], pos, 5, 1)
            pygame.display.flip()
        reloj.tick(30)
