import math
import random
import entities
import datastructures
import pygame

class GameManager:

    num_lines_ver = 6
    num_lines_hor = 5
    energy_value = 40

    def __init__(self, sizeX:int, sizeY:int, tilesize:int):
        """
        Default GameManager
        """
        self.sx = sizeX
        self.sy = sizeY
        self.z = tilesize
        
        self.dt = 0
        
        self.bact = []
        self.bact_positions = []
        self.food = []

    def update_clock(self, dt):
        self.dt += dt

    def draw_food(self, screen, x, y):
        pygame.draw.rect(screen, (100, 255, 100, 255), (x * self.z, y * self.z, self.z, self.z))

    def draw(self, screen):
        for x in range(len(self.food)):
            for y in range(len(self.food[0])):
                if self.food[x][y] == 1: self.draw_food(screen, x, y)
        
        for bacteria in self.bact:
            bacteria.draw(screen, self.z)

    def check_for_reproduces(self):
        for bacteria in self.bact:
            if bacteria.energy > 1000:
                self.bact.append(entities.Bacteria(bacteria.x, bacteria.y, bacteria))
                bacteria.energy = bacteria.energy/2

    def addFood(self, foods:list[int]):
        self.food += foods

    def addBacteria(self, bacts:list[entities.Bacteria]):
        self.bact += bacts

    def generateFood(self, amount:int):
        foodscoords = []

        tx = int(round((self.sx-self.z)/self.z))
        ty = int(round((self.sy-self.z)/self.z))
        return_coords = []

        for x in range(tx):
            foodscoords = []
            for y in range(ty):
                if random.random() >= 0.7:
                    foodscoords += [1]
                else:
                    foodscoords += [None] 
            return_coords.append(foodscoords)

        self.addFood(return_coords)

    def generateBacteria(self, amount:int):
        bactToAdd = []
        bactcoords = []
        for i in range(amount):    
            coords = (random.randint(0, int(round((self.sx-self.z)/self.z))), random.randint(0, int(round((self.sy-self.z)/self.z))))
            bactToAdd.append(coords)
        
        for i in range(amount):
            bactcoords.append(entities.Bacteria(bactToAdd[i][0], bactToAdd[i][1], None))
    
        

        self.addBacteria(bactcoords)
        self.SetbactPosition(bactToAdd)
    

    def SetbactPosition(self, positions):
        self.bact_positions = positions

    def move(self):

        for i, bacteria in enumerate(self.bact):
            bacteria.move((self.sx-self.z)/self.z, (self.sy-self.z)/self.z)
            if bacteria.energy < 1500: self.checkForFood()

            if bacteria.energy <= 0: self.bact.pop(i)

    
    def checkForFood(self):
        
        for bacteria in self.bact:
            istilefood = self.isTileFood(bacteria.x, bacteria.y)
            if istilefood[0]:
                bacteria.energy += istilefood[1]
                self.food[int(bacteria.x-1)][int(bacteria.y-1)] = None

    
    def isTileFood(self, x, y):
        x = int(x-1)
        y = int(y-1)
        if self.food[x][y] == 1:
            if self.food[x][y] == 1:
                return (True, GameManager.energy_value)
        return (False, None)
    



    def spawnFood(self):
        x = 0
        y = 0
        while self.food[x][y] == 1:
            x = random.randint(0, len(self.food)-1)
            y = random.randint(0, len(self.food[0])-1)
        self.food[x][y] = 1

    
    def spawnFoodLine(self):
        for x in range(GameManager.num_lines_ver):
            xpos = math.ceil((len(self.food)-1)/GameManager.num_lines_ver*x)
            ypos = random.randint(0, len(self.food[0])-1)
            self.food[xpos][ypos] = 1

        for y in range(GameManager.num_lines_hor):
            ypos = math.ceil((len(self.food[0])-1)/GameManager.num_lines_hor*y)
            xpos = random.randint(0, len(self.food[0])-1)
            self.food[xpos][ypos] = 1

    def spawnFoodEden(self):

        tx = len(self.food)-1
        ty = len(self.food[0])-1

        x = random.randint(int(round(tx/2-(tx/16))),int(round(tx/2+(tx/16))))
        y = random.randint(int(round(ty/2-(ty/16))),int(round(ty/2+(ty/16))))

        max = 100
        counter = 0

        while self.food[x][y] == 1 and counter < max:
            counter += 1
            x = random.randint(int(round(tx/2-(tx/16))),int(round(tx/2+(tx/16))))
            y = random.randint(int(round(ty/2-(ty/16))),int(round(ty/2+(ty/16))))
        self.food[x][y] = 1


    def spawnFoodSparse(self):
        tx = len(self.food)-1
        ty = len(self.food[0])-1

        x = random.randint(0, tx)
        y = random.randint(0, ty)

        while self.food[x][y] == 1 or ((x > tx/4 and x < (tx/4*3)) and (y > ty/4 and y < (ty/4*3))):
            x = random.randint(0, tx)
            y = random.randint(0, ty)
        self.food[x][y] = 1

                

