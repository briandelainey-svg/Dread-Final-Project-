
#Imports
import pygame

#Physcis entities
class Physics():
    #Setup
    def __init__(self, Game, etype, pos):
        self.Game = Game
        self.type = etype
        self.x = pos[0]
        self.y = pos[1]
        self.health = 5
        self.layer = self.Game.screen
        
    def entity(self):
        #check Enity type
        if self.type == 'Player':
            self.model = pygame.transform.scale(pygame.image.load("pyg_map_maker/asset_pack/Assets/Charecter_Sprite1.png"), (60, 80))
            self.model.set_colorkey((0, 0, 0))
            #player hitbox(don't touch)
            self.hitbox = pygame.draw.rect(self.Game.hitbox, (0, 0, 0), (self.x, self.y, 60, 80))
            self.hitbox
            #player model
            self.Game.screen.blit(self.model, (self.x, self.y))
            #health Bar
            if self.health >= 5:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 14, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 28, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 42, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 56, self.y - 10, 12, 10))
            elif self.health == 4:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 14, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 28, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 42, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 56, self.y - 10, 12, 10))
            elif self.health == 3:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 14, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 28, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 42, self.y - 10, 22, 10))
            elif self.health == 2:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x + 14, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 28, self.y - 10, 32, 10))
            elif self.health == 1:
                pygame.draw.rect(self.Game.screen, (0, 255, 0), (self.x, self.y - 10, 12, 10))
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x + 14, self.y - 10, 46, 10))
            else:
                pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x, self.y - 10, 60, 10))
                
            
        if self.type == 'Enemy':
            #enemy hitbox
            self.hitbox = pygame.draw.rect(self.Game.hitbox, (0, 0, 0), (self.x, self.y, 50, 80))
            self.hitbox
            #enemy model
            pygame.draw.rect(self.Game.screen, (255, 0, 0), (self.x, self.y, 50, 80))
            
    #gravity
    def gravity(self):
        if self.y < 550:
            self.y += 5
        if self.y > 550:
            self.y = 550
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, Game, pos):
        super.__init__()
        self.Game = Game
        self.facing = self.game.right
        if self.facing:
            self.x = pos[0] + 50
        else:
            self.x = pos[0]
        self.y = pos[1] + 40
        self.white = (255, 255, 255)
        
    def update(self):
        #hitbox
        pygame.draw.rect(self.Game.hitbox, (0, 0, 0), (self.x, self.y, 20, 10))
        #model
        pygame.draw.rect(self.Game.screen, self.white, (self.x, self.y, 20, 10))
        #movement
        if self.facing:
            self.x += 10
        else:
            self.x -= 10
    
            
if __name__ == '__main__':
    print('entities Is the Main')