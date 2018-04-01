import pygame

ANCHO=640
ALTO=480
Verde=[0,255,0]
Azul=[0,0,255]
Rojo=[255,0,0]
Negro=[0,0,0]

class Bloque(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  #siempre que cree un sprite debo generar esas ttres lineas
        self.image=pygame.Surface([20,20])
        self.image.fill(Verde)
        self.rect=self.image.get_rect()
        self.rect.x=100


if __name__=='__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    usuario=Bloque()
    grupo=pygame.sprite.Group()
    grupo.add(usuario)
    usuario.rect.y=200
    grupo.draw(pantalla)
    pygame.display.flip()
    varx=0
    vary=0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_RIGHT:
                    #usuario.rect.x+=2
                    varx+=2
                    vary=0
                if event.key ==pygame.K_LEFT:
                    #usuario.rect.x-=2
                    varx-=2
                    vary=0
                if event.key ==pygame.K_DOWN:
                    #usuario.rect.y+=2
                    vary+=2
                    varx=0
                if event.key ==pygame.K_UP:
                    #usuario.rect.y-=2
                    vary-=2
                    varx=0
        usuario.rect.x+=varx
        usuario.rect.y+=vary
        pantalla.fill(Negro)
        grupo.draw(pantalla)
        pygame.display.flip()
        reloj.tick(100)
