import pygame
from pygame.sprite import Sprite
import os 
from pygame.time import Clock
import math 

enemy_sheet = pygame.image.load(os.path.join("assets", "spritesheet.png"))
# should manage the enemies and the locations
# different thing sto consider but necessary now
# ideally spawn an enemy not sure if that should be handled by the game board but this class should handle smooth motion for the enemy ensuring constant speed
class EnemyManager:
    def __init__(self, spawn_points: list[tuple], clock : Clock):
        # spawn points are indexed by row and column of the tile rather then screen position
        self.spawn_points = spawn_points
        self.enemies = {}
        
        #self.snake_img = pygame.image.load(os.path.join("assets","spritesheet.png")).subsurface((0,0,16,16))
        self.snake_frame_sprites = []
    
    def get_spawn_points(self):
        return self.spawn_points

    def spawn_enemies(self, screen: pygame.surface.Surface):
        for spawn_point in self.spawn_points:
            enemy = Enemy(EnemyType.normal, spawn_point)
            self.enemies[spawn_point] = enemy


class EnemyType:
    normal = 1
    fast =  2
    tank = 3

class EnemyDataKeys:
    sprites = "sprites"
    health = "health"
    speed = "speed"
    damage = "damage"

enemy_data = {
    EnemyType.normal : {
        EnemyDataKeys.sprites : [
            enemy_sheet.subsurface((0,0,16,16)),
            enemy_sheet.subsurface((16,0,16,16)),
            enemy_sheet.subsurface((32,0,16,16)),
            enemy_sheet.subsurface((48,0,16,16))
        ],
        EnemyDataKeys.health: 10,
        EnemyDataKeys.speed: 1, #speed of one means 1 tile every 3 seconds for now may update the definition later 
        EnemyDataKeys.damage: 1
    },
    EnemyType.fast: {
        EnemyDataKeys.sprites : [
            enemy_sheet.subsurface((0,0,16,16)),
            enemy_sheet.subsurface((16,0,16,16)),
            enemy_sheet.subsurface((32,0,16,16)),
            enemy_sheet.subsurface((48,0,16,16))
        ],
        EnemyDataKeys.health: 10,
        EnemyDataKeys.speed: 1,
        EnemyDataKeys.damage: 1
    },
    EnemyType.tank : {
        EnemyDataKeys.sprites : [
            enemy_sheet.subsurface((0,0,16,16)),
            enemy_sheet.subsurface((16,0,16,16)),
            enemy_sheet.subsurface((32,0,16,16)),
            enemy_sheet.subsurface((48,0,16,16))
        ],
        EnemyDataKeys.health: 10,
        EnemyDataKeys.speed: 1,
        EnemyDataKeys.damage: 1
    }
}

class Enemy(Sprite):
    def __init__(self, enemy_type, pos):
        Sprite.__init__(self)
        self.enemy_type = enemy_type

        self.animation_counter = 0
        self.frame_index = 0
        self.frames_per_sec = 4
        self.path = []

        self.pos = pos
        self.true_pos = pos

        print(self.pos)

    def move(self, tile_size: int):
        # if we want to move x tiles per second then
        # what is the destination and how many spaces do we need to move between each
        # if we want to move 1 tile per second then we need to move tile_size pixels every 180 frames
        pixel_per_second = tile_size / 180
        self.true_pos = (self.true_pos[0] + pixel_per_second, self.true_pos[1])

        self.pos = (math.floor(self.true_pos[0]), math.floor(self.true_pos[1]))
    
    def draw(self, screen: pygame.surface.Surface):
        # much cleaner animation and can control the speed much easier 
        # will like want to change this into a system that can be applied to all animatable entities

        self.animation_counter += 1

        if self.animation_counter >= 60/self.frames_per_sec:
            self.animation_counter = 0
            self.frame_index += 1

            if self.frame_index >= len(enemy_data[self.enemy_type][EnemyDataKeys.sprites]):
                self.frame_index = 0
        
        screen.blit(enemy_data[self.enemy_type][EnemyDataKeys.sprites][self.frame_index], self.pos)


# Correct way to do it maybe have a global tracker -> no that doesn't work if there are different animation speeds
# We need to use a sprite might be able to use the update method
# in the game manager set the animation speed globally 
# every time a new frame is generated check if enough has passed then get the new one
# what about the health bar and move ment we'll want a path


# for mouse inputs might want to draw a small invisible sprite circle and check where the mouse is 
# have a sprite for each selectable object and select that object depending on sprite layer 
# 
# may want a controller that tells every sprite when to next go sprite 
# global animation speed controller may be nice but would mean that we can't control the animations individually 
# big thing for the game in the future can be being able to speed up the game 2x 4x 10x 