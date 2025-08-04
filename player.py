from tile import Tile
from game_manager import GameManager
from data_card import DataCard

class Player:

    def __init__(self, base_pos):
        self.selection: Tile = None 
        self.bank = 0 #store the amount of ccurrency the player has accumulated
        self.base_pos = base_pos
        self.towers = []

    def change_selection(self, screen, entity: Tile):
        if self.selection and self.selection != entity:
            self.selection.toggle_selection(screen)
        
        selected : bool = entity.toggle_selection(screen)
        
        if selected:
            self.selection = entity
            return True
        else:
            self.selection = None
            return False
    
    def get_base_pos(self):
        return self.base_pos

    def update_bank(self, amount) -> bool:
        # checks if bank will be less then 0 if so return false/invalid operation 
        if self.bank + amount < 0:
            return False
        else:
            self.bank += amount
            return True
