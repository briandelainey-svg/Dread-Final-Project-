import pygame

class Physics():
    def __init__(self, Game, etype, pos):
        self.Game = Game
        self.type = etype
        self.x = pos[0]
        self.y = pos[1]
        self.health = 5
    def entity(self):
        if self.type == 'Player':
            self.hitbox = pygame.draw.rect(self.Game.hitbox, (0, 0, 0), (self.x, self.y, 50, 80))
            self.hitbox
            pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y, 50, 80))
            if self.health >= 5:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 10, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 20, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 30, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 40, self.y - 20, 9, 10))
            elif self.health == 4:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 10, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 20, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 30, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 40, self.y - 20, 9, 10))
            elif self.health == 3:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 10, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 20, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 30, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 40, self.y - 20, 9, 10))
            elif self.health == 2:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 10, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 20, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 30, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 40, self.y - 20, 9, 10))
            elif self.health == 1:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 10, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 20, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 30, self.y - 20, 9, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 40, self.y - 20, 9, 10))
            else:
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x, self.y - 20, 50, 10))
                

        if self.type == 'Enemy':
            self.hitbox = pygame.draw.rect(self.Game.hitbox, (0, 0, 0), (self.x, self.y, 50, 80))
            self.hitbox
            pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x, self.y, 50, 80))
            
    def gravity(self):
        if self.y < 550:
            self.y += 5
        if self.y > 550:
            self.y = 550
            
if __name__ == '__main__':
    print('entities Is the Main')