import pygame
pygame.init()

# CONSTANT VARIABLE
WINDOW_WIDTH,WINDOW_HEGIHT = 1000,800
WINDOW_TITLE = "Snake Game"

# GAME SPECIFIC VARIABLE 
EXIT_GAME,QUIT_GAME = False,False

GAMEWINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEGIHT))
pygame.display.set_caption(WINDOW_TITLE)


def main():
    global EXIT_GAME
    # GAME LOOP
    while not EXIT_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: EXIT_GAME = True
    else:
        pygame.quit()
        quit()       
if __name__ == "__main__":
    main()