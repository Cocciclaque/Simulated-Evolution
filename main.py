import pygame
import datastructures
import gamemanager
import random



def mainloop():
    running = True
    stepcounter = 0
    move = 0
    while running:
        screen.fill(bgcolor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move = 0
                if event.key == pygame.K_DOWN:
                    move = 1
                if event.key == pygame.K_RIGHT:
                    move = 2
        
        Manager.move()

        if move == 0:
            for i in range(random.randint(0, 5)):
                Manager.spawnFood()
                Manager.spawnFood()

        if move == 1:
            Manager.spawnFood()
            Manager.spawnFoodLine()


        if move == 2:
            for i in range(random.randint(0, 3)):
                Manager.spawnFoodSparse()
            for i in range(7):
                Manager.spawnFoodEden()

        Manager.draw(screen)
        Manager.check_for_reproduces()
        
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()

    ###################################
    #             Params              #
    ###################################

    bgcolor:tuple = (80, 80, 80, 255)
    screen_size:datastructures.Vector2 = datastructures.Vector2(800, 800)
    screen:pygame.display = pygame.display.set_mode((screen_size.x, screen_size.y))
    
    tilesize:int = 2
    start_population:int = 20

    clock = pygame.time.Clock()
    Manager = gamemanager.GameManager(screen_size.x, screen_size.y, tilesize)

    fps:int = 144

    baseAmountFoods = 100
    baseAmountBacts = 100
    
    Manager.generateBacteria(baseAmountBacts)
    Manager.generateFood(baseAmountFoods)

    mainloop()





