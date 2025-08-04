import pygame
import os
import math
from enum import Enum
from tower import Tower, TowerType
from pygame.event import Event, EventType


class TileType(Enum):
    blank       = 0
    grass       = 1
    path        = 2
    spawn_point = 3
    base        = 4
    water       = 5

#in the future will want to addd more variations for if the tile is next to another
# for example if the tile is next to a path tile then it will have a different sprite
class TileTypeMapKeys:
    color="color"
    buildable="buildable"
    img="sprite_img"

tile_type_map = {
    TileType.blank : {
        TileTypeMapKeys.color : "white",
        TileTypeMapKeys.buildable: False,
        TileTypeMapKeys.img: None
    },
    TileType.grass : {
        TileTypeMapKeys.color: "green",
        TileTypeMapKeys.buildable: True,
        TileTypeMapKeys.img: pygame.image.load(os.path.join("assets", "tiles", "Grass_Middle.png"))
    },
    TileType.path  : {
        TileTypeMapKeys.color: "brown",
        TileTypeMapKeys.buildable: False,
        TileTypeMapKeys.img: pygame.image.load(os.path.join("assets", "tiles", "Path_Middle.png"))
    },
    TileType.spawn_point  : {
        TileTypeMapKeys.color: "gray",
        TileTypeMapKeys.buildable: False,
        TileTypeMapKeys.img: pygame.image.load(os.path.join("assets", "tiles", "FarmLand_Tile.png"))
    },
    TileType.base : {
        TileTypeMapKeys.color: "purple",
        TileTypeMapKeys.buildable: False,
        TileTypeMapKeys.img: pygame.image.load(os.path.join("assets", "tiles", "FarmLand_Tile.png"))
    }

}

class Tile:
    def __init__(self, x_pos, y_pos, size):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.selected = False

        self.tile_type=TileType.blank
        self.size = size
        self.image = tile_type_map[self.tile_type][TileTypeMapKeys.img]

        self.tower = None

    def update_type(self, tile_type):
        self.tile_type = tile_type
        self.image = tile_type_map[self.tile_type][TileTypeMapKeys.img]
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def get_color(self) -> str:
        return tile_type_map[self.tile_type][TileTypeMapKeys.color]
    
    def toggle_selection(self, screen) -> bool:
        self.selected = not self.selected
        return self.selected

    def draw(self, screen):
        if self.selected:
            pygame.draw.rect(surface=screen, color="red", rect=(self.x_pos, self.y_pos, self.size, self.size),border_radius=3)
        else:
            if self.image:
                # draw the image on the screen
                screen.blit(self.image, (self.x_pos, self.y_pos))
            else:
                print(self.image)
                # draw a rectangle with the color of the tile
                pygame.draw.rect(surface=screen, color=self.get_color(), rect=(self.x_pos, self.y_pos, self.size, self.size),border_radius=3)
        
        if self.tower:
            self.draw_tower(screen)
        
    
    def draw_tower(self, screen):
        self.tower.draw(screen)
    
    def build_tower(self):
        self.tower =  Tower(TowerType.medium_range, (self.x_pos + (self.size/2), self.y_pos + (self.size/2)))
        
        # here as an example event if needed
        # event = Event(pygame.event.custom_type, {"drawable": obj_tower})
        # pygame.event.post(obj_tower)               
        pass

    def get_center(self):
        return (math.floor((self.x_pos + (self.size/2))),math.floor(self.y_pos + (self.size/2)))

    def update(self, enemies):
        if self.tower:
            self.tower.update(enemies, self.size)

