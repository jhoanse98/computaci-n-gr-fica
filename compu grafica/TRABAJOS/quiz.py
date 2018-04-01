import pygame
import math

ANCHO=640
ALTO=480
ORIGENX=320
ORIGENY=240

if __name__=='__main__':
    pygame.init()
    fin=False
    A=[]
    c=0
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    """
    pygame.draw.line(pantalla, [255,255,0], [320,0], [320,480])
    pygame.draw.line(pantalla, [255,255,0], [0,240], [640,240])
    pygame.display.flip()
    """
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                pygame.draw.line(pantalla, [255,255,0], [0,pos[1]], [ANCHO,pos[1]])
                pygame.display.flip()
                A.append(pos)
                c+=1
                if c==3:
                    X=A[2][0]
                    Y=A[2][1]
                    print X,Y
                    print A
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if Y<(A[1][1]-20):
                        Y+=20
                        pygame.draw.line(pantalla, [255,255,0], [0,Y], [ANCHO,Y], 1)
                        pygame.draw.line(pantalla, [0,0,0], [0,Y-20],[ANCHO,Y-20] , 1)
                        pygame.display.flip()
                if event.key == pygame.K_UP:
                    if Y>(A[0][1]+20):
                        Y-=20
                        pygame.draw.line(pantalla, [255,255,0], [0,Y], [ANCHO,Y], 1)
                        pygame.draw.line(pantalla, [0,0,0], [0,Y+20],[ANCHO,Y+20] , 1)
                        pygame.display.flip()
