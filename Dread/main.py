###############################
# Dread(A Roguelike)          #
# By: Brian Delainey(Brandor) #
# Started: 05/22/2026         #
# Finished:                   #
###############################

#imports
import pygame
import sys

#The Game
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 650))#1280, 650
        pygame.display.set_caption('Dread')
        self.clock = pygame.time.Clock()
        self.movex = [False, False]
        self.x = 50
        self.y = 50
        self.speed = 5
        
    def player(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, 50, 80))
    
    def refresh(self):
        pygame.display.update()
        self.clock.tick(60)
        self.screen.fill((0, 48, 9))
        self.player()
        
    def run(self):
        #Main Loop
        while True:
            if self.movex[1] > self.movex[0]:
                self.x += self.speed
            if self.movex[0] > self.movex[1]:
                self.x -= self.speed
            if self.y < 550:
                self.y += self.speed
            else:
                self.y = 550
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.y == 550:
                            self.y -= 300
                        
                    if event.key == pygame.K_LEFT:
                        self.movex[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movex[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movex[0] = False 
                    if event.key == pygame.K_RIGHT:
                        self.movex[1] = False 
                    
            self.refresh()



if __name__ == '__main__':
    Game().run()