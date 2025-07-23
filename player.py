from tile import Tile
from game_manager import GameManager

class Player:

    def __init__(self, base_pos):
        self.selection: Tile = None 
        self.base_pos = base_pos
        self.towers = []

    def change_selection(self, entity: Tile):
        if self.selection and self.selection != entity:
            self.selection.toggle_selection()
        
        selected: bool = entity.toggle_selection()
        if selected:
            self.selection = entity
        else:
            self.selection = None
    
    def get_base_pos(self):
        return self.base_pos
