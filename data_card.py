import pygame

# Everything should be representable as a data card
# How do we make it extensible
# Takes in info and displays it but also want some action buttons
# Should be able to override a known function
# Or fast approach is build them all seperately 
# not a good idea if we need to add more or different functionality
# maybe leave as data_card intentionally blank just creates a card 
# have pages that get scaled to fit the card
# so we'll never have more than one thing selected so instead of recreating it each time why not set to invisible and make visible and pass the info needed instead

class DataCard:
    def __init__(self, pos, size, boarder=4):
        self.pos = pos
        self.size = size
        self.boarder = boarder
        self.visible = False

    def set_visible(self, val):
        self.visible = val

    def clickable(self):
        return False

    def draw(self, screen):
        if not self.visible:
            return 
        padding = self.boarder/2
        pygame.draw.rect(surface=screen, color="black", rect=(self.pos[0], self.pos[1], self.size[0], self.size[1]), border_radius=3)
        pygame.draw.rect(surface=screen, color="white", rect=(self.pos[0] + padding , self.pos[1] + padding, self.size[0] - self.boarder, self.size[1] - self.boarder), border_radius=3)
        