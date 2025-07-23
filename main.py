import pygame 
from tile import Tile
from board import Board
from player import Player


# encapsulate the display dimensions and board size at some point
display_width = 1280
display_height = 720

board_size = (15,10) # 10x10 board
active_selection = []

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# allow specific events
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

running = True
board = Board(width=board_size[0], height=board_size[1], screen=screen)
# player will handle all the states related to player 
player = Player()

def handle_mouse_events():
    mouse_events = pygame.event.get(eventtype=pygame.MOUSEBUTTONDOWN)
    if mouse_events:
        tile : Tile = board.get_tile_at_pos(mouse_events[0].pos[0],mouse_events[0].pos[1])
        player.change_selection(tile)
        


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")  # Clear the screen with black
   
    # draw entities onto the screen
    board.draw_board(screen)

    # event handler or sytems
    handle_mouse_events()

    pygame.display.flip()
    # clock.tick(480)  # Limit to 480 frames per second