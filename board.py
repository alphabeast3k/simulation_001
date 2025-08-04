import math
from tile import Tile
from tile import TileType
from player import Player

class Board: 
    def __init__(self, width, height, screen, spawn_point,  player: Player):
        max_square_width = math.floor((screen.get_width()/width))
        max_square_height = math.floor((screen.get_height() / height))

        self.width = width
        self.height = height

        self.tile_size = min(max_square_height, max_square_width)
        self.tiles = [] 
        self.spawn_point = spawn_point

        # find the number of squares on the board 
        # find the max size of the squares * number of squares that can fit on the board 
        # 1280 / 10 -> 128 * 128 pixels
        # 720 / 10 -> 72 * 72  pixels 
        # whichever is greater 
        # draw rects/tiles/sprites
        for row in range(width):
            new_row_list = []
            for column in range(height):
                tile = Tile(row * self.tile_size, column*self.tile_size, self.tile_size)
                if  (row, column) == spawn_point:
                    tile.update_type(TileType.spawn_point)
                elif (row, column) == player.get_base_pos():
                    tile.update_type(TileType.base)
                elif column == 5:
                    tile.update_type(TileType.path)
                else:
                    tile.update_type(TileType.grass)
                
                new_row_list.append(tile)
            
            self.tiles.append(new_row_list)
    

    def draw_board(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)
    
    def  on_resize():
        # in the future will want to recalculate tile_size and redraw tiles
        pass
    
    def get_tile_at_pos(self, pos):
        # thinking that if we do modulo pos_y withh tile_size and floor than we get the tile that is currently at a position
        index_x = math.floor(pos[0] / self.tile_size)
        index_y = math.floor(pos[1] / self.tile_size)


        if index_x < self.width and index_y < self.width:
            return self.tiles[index_x][index_y]
    
    def get_tile_at_index(self, index_tuple: tuple):
        return self.tiles[index_tuple[0]][index_tuple[1]]
    
    def update_tiles(self, enemies):
        for row in self.tiles:
            for tile in row:
                tile.update(enemies)

