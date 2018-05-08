import sys
import pygame, time
# ###
# Proof: LogB(M•N)= LogB(M)+LogB(N), where B, M & N are numbers.
# ###

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
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        time.sleep(frameDelay)
        
main()