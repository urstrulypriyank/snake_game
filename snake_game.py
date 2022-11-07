import pygame
import random
pygame.init()


# CONSTANT VARIABLE
WINDOW_WIDTH,WINDOW_HEGIHT = 1000,800
WINDOW_TITLE = "Snake Game"
FPS = 30
# CONSTANT VARIABLES FOR COLORS
WHITE,BLACK,RED = (255,255,255),(0,0,0),(255,0,0)

# GAME SPECIFIC VARIABLE 
EXIT_GAME,QUIT_GAME = False,False
score = 0




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
    global EXIT_GAME,WHITE,score

    # GAME LOOP
    set_backgroudColor(WHITE)
    global GAMEWINDOW,BLACK,FPS,EXIT_GAME
    snake_x,snake_y,snake_size = 45,55,10
    ssize = 10
    snake_sizex = 10
    snake_sizey = 10
    velocity_x = velocity_y = 0
    foodx = random.randint(20, WINDOW_WIDTH/2)
    foody = random.randint(20, WINDOW_HEGIHT/2)
    clock = pygame.time.Clock()
    
    while not EXIT_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: EXIT_GAME = True
           
            # KEY PRESS EVENT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 10
                    velocity_y =0
                    snake_sizex = ssize
                    snake_sizey = 10


                   
                if event.key == pygame.K_LEFT:
                    velocity_x = -10
                    velocity_y = 0
                    snake_sizex = ssize
                    snake_sizey = 10
                if event.key == pygame.K_DOWN :
                    velocity_y = 10
                    velocity_x = 0
                    snake_sizey = ssize
                    snake_sizex = 10
                if event.key == pygame.K_UP:
                    print("UP")
                    velocity_y = -10
                    velocity_x = 0
                    snake_sizey = ssize
                    snake_sizex = 10
               
                
                print(snake_x,snake_y)
                pygame.display.update()
        if(snake_x <1):
            snake_x = WINDOW_WIDTH-5
        if(snake_x >WINDOW_WIDTH):
            snake_x = 5
        if(snake_y <5):
            snake_y = WINDOW_HEGIHT-5
        if(snake_y >WINDOW_HEGIHT-5):
            snake_y = 5
        snake_x += velocity_x
        snake_y += velocity_y  
        if abs(snake_x -foodx)<10 and abs(snake_y-foody)<10:
            score+=1
            foodx = random.randint(20, WINDOW_WIDTH/2)
            foody = random.randint(20, WINDOW_HEGIHT/2)
            ssize+=10
            print("Score",score)      
        GAMEWINDOW.fill(WHITE)
        pygame.draw.rect(GAMEWINDOW, BLACK, [snake_x,snake_y,snake_sizex,snake_sizey])
        pygame.draw.rect(GAMEWINDOW, RED, [foodx,foody,snake_size,snake_size])
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