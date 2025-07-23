from tile import Tile
from game_manager import GameManager

class Player:

    def __init__(self):
        self.selection: Tile = None 

    def change_selection(self, entity: Tile):
        if self.selection and self.selection != entity:
            self.selection.toggle_selection()
        
        selected: bool = entity.toggle_selection()
        if selected:
            self.selection = entity
        else:
            self.selection = None
