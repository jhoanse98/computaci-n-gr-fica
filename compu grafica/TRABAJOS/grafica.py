import pygame

if __name__=='__main__':
    pygame.init()
    print 'funciona...'
    pantalla=pygame.display.set_mode([600,600])
    '''
    pygame.draw.line(pantalla, [255,0,0], [100,100], [200,200])
    pygame.display.flip()
    '''
    fin=False
    c=0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
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
