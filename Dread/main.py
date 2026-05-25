###############################
#Dread(A Roguelike)           #
#By: Brian Delainey(Brandor)  #
#Started: 05/22/2026          #
#Finished:                    #
###############################

#imports
import pygame
import sys

#The Game
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 650))#1275, 650
        pygame.display.set_caption('Dread')
        self.clock = pygame.time.Clock()
        
    def player(self):
        self.pygame.draw.rect(self.screen, (255, 0, 0), (80, 80, 50, 80))
    
    def refresh(self):
        pygame.display.update()
        self.clock.tick(60)
        self.screen.fill((0, 48, 9))
        
    def run(self):
        #Main Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.KEYDOWN:
                    pass
                if event.type == pygame.KEYUP:
                    pass
            self.refresh()



if __name__ == '__main__':
    Game().run()