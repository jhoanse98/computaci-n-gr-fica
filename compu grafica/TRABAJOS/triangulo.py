import pygame
import math

ANCHO=640
ALTO=480
ORIGENX=320
ORIGENY=240
D=[1,1]

def desdeorigen(C,D):
    x=D[0]-C[0]
    y=D[1]-C[1]
    return [x,y]

def deregreso(C,D):
    X=D[0]+C[0]
    Y=D[1]+C[1]
    return [X,Y]

def acartesiana(C):
        X=C[0]-ORIGENX
        Y=ORIGENY-C[1]
        return [X,Y]

def traslacion (C):# a pantalla
    X1= ORIGENX+C[0]
    Y1= ORIGENY-C[1]
    return [X1,Y1]

def escalarteclado(C,D):
    X=C[0]*D[0]
    Y=C[1]*D[1]
    return [X,Y]



def rotacionhoraria(puntos):
    a=int(math.cos(math.pi/2))
    b=int(math.sin(math.pi/2))
    X=puntos[0]*a + puntos[1]*b
    Y=puntos[0]*-b + puntos[1]*a
    return [X,Y]


def rotacionantihoraria(puntos,angulo):
    X=int(puntos[0]*math.degrees(math.cos(angulo)))-1*int(puntos[1]*math.degrees(math.sin(angulo)))
    Y=int(puntos[0]*math.degrees(math.sin(angulo)))+int(puntos[1]*math.degrees(math.cos(angulo)))
    return [X,Y]

if __name__=='__main__':
    pygame.init()
    fin=False
    c=0
    vertices=[[0,0]]
    PRUEBA=[]
    l=[]
    E=[]
    C=[[320,240]]
    D=[1,1]
    F=[]
    G=[]
    K=[]
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.draw.line(pantalla, [255,255,0], [320,0], [320,480])
    pygame.draw.line(pantalla, [255,255,0], [0,240], [640,240])
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                PRUEBA.append(pos)
                A=acartesiana(pos)
                l.append(A)
                print l
                c+=1
                if c==3:
                    vertice1=desdeorigen(l[0],l[1])
                    vertices.append(vertice1)
                    VERTICE1=traslacion(vertice1)
                    C.append(VERTICE1)
                    vertice2=desdeorigen(l[0],l[2])
                    vertices.append(vertice2)
                    VERTICE2=traslacion(vertice2)
                    C.append(VERTICE2)
                    pygame.draw.polygon(pantalla, [0,255,0], C,1)
                    pygame.draw.polygon(pantalla, [0,255,0], PRUEBA,1)
                    pygame.display.flip()
                    print vertices
                    c=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    D[0]=D[0]+1
                    D[1]=D[1]+1
                    for a in vertices:
                        b=rotacionhoraria(a)
                        F=deregreso(b,l[0])
                        T=traslacion(F)
                        E.append(T)
                        print E, "E"
                        print vertices,"vertices"
                        if len(E)==4:
                            del(E[0])
                            del(E[0])
                            del(E[0])
                    pygame.draw.polygon(pantalla, [0,0,0], PRUEBA,1)
                    pygame.draw.polygon(pantalla, [255,255,0], E,1)
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    for punto in l:
                        puntos=rotacionhoraria(punto)
                        G.append(puntos)
                        puntopantalla=traslacion(puntos)
                        K.append(puntopantalla)
                        print K
                    if len(K)>4:
                        del(K[0])
                        del(K[0])
                        del(K[0])
                        G[0:3]=G[-1:-4]
                    print K
                    l[0:3]=G[0:3]
                    pygame.draw.polygon(pantalla, [0,255,0], K,1)
                    pygame.display.flip()
