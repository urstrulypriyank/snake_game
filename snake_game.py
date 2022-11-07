import pygame
pygame.init()

# CONSTANT VARIABLE
WINDOW_WIDTH,WINDOW_HEGIHT = 1000,800
WINDOW_TITLE = "Snake Game"
# CONSTANT VARIABLES FOR COLORS
WHITE,BLACK,RED = (255,255,255),(0,0,0),(255,0,0)

# GAME SPECIFIC VARIABLE 
EXIT_GAME,QUIT_GAME = False,False

GAMEWINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEGIHT))
pygame.display.update()
pygame.display.set_caption(WINDOW_TITLE)


# METHOD TO SET BACKGROUD COLOR 
def set_backgroudColor(color):
    global GAMEWINDOW
    GAMEWINDOW.fill(color)
    pygame.display.update()


def main():
    # IMPORTING SOME GLOABL VARIABLES
    global EXIT_GAME,WHITE

    # GAME LOOP
    set_backgroudColor(WHITE)
    while not EXIT_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: EXIT_GAME = True
        
    else:
        pygame.quit()
        quit()       
if __name__ == "__main__":
    main()