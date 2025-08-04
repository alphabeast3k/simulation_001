from pygame.sprite import Sprite
import pygame
import os
import math

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
        self.pos = pos
        self.tower_type = tower_type
    

    def draw(self, screen):
        screen.blit(self.image, self.pos)
    
    def update(self, enemies):
        pass

    def attack(self,enemies):
        for enemy in enemies:
            if self.in_range(enemy.true_pos):
                pass

    def in_range(self, target_pos: tuple) -> bool:
        a_squared = (self.pos[0] - target_pos[0])**2
        b_squared = (self.pos[1] - target_pos[1])**2

        pythagorean_distance = math.sqrt(a_squared + b_squared)

        return pythagorean_distance <= tower_data[self.tower_type][TowerDataKeys.range]