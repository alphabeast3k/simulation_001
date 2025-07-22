import enum
import pygame

class TileType:
    blank=0
    grass=1
    path=2

class TileTypeMapKeys:
    color="color"
    buildable="buildable"

tile_type_map = {
    TileType.blank : {
        TileTypeMapKeys.color : "white",
        TileTypeMapKeys.buildable: False
    },
    TileType.grass : {
        TileTypeMapKeys.color: "green",
        TileTypeMapKeys.buildable: True
    },
    TileType.path  : {
        TileTypeMapKeys.color: "brown",
        TileTypeMapKeys.buildable: False
    }
}

class Tile():

    def __init__(self, x_pos, y_pos, size):
        self.x_pos=x_pos
        self.y_pos=y_pos

        self.tile_type=TileType.blank
        self.size = size
        self.selected = False

    def update_type(self, tile_type):
        self.tile_type = tile_type

    def get_color(self) -> str:
        return tile_type_map[self.tile_type][TileTypeMapKeys.color]

    def toggle_selection(self):
        self.selected = not self.selected

    def draw(self, screen):
        if self.selected:
            pygame.draw.rect(surface=screen, color="red", rect=(self.x_pos, self.y_pos, self.size, self.size),border_radius=3) 
        else:
            pygame.draw.rect(surface=screen, color=self.get_color(), rect=(self.x_pos, self.y_pos, self.size, self.size),border_radius=3) 

        