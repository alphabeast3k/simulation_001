from pygame.sprite import Sprite
import pygame
import os 

class TowerType:
    short_range =  1
    medium_range =  2
    long_range = 3

class TowerDataKeys:
    sprite =  "sprite" # we want to load all the sprites in the beginning and reference the same img
    range = "range"
    damage = "damage"
    cost = "cost"

tower_data = {
    TowerType.short_range: {
        TowerDataKeys.sprite : pygame.image.load(os.path.join("assets", "spritesheet.png")).subsurface((0,208, 16,16)),
        TowerDataKeys.range : 2,
        TowerDataKeys.damage: 1,
        TowerDataKeys.cost: 1
    },
    TowerType.medium_range: {
        TowerDataKeys.sprite : pygame.image.load(os.path.join("assets", "spritesheet.png")).subsurface((128,208, 16,16)),
        TowerDataKeys.range : 4,
        TowerDataKeys.damage: 1,
        TowerDataKeys.cost: 1
    },
    TowerType.long_range: {
        TowerDataKeys.sprite : pygame.image.load(os.path.join("assets", "spritesheet.png")).subsurface((0,208, 16,16)),
        TowerDataKeys.range : 6,
        TowerDataKeys.damage: 1,
        TowerDataKeys.cost: 1
    },
}

class Tower(pygame.sprite.Sprite):
    def __init__(self, tower_type: int, pos: tuple):
        Sprite.__init__(self)
        self.image = tower_data[tower_type][TowerDataKeys.sprite]
        # self.rect = self.image.get_rect()
        # self.rect.x = pos[0]
        # self.rect.y = pos[1]
        self.pos = pos
    

    def draw(self, screen):
        screen.blit(self.image, self.pos)