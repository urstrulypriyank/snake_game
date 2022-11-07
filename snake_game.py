import pygame
pygame.init()


# CONSTANT VARIABLE
WINDOW_WIDTH,WINDOW_HEGIHT = 1000,800
WINDOW_TITLE = "Snake Game"
FPS = 30
# CONSTANT VARIABLES FOR COLORS
WHITE,BLACK,RED = (255,255,255),(0,0,0),(255,0,0)

# GAME SPECIFIC VARIABLE 
EXIT_GAME,QUIT_GAME = False,False




# METHOD TO SET BACKGROUD COLOR 
def set_backgroudColor(color):
    global GAMEWINDOW
    GAMEWINDOW.fill(color)
    pygame.display.update()

# GAME ENGINE LOGIC IMPLEMENTATION
def engine_logic(event):
    pass
   
    




def main():
    # IMPORTING SOME GLOABL VARIABLES
    global EXIT_GAME,WHITE

    # GAME LOOP
    set_backgroudColor(WHITE)
    global GAMEWINDOW,BLACK,FPS,EXIT_GAME
    snake_x,snake_y,snake_size = 45,55,10
    clock = pygame.time.Clock()
    
    while not EXIT_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: EXIT_GAME = True
            
            # KEY PRESS EVENT
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT:
                    snake_x = snake_x+10
                if event.key == pygame.K_LEFT:
                    snake_x = snake_x-10
                if event.key == pygame.K_DOWN:
                    snake_y = snake_y+10
                if event.key == pygame.K_UP:
                    snake_y = snake_y-10
                pygame.display.update()
                
        GAMEWINDOW.fill(WHITE)
        pygame.draw.rect(GAMEWINDOW, BLACK, [snake_x,snake_y,snake_size,snake_size])
        pygame.display.update()
        clock.tick(FPS) 
    else:
        pygame.quit()
        quit() 


if __name__ == "__main__":

    GAMEWINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEGIHT))
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.update()
    main()