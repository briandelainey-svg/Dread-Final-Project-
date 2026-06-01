###############################
# Dread(A Roguelike)          #
# By: Brian Delainey(Brandor) #
# Started: 05/22/2026         #
# Finished:                   #
###############################

#imports
import pygame
import sys
from entities import Physics

#The Game
class Game:
    def __init__(self):
        pygame.init()
        self.hitbox = pygame.display.set_mode((1280, 650))
        self.screen = pygame.display.set_mode((1280, 650))#1280, 650
        pygame.display.set_caption('Dread')
        self.clock = pygame.time.Clock()
        self.movex = [False, False]
        self.x = 50
        self.y = 50
        self.speed = 4
        self.player = Physics(self, 'Player', [self.x, self.y])
        self.enemy = Physics(self, 'Enemy', [1180, 50])
        self.player.entity()
        self.health = self.player.health
        self.enemy.entity()
    

        
    def refresh(self):
        pygame.display.update()
        self.clock.tick(60)
        self.hitbox
        self.screen.fill((0, 48, 9))
        self.player.entity()
        self.enemy.entity()
        
    def run(self):
        #Main Loop
        while True:
            if  self.player.hitbox.colliderect(self.enemy.hitbox):
                self.player.health -= 1
            if self.player.x > self.enemy.x:
                self.enemy.x += self.speed -2
            elif self.player.x < self.enemy.x:
                self.enemy.x -= self.speed -2
            
            #movement
            if self.movex[1] > self.movex[0]:
                self.player.x += self.speed
            if self.movex[0] > self.movex[1]:
                self.player.x -= self.speed
            #falling
            self.player.gravity()
            self.enemy.gravity()
            #events
            for event in pygame.event.get():
                #'x' button clicked
                if event.type == pygame.QUIT or self.player.health <= 0:
                    pygame.quit()
                    print('Game Over')
                    sys.exit
                #key pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.player.y == 550:
                            self.player.y = 300
                        
                    if event.key == pygame.K_LEFT:
                        self.movex[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movex[1] = True
                        
                #key released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movex[0] = False 
                    if event.key == pygame.K_RIGHT:
                        self.movex[1] = False 
            
            #refresh screen
            self.refresh()

        



if __name__ == '__main__':
    Game().run()