import sys
import pygame, time
# ###
# Proof: LogB(M•N)= LogB(M)+LogB(N), where B, M & N are numbers.
# ###

def start_menu(surface):
    color='white'
    title = pygame.font.SysFont('' , 40)
    Laws = pygame.font.SysFont('',17)
    pygame.draw.rect(surface,pygame.Color(color),(100,100,130,20),0)
    pygame.draw.rect(surface,pygame.Color(color),(100,150,130,20),0)
    pygame.draw.rect(surface,pygame.Color(color),(100,200,130,20),0)
    pygame.draw.rect(surface,pygame.Color(color),(100,250,130,20),0)
    pygame.draw.rect(surface,pygame.Color(color),(100,300,130,20),0)
    displayTitle=title.render('Log Laws',1,(248,248,255))
    surface.blit(displayTitle,(100,50))
    firstLaw=Laws.render('log_bxy=log_bx+log_by',1,(0,0,0))
    surface.blit(firstLaw,(100,104))
    return


def add():
    # ###
    # Input:
    # Motivation:
    # return:
    # ###
    return


def main():
    pygame.init()

    Surfacesize=(500,400)
    WindowTitle = 'Log Laws'
    frameDelay = 0.02

    surface = pygame.display.set_mode(Surfacesize,0,0)
    pygame.display.set_caption(WindowTitle)
    gameOver=False
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        start_menu(surface)
        pygame.display.update()

        time.sleep(frameDelay)

    # print('''This is a demonstration for "Log_B(M*N)=Log_B(M)+Log_B(N)":''')
    # input('''(Any key to continue)''')
    # X = input('''1. Let Log_B(M)=''')
    # Y = input('''2. Let Log_B(N)=''')
    # input('''3. B^{} and B^{}'''.format(X, Y))

main()