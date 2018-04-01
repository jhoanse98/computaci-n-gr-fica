from math import *
import pygame

ANCHO=640
ALTO=480
ORIGENX=320
ORIGENY=240

angulos=[0,15,30,45,60,90,100,120,140,160,180,210,240,270,300,330,360]

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
    X1= int(ORIGENX+C[0])
    Y1= int(ORIGENY-C[1])
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

def polares(angulo, radio=1):
    angu=radians(angulo)
    b=cos(angu)
    c=sin(angu)
    x=radio*b
    y=radio*c
    return [x,y]

def puntopolar(punto1,radio=1):
    pygame.draw.circle(pantalla, [255,255,255], traslacion(punto1), radio)

def linea(punto1,punto2, color=[255,255,255]):
    pygame.draw.line(pantalla, color, traslacion(punto1), traslacion(punto2))


def rosa(a,n,amp=100):
    np =[]
    a = radians(a)
    r = amp*cos(n*a)
    c = cos(a)
    s = sin(a)
    np = [int(r*c),int(r*s)]
    return np

def cardioide(i):
    np = []
    r = -100 -100*sin(i)
    c = cos(i)
    s = sin(i)
    np = [int(r*c),int(r*s)]
    return np

def cardioide2(i):
    np = []
    r = -100 +100*sin(i)
    c = cos(i)
    s = sin(i)
    np = [int(r*c),int(r*s)]
    return np

def cardioide3(i):
    np = []
    r = -100 -100*cos(i)
    c = cos(i)
    s = sin(i)
    np = [int(r*c),int(r*s)]
    return np

def cardioide4(i):
    np = []
    r = -100 +100*cos(i)
    c = cos(i)
    s = sin(i)
    np = [int(r*c),int(r*s)]
    return np

def espiral(a,b,i):
    np = []
    r = a + b*i
    c = cos(i)
    s = sin(i)
    np = [int(r*c),int(r*s)]
    return np

def cicloide(a,i,r=1):
    np =[]
    i = radians(i)
    c = cos(i)
    s = sin(i)
    np = [int(a*(i-s)),int(a*(1-c))]
    return np


if __name__=='__main__':
    pygame.init()
    fin=False
    c=0
    x=[0,360]
    var_x=x[0]
    """verticesorigen=[[0,0]]
    apantalla=[[320,240]]
    escalar=[1,1]"""
    reloj = pygame.time.Clock()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.draw.line(pantalla, [255,255,0], [320,0], [320,480])
    pygame.draw.line(pantalla, [255,255,0], [0,240], [640,240])

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        #linea(rosa(var_x,6,200), rosa(var_x+1,6,200))
        #puntopolar(polares(var_x,200),1)
        linea(cardioide(var_x), cardioide(var_x+1))
        linea(cardioide2(var_x), cardioide2(var_x+1))
        linea(cardioide3(var_x), cardioide3(var_x+1))
        linea(cardioide4(var_x), cardioide4(var_x+1))
        var_x=var_x+1
        #linea([200,0],[199,3])

        pygame.display.flip()

        reloj.tick(60)
