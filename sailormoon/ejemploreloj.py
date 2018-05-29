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
    pag=1
    fuente=pygame.font.Font(None, 30)
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pag+=1

        if pag==1:
            texto=fuente.render("pagina1", True, blanco)
            pantalla.fill([0,0,0])
            pantalla.blit(texto, [100,100])
            pantalla.display.flip()
            reloj.tick(15)
