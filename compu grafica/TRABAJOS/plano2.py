import pygame
from plano import traslacion

origenx=340
origeny=250

if __name__=='__main__':
    pygame.init()
    print 'funciona...'
    fin=False
    pantalla=pygame.display.set_mode([640,480])
    pygame.draw.line(pantalla, [255,0,0], [340,0], [640,250])
    pygame.draw.line(pantalla, [255,0,0], [0,250], [0,250])
    pygame.draw.line(pantalla, [255,0,0], [350,400], [450,300])
    pygame.draw.line(pantalla, [255,0,0], [350,400], [200,350])
    pygame.display.flip()
