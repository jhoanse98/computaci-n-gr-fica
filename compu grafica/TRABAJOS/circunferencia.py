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
    fin=False
    lista=[]
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                X,Y=pygame.mouse.get_pos()
                pygame.draw.circle(pantalla, [0,255,0], [X,Y], 30, 1)
                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    X+=10
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla, [0,255,0], [X,Y], 30, 1)
                    #pygame.draw.circle(pantalla, [0,0,0], [X-10,Y], 30, 1)
                    pygame.display.flip()
                if event.key == pygame.K_LEFT:
                    X-=10
                    #pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla, [0,255,0], [X,Y], 30, 1)
                    pygame.draw.circle(pantalla, [0,0,0], [X+10,Y], 30, 1)
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    Y+=10
                    pygame.draw.circle(pantalla, [0,255,0], [X,Y], 30, 1)
                    pygame.draw.circle(pantalla, [0,0,0], [X,Y-10], 30, 1)
                    pygame.display.flip()
                if event.key == pygame.K_UP:
                    Y-=10
                    pygame.draw.circle(pantalla, [0,255,0], [X,Y], 30, 1)
                    pygame.draw.circle(pantalla, [0,0,0], [X,Y+10], 30, 1)
                    pygame.display.flip()
