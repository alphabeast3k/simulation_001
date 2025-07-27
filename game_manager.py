from enum import Enum

class GameState(Enum):
    # will probably control the screen currently being displayed
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    VICTORY = 5
    SETTINGS = 6

class GameManager:
    def __init__(self, tile_size):
        self.tile_size = tile_size
    
    def update_tile_size(self, tile_size):
        self.tile_size = tile_size