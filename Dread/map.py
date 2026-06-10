
#imports
import pygame
import random

class Floor():
    def __init__(self, Game):
        self.map = random.randint(1, 3)
        self.game = Game
        self.tiles = []
        
    def spawn(self):
        if self.map == 1:
        elif self.map == 2:
        elif self.map == 3:
        
        if self.game.player.hitbox.colliderect(self.tiles):
            