import pygame 
import math
from tile import Tile
from tile import TileType
from board import Board


# encapsulate the display dimensions and board size at some point
display_width = 1280
display_height = 720

board_size = (15,10) # 10x10 board

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

running = True
board = Board(width=board_size[0], height=board_size[1], screen=screen)

def handle_mouse_events():
    mouse_press = pygame.mouse.get_pressed()
    if (mouse_press[0]):
        print("left pressed")
        board.get_tile_at_pos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    elif (mouse_press[1]):
        print("middle pressed")
    elif (mouse_press[2]):
        print("right pressed")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")  # Clear the screen with black
    board.draw_board(screen)
    handle_mouse_events()
    pygame.display.flip()

    clock.tick(60)  # Limit to 60 frames per second