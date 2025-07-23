import pygame
import os 
from pygame.time import Clock
# should manage the enemies and the locations
# different thing sto consider but necessary now
# ideally spawn an enemy not sure if that should be handled by the game board but this class should handle smooth motion for the enemy ensuring constant speed
class EnemyManager:
    def __init__(self, spawn_points: list[tuple], clock : Clock):
        # spawn points are indexed by row and column of the tile rather then screen position
        self.spawn_points = spawn_points
        self.enemies = {}

        self.img_index = 0
        self.animation_counter = 0

        snake_frames = {0: (0,0,16,16),
                        1: (16,0,16,16),
                        2: (32,0,16,16),
                        3: (48,0,16,16)}
        
        #self.snake_img = pygame.image.load(os.path.join("assets","spritesheet.png")).subsurface((0,0,16,16))
        self.snake_frame_sprites = []

        for index in snake_frames.keys():
            self.snake_frame_sprites.append(pygame.image.load(os.path.join("assets","spritesheet.png")).subsurface(snake_frames[index]))
    
    def get_spawn_points(self):
        return self.spawn_points

    def spawn_enemies(self, screen):
        pass

    def get_snake_sprite(self, clock: Clock):
        self.animation_counter += 1
        if self.animation_counter == 15:
            self.animation_counter = 0
            self.img_index += 1
            if self.img_index == 4:
                self.img_index = 0
        
        return self.snake_frame_sprites[self.img_index]


class Enemy: 
    def __init__(self):
        pass


# Correct way to do it maybe have a global tracker -> no that doesn't work if there are different animation speeds
# We need to use a sprite might be able to use the update method
# in the game manager set the animation speed globally 
# every time a new frame is generated check if enough has passed then get the new one
# what about the health bar and move ment we'll want a path


# for mouse inputs might want to draw a small invisible sprite circle and check where the mouse is 
# have a sprite for each selectable object and select that object depending on sprite layer  