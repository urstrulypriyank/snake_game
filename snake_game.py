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
EXIT_GAME,QUIT_GAME,GAME_OVER = False,False,False
score = 0




# METHOD TO SET BACKGROUD COLOR 
def set_backgroudColor(color):
    global GAMEWINDOW
    GAMEWINDOW.fill(color)
    pygame.display.update()

# GAME ENGINE LOGIC IMPLEMENTATION
def engine_logic():
    global EXIT_GAME,WHITE,score,GAME_OVER,highScore
    # GAME LOOP
    set_backgroudColor(WHITE)
    global GAMEWINDOW,BLACK,FPS,EXIT_GAME
    snake_x,snake_y,snake_size = 45,55,30
    ssize = 10
    velocity_x = velocity_y = 0
    foodx = random.randint(20, WINDOW_WIDTH/2)
    foody = random.randint(20, WINDOW_HEGIHT/2)
    clock = pygame.time.Clock()
    snake_list = []
    snake_len = 1
    with open("HighScore.txt","r") as f:
        highScore = f.read()
    while not EXIT_GAME:
        if GAME_OVER:
            with open("HighScore.txt","w") as f:
                f.write(str(highScore))
            GAMEWINDOW.fill(WHITE)
            text_screen("Game Over ! Press Enter To Continue", RED, WINDOW_WIDTH/4,WINDOW_HEGIHT/2 )
            for event in pygame.event.get():
                if event.type == pygame.QUIT: EXIT_GAME = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        score = 0
                        GAME_OVER = False
                        main()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: EXIT_GAME = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        engine_logic() 
            
                # KEY PRESS EVENT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y =0


                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0

                    if event.key == pygame.K_DOWN :
                        velocity_y = 10
                        velocity_x = 0

                    if event.key == pygame.K_UP:
                        print("UP")
                        velocity_y = -10
                        velocity_x = 0
                    
                
                    
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
                score+=10
                foodx = random.randint(20, WINDOW_WIDTH/2)
                foody = random.randint(20, WINDOW_HEGIHT/2)
                ssize+=10
                snake_len += 5  
                if score>int(highScore):
                    highScore = score    
            GAMEWINDOW.fill(WHITE)
            pygame.draw.rect(GAMEWINDOW, RED, [foodx,foody,snake_size,snake_size])
            # pygame.draw.rect(GAMEWINDOW, BLACK, [snake_x,snake_y,snake_sizex,snake_sizey])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_len:
                del snake_list[0]
            if head in snake_list[:-1]:
                GAME_OVER = True
            plot_snake(GAMEWINDOW,BLACK,snake_list,snake_size)
            text_screen("Score: "+str(score)+"Hight Score :"+str(highScore), RED, 5, 5)
        pygame.display.update()
        clock.tick(FPS) 
    else:
        pygame.quit()
        quit() 
   
def text_screen(text,color,x,y):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text,True,color)
    GAMEWINDOW.blit(screen_text, [x,y])    

def plot_snake(GAMEWINDOW,BLACK,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(GAMEWINDOW, BLACK, [x,y,snake_size,snake_size])
   




def main():
    global GAMEWINDOW
    GAMEWINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEGIHT))
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.update()
    engine_logic()




if __name__ == "__main__":
    main()