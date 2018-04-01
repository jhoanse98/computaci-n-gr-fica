import pygame
import math

ANCHO=640
ALTO=480
ORIGENX=320
ORIGENY=240

def traslacion (C):# a pantalla
    X1= ORIGENX+C[0]
    Y1= ORIGENY-C[1]
    return [X1,Y1]

def acartesiana(C):
        X=C[0]-ORIGENX
        Y=ORIGENY-C[1]
        return [X,Y]

def desdeorigen(C,D):
    x=D[0]-C[0]
    y=D[1]-C[1]
    return [x,y]

def norma(A):
    P=math.sqrt(A[0]**2+A[1]**2)
    return P

def producpunto(A,B):
    Q=(A[0]*B[0])+(A[1]*B[1])
    return Q

def angulo(A,B):
    P=producpunto(A,B)/(norma(A)*norma(B))
    angu=math.degrees(math.acos(P))
    return angu

def traslacion2(tupla):
    for elementos in tupla:
        X1=ORIGENX+int(elementos[0])
        Y1=ORIGENY+ int(elementos[1])
        pygame.draw.line(pantalla, [255,255,0], [340,250], [X1,Y1])
        pygame.display.flip()

def escalar(X,Y, ESCA):
    X1=X*ESCA
    Y1=Y*ESCA
    pygame.draw.line(pantalla, [255,255,0], [340,250], [X1,Y1])
    pygame.display.flip()


if __name__=='__main__':
    pygame.init()
    fin=False
    c=0
    l=[]
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.draw.line(pantalla, [255,255,0], [320,0], [320,480])
    pygame.draw.line(pantalla, [255,255,0], [0,240], [640,240])
    pygame.display.flip()
    #pygame.draw.line(pantalla, [255,255,0], [350,400], [450,300])
    #pygame.draw.line(pantalla, [255,255,0], [350,400], [200,350])
    #P=((-80,200),(100,-100))
    #traslacion2(P)
    #traslacion(-80,200)
    #traslacion(100,-100)
    #traslacion(20,100)
    #T=raw_input("digite el valor del escalar: ")
    #escalar(20,20, int(T))
    #pygame.display.flip()
    #X=raw_input("digite coordenada x: ")
    #Y=raw_input("digite coordenada y: ")
    #traslacion(int(X),int(Y))
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                c+=1
                if c==1:
                    c1=pos
                    P= acartesiana(c1)
                    print c1, " coordenadas de pantalla"
                    print P, " coordenadas cartesianas"
                if c==2:
                    c2=pos
                    Q=acartesiana(c2)
                    print c2, "coordenadas de pantalla 2"
                    print Q, "coordenadas cartesianas 2"
                    C3= desdeorigen(P,Q)
                    print C3, "puntos  cartesianos 1 y 2 trasladados al origen"
                    Z=traslacion(C3)
                    print Z, "punto C3 desde orige cartesiano pero en base a la pantalla"
                    pygame.draw.line(pantalla,[0,255,0],c1,c2,1)
                    pygame.draw.line(pantalla,[0,255,0], (320,240), Z,1)
                    pygame.display.flip()
                    #l.append(C3)
                    #if len(l)>=2:
                    #    print angulo(l[-1],l[-2])
                    #c=0


# coseno director

# estudiar ecuacion de una recta
#  angulos entre dos rectas
#rectas ortogonales
