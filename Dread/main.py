import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1275, 650))
        self.display = pygame.Surface((320 , 240))
        pygame.display.set_caption('Dread')
        self.clock = pygame.time.Clock()
        
    def run(self):
        pass

if __name__ == '__main__':
    Game().run()