import pygame
import random
import math
from clases2 import *

blanco=[255,255,255]
negro=[0,0,0]
Azul=[0,0,255]
Rojo=[255,0,0]
ANCHO=940
ALTO=520

def distancia(p1,p2):
    return math.sqrt((p1.rect.x -p2.rect.x)**2 +(p1.rect.y-p2.rect.y)**2)

def acercar(dist, enemigo, jugador):
    #print jugador.rect.x, enemigo.rect.x
    if dist > 230 and not((enemigo.accion==3) or (enemigo.accion==8)):
        if jugador.rect.x < enemigo.rect.x and enemigo.rect.x > 50:
            enemigo.left()
        elif jugador.rect.x > enemigo.rect.x and enemigo.rect.x < ANCHO -50:
            enemigo.right()
    else:
        enemigo.golpear()



def recortar(max_x, max_y, archivo, vector):
    imagen=pygame.image.load(archivo)
    info=imagen.get_rect()
    an_imagen=info[2]
    al_imagen=info[3]
    an_image_corte= an_imagen/max_x
    al_image_corte= al_imagen/max_y
    mapa=[]
    for i in range(max_y):
        mapis=[]
        for j in range(vector[i]):
            cuadro=imagen.subsurface(j*an_image_corte, i*al_image_corte, an_image_corte, al_image_corte)
            mapis.append(cuadro)
        mapa.append(mapis)
    return mapa


def juego():
    pygame.init()
    GAME_OVER=False
    c=0
    fin=False
    cara=pygame.image.load('cara sailor.png')
    fuente=pygame.font.Font(None, 30)
    fuente2=pygame.font.Font(None, 80)
    txt_pausa=fuente.render("PAUSA", False, blanco)
    txt_puntaje=fuente.render("PUNTAJE", False, Azul)
    parada=True
    reloj = pygame.time.Clock()
    pygame.display.set_caption("sailor moon's game")
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    flag=True
    flag2=True
    pygame.mixer.music.load("escenario1.mp3")
    pygame.mixer.music.play(-1)
    resultado=False

    modificadores=pygame.sprite.Group()
    golosinas=pygame.sprite.Group()
    pasteles=pygame.sprite.Group()
    helados=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    todos=pygame.sprite.Group()
    barrasenemigas=pygame.sprite.Group()



    barradevidasprite='barras de vida.png'
    barritadevida=recortar(5,1, barradevidasprite,[5])


    barrasdevida=barravida_jugador(barritadevida)
    barras=pygame.sprite.Group()
    barras.add(barrasdevida)

    cantidad_enemigos=10
    enemiga1sprites='enemiga1final.png'
    enemigaln=recortar(9,8, enemiga1sprites, [4,7,5,9,4,7,5,9])
    reptilsprites='reptilfinal2.png'
    reptiln=recortar(6,10, reptilsprites, [5,6,5,6,6,5,6,5,6,6])
    ninjasprites='ninjas derecha.png'
    ninjasln=recortar(7,10, ninjasprites, [7,6,3,7,5,7,6,3,7,5])
    barradevidaspriteenemiga='barras de vida.png'
    barritadevidaenemiga=recortar(5,1, barradevidasprite,[5])

    for R in range(cantidad_enemigos):
        x=random.randrange(-5000,5000)
        y=random.randrange(200,250)
        reptil=reptiles(reptiln,barrasenemigas, barritadevidaenemiga, [x,y])
        enemigos.add(reptil)
        todos.add(reptil)

    """for M in range(cantidad_enemigos):
        x=random.randrange(-10000,10000)
        y=random.randrange(200,250)
        ninja=ninjas(ninjasln,barrasenemigas, barritadevidaenemiga, [x,y])
        enemigos.add(ninja)
        todos.add(ninja)

    for E in range(1):
        x=random.randrange(-10000,10000)
        y=random.randrange(200,250)
        enemiga=enemigas(enemigaln, barrasenemigas, barritadevidaenemiga, [x,y])
        enemigos.add(enemiga)
        todos.add(enemiga)"""


    fondito=fondo()
    fondos=pygame.sprite.Group()
    fondos.add(fondito)
    todos.add(barrasdevida)
    #todos.add(barradevida2)

    protagonista1sprite='protagonista1.png'
    protagonista1=recortar(11,16,protagonista1sprite,[1,11,10,8,7,7,11,7,1,11,10,8,7,7,11,7])


    """protagonista2sprite='protagonista2 final.png'
    protagonista2=recortar(12,16,protagonista2sprite,[2,12,9,9,3,9,10,6,2,12,9,9,3,9,10,6])"""


    jugador1=jugador(protagonista1)
    #colega1=colega(protagonista2)



    jugadores=pygame.sprite.Group()
    #colegas=pygame.sprite.Group()
    jugadores.add(jugador1)
    #colegas.add(colega1)
    todos.add(jugador1)
    #todos.add(colega1)

    pause = False
    while not GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_OVER=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador1.j=0
                    jugador1.mov=False
                    jugador1.dir=True
                    jugador1.accion=1
                    jugador1.varx=20
                    parada =True
                    flag=True
                if event.key == pygame.K_LEFT:
                    jugador1.j=0
                    jugador1.mov=False
                    jugador1.dir=False
                    jugador1.flag=True
                    jugador1.cambiodir=8
                    jugador1.accion=1
                    jugador1.varx=-20
                    parada=False
                    flag=False

                if event.key == pygame.K_UP:
                    if jugador1.dir:
                        jugador1.j=0
                        flag2=True
                        jugador1.mov=False
                        jugador1.accion=1
                        jugador1.vary=-5
                        print jugador1.rect.y
                    else:
                        jugador1.j=0
                        flag2=True
                        jugador1.mov=False
                        jugador1.flag=True
                        jugador1.accion=1
                        jugador1.vary=-5
                        jugador1.cambiodir=8
                if event.key == pygame.K_DOWN:
                    if jugador1.dir:
                        jugador1.j=0
                        flag2=False
                        jugador1.mov=False
                        jugador1.accion=1
                        jugador1.vary=+5
                    else:
                        jugador1.j=0
                        flag2=False
                        jugador1.mov=False
                        jugador1.flag=True
                        jugador1.accion=1
                        jugador1.vary=5
                        jugador1.cambiodir=8


                if event.key == pygame.K_s:
                    if jugador1.dir:
                        jugador1.accion=2
                        jugador1.j=0
                    else:
                        jugador1.flag=True
                        jugador1.accion=2
                        jugador1.cambiodir=8
                        jugador1.j=0
                if event.key == pygame.K_c:
                    if jugador1.dir:
                        jugador1.accion=4
                        jugador1.j=0
                    else:
                        jugador1.flag=True
                        jugador1.accion=4
                        jugador1.cambiodir=8
                        jugador1.j=0
                if event.key == pygame.K_x:
                    if jugador1.dir:
                        jugador1.accion=5
                        jugador1.j=0
                    else:
                        jugador1.flag=True
                        jugador1.accion=5
                        jugador1.cambiodir=8
                        jugador1.j=0
                if event.key == pygame.K_z:
                    if jugador1.dir:
                        jugador1.accion=7
                        jugador1.j=0
                    else:
                        jugador1.flag=True
                        jugador1.accion=7
                        jugador1.cambiodir=8
                        jugador1.j=0


                if event.key == pygame.K_p:
                    if not pause:
                        pause=True
                    else:
                        pause=False



            if (jugador1.accion==2 or jugador1.accion==4 or jugador1.accion==5 or jugador1.accion==7):
                jugador1.sonido.set_volume(2.0)
                jugador1.sonido.play()
                if jugador1.dir:
                    punto=[jugador1.rect.x+150,jugador1.rect.y+40]
                else:
                    punto=[jugador1.rect.x-50, jugador1.rect.y]
                for enemy in enemigos:
                    golpe_aenemigos=enemy.rect.collidepoint(punto)
                    if golpe_aenemigos:
                        jugador1.puntaje+=300
                        enemy.salud-=30
                        enemy.barra.comoloquierollamar()
                        if enemy.derecha:
                            enemy.i=0
                            enemy.accion=3
                            enemy.varx=-50
                        if enemy.izquierda:
                            enemy.i=0
                            enemy.accion=8
                            enemy.varx=+50
                        if enemy.Tmuerte<=0:
                            break



            if event.type == pygame.KEYUP:
                jugador1.varx=0
                jugador1.vary=0
                jugador1.mov=True
                parada=False
                flag=False






        for enemy in enemigos:
            if enemy.golpe:
                if enemy.derecha:
                    punto=[enemy.rect.x+300,enemy.rect.y+50]
                if enemy.izquierda:
                    punto=[enemy.rect.x-50,enemy.rect.y+50]
                golpe_protagonista=jugador1.rect.collidepoint(punto)
                if golpe_protagonista:
                    print("fist")
                    jugador1.salud-=20
                    jugador1.c+=1
                    if jugador1.dir:
                        jugador1.j=0
                        jugador1.accion=3
                        jugador1.varx=-20
                        enemy.golpe=False
                    else:
                        jugador1.j=0
                        jugador1.accion=3
                        jugador1.varx=20
                        enemy.golpe=False
                    if jugador1.salud>=0:
                        if jugador1.c>=4:
                            jugador1.c=4
                        print jugador1.salud, jugador1.c
                        barrasdevida.image=barrasdevida.v[0][jugador1.c]
                    else:
                        GAME_OVER=True

        if jugador1.salud<=0:
            GAME_OVER=True


        for player in jugadores:
            if player.Tmuerte<=0:
                jugadores.remove(player)
                todos.remove(player)


        for enemy in enemigos:
            if enemy.Tmuerte<=0:
                cantidad_enemigos-=1
                print enemy.donacion
                if enemy.donacion>=5:
                    Pastel=pastel([enemy.rect.x,350])
                    pasteles.add(Pastel)
                    modificadores.add(Pastel)
                    todos.add(Pastel)
                elif enemy.donacion>=0:
                    Helado=helado([enemy.rect.x,350])
                    helados.add(Helado)
                    modificadores.add(Helado)
                    todos.add(Helado)
                else:
                    Golosina=golosina([enemy.rect.x,350])
                    golosinas.add(Golosina)
                    modificadores.add(Golosina)
                    todos.add(Golosina)
                barrasenemigas.remove(enemy.barra)
                enemigos.remove(enemy)
                todos.remove(enemy)

        for modi in modificadores:
            if modi.Ttime<=0:
                if modi.id==0:
                    pasteles.remove(modi)
                    modificadores.remove(modi)
                    todos.remove(modi)
                elif modi.id==1:
                    helados.remove(modi)
                    modificadores.remove(modi)
                    todos.remove(modi)

        for cake in pasteles:
            ls_colu=pygame.sprite.spritecollide(jugador1, pasteles, False)
            for u in ls_colu:
                jugador1.c-=1
                if jugador1.c<=0:
                    jugador1.c=0
                cake.sonido.play()
                barrasdevida.image=barrasdevida.v[0][jugador1.c]
                jugador1.salud=jugador1.salud+20
                pasteles.remove(cake)
                modificadores.remove(cake)
                todos.remove(cake)

        for icescream in helados:
            ls_colu=pygame.sprite.spritecollide(jugador1, helados, False)
            for u in ls_colu:
                jugador1.puntaje+=1000
                icescream.sonido.play()
                modificadores.remove(icescream)
                helados.remove(icescream)
                todos.remove(icescream)

        for sweet in golosinas:
            ls_colu=pygame.sprite.spritecollide(jugador1, golosinas, False)
            for u in ls_colu:
                jugador1.Tiempo+=20
                if jugador1.Tiempo>=120:
                    jugador1.Tiempo=120
                modificadores.remove(sweet)
                golosinas.remove(sweet)
                todos.remove(sweet)




        if jugador1.rect.x>512 and parada:
            fondito.varx=10
            for m in modificadores:
                if m.rect.x>500:
                    m.desplazar()
            jugador1.varx=0
            fondito.movefondo()
            if math.fabs(fondito.rect.x)>math.fabs(ANCHO-3254) and parada:
                fondito.varx=0
                fondito.rect.x=ANCHO-3264
                parada=False
        else:
            fondito.varx=0

        if cantidad_enemigos<=0 and jugador1.rect.x>850:
            resultado=True
            GAME_OVER=True

        if fondito.rect.x==ANCHO-3264 and flag:
            parada=False
            jugador1.varx=10


        if cantidad_enemigos>0 and jugador1.rect.x>700 and flag :
            jugador1.varx=0

        if jugador1.rect.x<=-100 and not flag:
            jugador1.varx=0

        if jugador1.rect.y<=180 and flag2:
            jugador1.vary=0

        if jugador1.rect.y>=ALTO-250 and not(flag2):
            jugador1.vary=0


        if not pause:
            todos.update()
            pantalla.fill(negro)
            fondos.draw(pantalla)
            barrasenemigas.draw(pantalla)
            todos.draw(pantalla)
            txt_puntos=fuente.render(str(jugador1.puntaje), False, blanco)
            txt_tiempo=fuente2.render(str(jugador1.Tiempo), False, Rojo)
            pantalla.blit(cara, [20,20])
            pantalla.blit(txt_puntaje, [100,60])
            pantalla.blit(txt_puntos, [200,60])
            pantalla.blit(txt_tiempo, [450,30])
            pygame.display.flip()

            for enemy in enemigos:
                distance=distancia(jugador1, enemy)
                acercar(distance, enemy, jugador1)

            reloj.tick(8)
        else:
            pantalla.blit(txt_pausa, [500,300])
            pygame.display.flip()
    return [resultado,jugador1.puntaje]
