from tile import Tile
from tower import TowerType

class Player:

    def __init__(self, base_pos):
        self.selection: Tile = None
        self.starting_currency = 10
        self.bank = 0 + self.starting_currency #store the amount of ccurrency the player has accumulated
        self.base_pos = base_pos
        self.health = 10

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

    def build_tower(self):
        if self.selection:
            self.selection.build_tower()
