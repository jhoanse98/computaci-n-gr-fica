import pygame

ANCHO=600
ALTO=480

if __name__=='__main__':
    pygame.init()
    print 'funciona...'
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    '''
    pygame.draw.line(pantalla, [255,0,0], [100,100], [200,200])
    pygame.display.flip()
    '''
    fin=False
    c=0
    altoo=ANCHO/20
    d=altoo
    while d<=ANCHO:
        pygame.draw.line(pantalla, [255,0,0], [d,0], [d,ALTO])
        pygame.display.flip()
        d+=altoo
    altoo=ALTO/20
    fin=False
    d=altoo
    while d<=ALTO:
        pygame.draw.line(pantalla, [255,0,0], [0,d], [ANCHO,d])
        pygame.display.flip()
        d+=altoo
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True





    '''
    if event.type == pygame.MOUSEBUTTONDOWN:
        print 'click'
        a=pygame.mouse.get_pos()
        c+=1
        if c==1:
            b=a
            print b
        if c==2:
            d=a
            print d
            pygame.draw.line(pantalla,[0,255,0], b, d)
            pygame.display.flip()
            c=0
    '''
