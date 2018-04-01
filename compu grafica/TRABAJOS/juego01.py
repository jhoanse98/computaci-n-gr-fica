##Sprite Movimiento de Bloque (JUGADOR)
import pygame
import random


ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
BLANCO=(255,255,255)
NEGRO=(0,0,0)

ANCHO=800
ALTO=600

class Jugador(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()

        #Variable (Variacion en X) como se mueve el jugadores
        self.var_x=0



    def update(self):
        self.rect.x+=self.var_x

        if self.rect.x>= ANCHO - self.rect.width:
            self.var_x=0

        elif (self.rect.x<= 0):
            self.var_x=0


class Vida_C(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.var_x=0
        self.var_y=0

class No_Vida(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.var_x=0
        self.var_y=0



class Linea_Blanca(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.var_x=0

class Rival(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()

        self.rect.y=0
        #Variable (Variacion en Y) como se mueve los rivales
        self.var_y=2
        self.var_x=0

        self.temporizador=random.randrange(3000)

    def update(self):

        if self.temporizador >= 0:
            self.temporizador -= 2

        else:
            self.rect.y+=self.var_y

            #if self.rect.y>= ALTO - 140:
            #    self.var_y=-2
            #elif (self.rect.y<= 0):
            #    self.var_y=2

#Los movimientos de los jugadores deben estar en la clase


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    jp=Jugador (100,30)   #Variable tipo Bloque

    Ll=Linea_Blanca(800,10)
    #  Los sprite se manejan por grupos
    general= pygame.sprite.Group() #creamos un grupo de sprite llamado general
    general.add(jp)
    general.add(Ll)


    Ll.rect.x=0
    Ll.rect.y=480

    jp.rect.x=350
    jp.rect.y=450
    ptos=0
    vida=3


    fuente=pygame.font.Font(None,36)

    reloj=pygame.time.Clock()

    rivales=pygame.sprite.Group() #creamos un grupo de sprite llamado rivales
    Cuadros=pygame.sprite.Group() #creamos un grupo de sprite llamado cuadros vida
    ChaoVida=pygame.sprite.Group() #creamos un grupo de sprite llamado termina vida

    aux_x=150
    for i in range(3):
        aux_y=550
        CuadroVida=Vida_C(30,30)

        CuadroVida.rect.x=aux_x
        CuadroVida.rect.y=aux_y
        aux_x+=50

        Cuadros.add(CuadroVida)
        general.add(CuadroVida)


    n=10
    for i in range(n):
        r=Rival(20,20)
        #Para que la posicion donde aparece sea random
        r.rect.x=random.randrange(10,ANCHO - 20)
        r.rect.y=(-150)

        rivales.add(r)
        general.add(r)

    fin_juego=False
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        #Gestion de eventos
        #Dentro del for deben estar todos los eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x=5
                    jp.var_y=0
                if event.key == pygame.K_LEFT:
                    jp.var_x=-5
                    jp.var_y=0
                if event.key == pygame.K_SPACE:
                    jp.var_x=0
                    jp.var_y=0
            #Es un evento cuando la tecla se levanta
            if event.type == pygame.KEYUP:
                jp.var_x=0
                jp.var_y=0
            if event.type == pygame.QUIT:
                fin=True

        #Gestion de colision
        #Cuando esta en False el objeto no se destruye, pero si incrementa el contador de puntos
        #Cuando esta en True el objeto se destruye
        ls_col=pygame.sprite.spritecollide(jp, rivales, True)
        for elemento in ls_col:
            ptos+=1
            for i in range(1,2):
                r=Rival(20,20)
                #Para que la posicion donde aparece sea random
                r.rect.x=random.randrange(10,ANCHO - 20)
                r.rect.y=(-150)
                rivales.add(r)
                general.add(r)

            #print ptos #Variable puntos (almacena puntos obtenidos)

        aux_x1=250
        aux_y1=550
        ll_col=pygame.sprite.spritecollide(Ll, rivales, True)
        for elemento in ll_col:

            for i in range(0,1):
                r=Rival(20,20)
                #Para que la posicion donde aparece sea random
                r.rect.x=random.randrange(10,ANCHO - 20)
                r.rect.y=(-150)
                rivales.add(r)
                general.add(r)

                #vida=vida-1
                #print vida

                if vida==2:
                    cvida=No_Vida(30,30)
                    cvida.rect.x=aux_x1
                    cvida.rect.y=aux_y1
                    ChaoVida.add(cvida)
                    general.add(cvida)

                if vida==1:
                    cvida=No_Vida(30,30)
                    cvida.rect.x=aux_x1-50
                    cvida.rect.y=aux_y1
                    ChaoVida.add(cvida)
                    general.add(cvida)





            #Va quitando las vidas

            #vida-=1
            #if vida<=0:
            #    break
            #print vida






        jp.update()
        rivales.update()


        if vida<=0:
            fin_juego=True

        #if ptos>20:
        #    fin_juego=True

        #Actualizacion de pantalla
        #En esta parte es la actualizacion de la pantalla (Refresco de la pantalla)
        if not fin_juego:
            general.update()
            pantalla.fill(BLANCO)
            general.draw(pantalla)
            ####
            pygame.draw.line(pantalla,AZUL,(0,490), (800,490))
            pygame.draw.line(pantalla,AZUL,(20,495), (780,495))
            pygame.draw.line(pantalla,AZUL,(40,500), (760,500))
            pygame.draw.line(pantalla,AZUL,(60,505), (740,505))


            ### imprime vida
            texto3=fuente.render("VIDA: ",True, NEGRO)
            texto4=fuente.render(str(vida),True, NEGRO)
            pantalla.blit(texto3,[40,550])
            pantalla.blit(texto4,[120,550])
            ###
            ### imprime puntos
            texto1=fuente.render("PUNTOS: ",True, NEGRO)
            texto2=fuente.render(str(ptos), True, NEGRO)
            pantalla.blit(texto1,[600,550])
            pantalla.blit(texto2,[720,550])
            ###
            pygame.display.flip()
            #Despues de esta parte se controla los movimientos el tiempo que lleva
            reloj.tick(60)

        else:
            texto=fuente.render("Fin de juego", True, BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto,[320,300])
            pygame.display.flip()
