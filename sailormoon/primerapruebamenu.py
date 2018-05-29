import pygame
import math
import ConfigParser
from versionjuego399 import *
from clases import *

anchoimagen=3840
altoimagen=2160
ANCHO=940
ALTO=480
ORIGENX=320
ORIGENY=240
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO  = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


class opcion(pygame.sprite.Sprite):
    def __init__(self, texto):
        pygame.sprite.Sprite.__init__(self)  #siempre que cree un sprite debo generar esas ttres lineas
        self.color=BLANCO
        self.textos=texto
        self.background=NEGRO
        self.fuente=pygame.font.Font(None, 30)
        self.opcion=0
        self.fondo=pygame.image.load("intro1.png")
        self.text=self.fuente.render(self.textos, True, self.color, self.background)

    def update(self,opcion):
        if opcion:
            self.background=AZUL
            self.text=self.fuente.render(self.textos, False, self.color, self.background)
        else:
            self.background=NEGRO
            self.text=self.fuente.render(self.textos, False, self.color, self.background)



#if __name__ == '__main__':
def menu():
    pygame.init()
    fin=False
    c=0
    puntaje=0
    interprete= ConfigParser.ConfigParser()
    interprete.read('minimenu.menu')
    nom_ar=interprete.get('0', 'fondo')
    fondo=pygame.image.load(nom_ar)
    reloj = pygame.time.Clock()
    pygame.display.set_caption("Menu sailor moon")
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fondointro=pygame.image.load('imagen de menu.png')
    fuente=pygame.font.Font(None, 30)
    fuente2=pygame.font.Font(None, 80)
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play(1)
    opciones=[]
    opc=[0,0,0,0]
    i=0
    opciones=[]
    txt_inicio=opcion("Iniciar Partida")
    txt_inicio.fondo=pygame.image.load("menuprincipal.png")
    opciones.append(txt_inicio)
    txt_introduccion=opcion("Instrucciones")
    txt_introduccion.fondo=pygame.image.load("sprites efectos.png")
    opciones.append(txt_introduccion)
    txt_creditos=opcion("Creditos")
    txt_creditos.fondo=pygame.image.load("creditos.png")
    opciones.append(txt_creditos)
    txt_salir=opcion("Salir")
    opciones.append(txt_salir)
    txt_gameover=opcion("GAME OVER")
    txt_gameover.fondo=pygame.image.load("gameover.jpg")
    a=0
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if i==0:
                pantalla.blit(fondo, [0,0])
                pantalla.blit(opciones[0].text, [420,250])
                pantalla.blit(opciones[1].text, [420,300])
                pantalla.blit(opciones[2].text, [420,350])
                pantalla.blit(opciones[3].text, [420,400])
                if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if(a<=3):
                            opciones[1].opcion=0
                            opciones[2].opcion=0
                            opciones[0].opcion=0
                            opciones[3].opcion=0
                            opc[a]=1
                            opciones[a].opcion=opc[a]
                            opciones[a].update(opciones[a].opcion)
                            a+=1
                        else:
                            a=0
                            opc=[0,0,0,0]

                    if event.key == pygame.K_UP:
                        if a==4:
                            fondo=opciones[a-1].fondo
                            i=a
                        else:
                            fondo=opciones[a].fondo
                            i=a

            if i==1:
                if  event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        i=0
                        a=0
                        fondo=txt_inicio.fondo
                        print 'ya no'
                        break
                    else:
                        pygame.mixer.music.stop()
                        T=juego()
                        if T[0]:
                            puntaje=T[1]
                            i=6
                        else:
                            i=5
            if i==2:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        i=0
                        a=0
                        fondo=txt_inicio.fondo
                    else:
                        fondo=interprete.get(str(i), 'fondo')
                        fondo=opciones[a].fondo=pygame.image.load(fondo)
                        pantalla.blit(fondo, [0,0])
            if i==3:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        i=0
                        a=0
                        fondo=txt_inicio.fondo
                    else:
                        fondo=interprete.get(str(i), 'fondo')
                        fondo=opciones[a].fondo=pygame.image.load(fondo)
                        pantalla.blit(fondo, [0,0])
                        texto=fuente.render("JUEGO CREADO POR: ", False , NEGRO)
                        texto2=fuente.render("JHOAN SEBASTIAN MARIN", False, NEGRO)
                        pantalla.blit(texto, [650,100])
                        pantalla.blit(texto2, [650,150])
            if i==4:
                fin=True
                print "se cerro"


            if i==5:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        i=0
                        a=0
                        fondo=txt_inicio.fondo
                        pygame.mixer.music.load("intro.mp3")
                        pygame.mixer.music.play(1)
                    else:
                        fondo=interprete.get(str(i), 'fondo')
                        fondo=opciones[a].fondo=pygame.image.load(fondo)
                        pantalla.blit(fondo, [0,0])
                        pygame.mixer.music.load("game over.mp3")
                        pygame.mixer.music.play(1)
                    if event.key==pygame.K_o:
                        fin=True
                    if event.key==pygame.K_w:
                        i=6
            if i==6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        i=0
                        a=0
                        fondo=txt_inicio.fondo
                        pygame.mixer.music.load("intro.mp3")
                        pygame.mixer.music.play(1)
                    else:
                        fondo=interprete.get(str(i), 'fondo')
                        fondo=opciones[a].fondo=pygame.image.load(fondo)
                        pantalla.blit(fondo, [0,0])
                        tpuntaje=fuente2.render("TU PUNTAJE: ", False, NEGRO)
                        tpuntos=fuente2.render(str(puntaje), False, NEGRO)
                        pantalla.blit(tpuntaje, [300,200])
                        pantalla.blit(tpuntos, [400,250])
                        pygame.mixer.music.load("creditos.mp3")
                        pygame.mixer.music.play(1)

        for b in opciones:
            b.update(b.opcion)

        pygame.display.flip()
menu()
