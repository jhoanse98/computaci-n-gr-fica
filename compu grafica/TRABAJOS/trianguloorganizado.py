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
    verticesorigen=[[0,0]]
    cartesiana=[]
    apantalla=[[320,240]]
    enpantalla=[]
    escalar=[1,1]
    aumentoescalar=[]
    rotativa=[]
    vectiorigen2=[]
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
                enpantalla.append(pos)
                coorcartesiana=acartesiana(pos)
                cartesiana.append(coorcartesiana)
                c+=1
                if c==3:
                    vertice1=desdeorigen(cartesiana[0],cartesiana[1])
                    verticesorigen.append(vertice1)
                    vertice1=traslacion(vertice1)
                    apantalla.append(vertice1)
                    vertice2=desdeorigen(cartesiana[0],cartesiana[2])
                    verticesorigen.append(vertice2)
                    vertice2=traslacion(vertice2)
                    apantalla.append(vertice2)
                    pygame.draw.polygon(pantalla, [0,255,255], enpantalla,1)
                    pygame.draw.polygon(pantalla, [0,255,0], apantalla,1)
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    escalar[0]=escalar[0]+1
                    escalar[1]=escalar[1]+1
                    for a in verticesorigen:
                        pygame.draw.polygon(pantalla, [0,0,0], enpantalla,1)
                        b=escalarteclado(a,escalar)
                        F=deregreso(b,cartesiana[0])
                        T=traslacion(F)
                        aumentoescalar.append(T)
                        if len(aumentoescalar)==4:
                            pygame.draw.polygon(pantalla, [0,0,0], aumentoescalar,1)
                            del(aumentoescalar[0])
                            del(aumentoescalar[0])
                            del(aumentoescalar[0])
                    pygame.draw.polygon(pantalla, [0,255,255], aumentoescalar,1)
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    for a in verticesorigen:
                        b=rotacionhoraria(a)
                        vectiorigen2.append(b)
                        F=deregreso(b,cartesiana[0])
                        T=traslacion(F)
                        rotativa.append(T)

                        if len(rotativa)==4:
                            pygame.draw.polygon(pantalla, [0,0,0], rotativa,1)
                            del(rotativa[0])
                            del(rotativa[0])
                            del(rotativa[0])
                            del(vectiorigen2[0])
                            del(vectiorigen2[0])
                            del(vectiorigen2[0])
                    verticesorigen[:3]=vectiorigen2[:3]
                    pantalla.fill([0,0,0])
                    pygame.draw.line(pantalla, [255,255,0], [320,0], [320,480])
                    pygame.draw.line(pantalla, [255,255,0], [0,240], [640,240])
                    pygame.draw.polygon(pantalla, [0,255,0], apantalla,1)
                    pygame.draw.polygon(pantalla, [0,255,255], rotativa,1)
                    pygame.display.flip()
