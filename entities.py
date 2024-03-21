import pygame
from alias import alias
import random
import math

class Bacteria:

    costs_alias = [0, 1, 2, 4, 8, 4, 2, 1]
    max_gene = 1

    def __init__(self, x:int, y:int, parent):
        self.x = x
        self.y = y 

        self.dir = random.randint(0, 7)

        self.genome = [0]*8 
        self.generate_genome()


        self.energylostperstep = 4
        self.energy = 1000

        self.color = (100, 100, 255, 255)

        self.size = 10
        self.generate_genome()

        if parent:
            self.energy = parent.energy/2
            self.genome = parent.genome
            self.genome = self.mutate_gene()
        

    
    def generate_genome(self):
        for i in range(len(self.genome)):
            self.genome[i] = random.random()

    def choose_direction(self):
        _sum = sum(self.genome)

        rand_num = random.randint(0, math.floor(_sum))+random.random()
        chosen_dir = 0
        
        for i in range(len(self.genome)):
            if self.genome[i] <= rand_num:
                rand_num -= self.genome[i]
            else:
                chosen_dir = i
                break

        self.energy -= Bacteria.costs_alias[chosen_dir]
        self.dir = (self.dir + chosen_dir)%8
        

    def mutate_gene(self):

        new_genes = self.genome.copy()

        n = random.randint(0, 7)
        new_genes[n] += (random.random()-0.5)*10
        if new_genes[n] < 0: new_genes[n]=0

        saved = new_genes[n]
        
        if new_genes[n]>1:
            new_genes[n] = 1

        return new_genes

    def draw(self, screen, tilesize):
        pygame.draw.rect(screen, self.color, (self.x * tilesize, self.y * tilesize, self.size, self.size))

    def move(self, maxX, maxY):
        self.choose_direction()
        self.energy -= self.energylostperstep
        self.x += alias()[self.dir][0]
        self.y += alias()[self.dir][1]

        if self.x < 0:
            self.x = maxX-2
        elif self.x > maxX:
            self.x = 0

        if self.y < 0:
            self.y = maxY-2
        elif self.y > maxY:
            self.y = 0



# class Food:

#     def __init__(self, x:int, y:int):
#         self.x = x
#         self.y = y

#         self.energy_value = 100


#         self.color = (100, 255, 100, 255)


    
#     def draw(self, screen, tilesize):
#         pass