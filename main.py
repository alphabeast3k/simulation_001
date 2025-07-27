import pygame 
from tile import Tile
from board import Board
from player import Player
from game_manager import GameManager
from enemy_manager import EnemyManager, Enemy, EnemyType
from tower import TowerType, Tower
from button import Button
import math


# encapsulate the display dimensions and board size at some point
display_width = 1280
display_height = 720

board_size = (15,10) # 10x10 board
active_selection = []

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# allow specific events
# pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

running = True

# player will handle all the states related to player 
player = Player(base_pos=(14,5))
enemy_manager = EnemyManager(spawn_points=[(0,5)], clock=clock)

board = Board(width=board_size[0], height=board_size[1], screen=screen, enemy_manager=enemy_manager, player=player)

def handle_mouse_clicks(event):
    if event.button == 1:
        button_clicked = False
        for button in buttons:
            if button.is_clicked(event.pos):
                button_clicked = True
                break
        
        if not button_clicked:
            tile : Tile = board.get_tile_at_pos(event.pos[0],event.pos[1])
            player.change_selection(tile)
        
screen.fill("white") 
board.draw_board(screen)

button = Button("Start Game", (100, 50), (150, 50))

buttons = [button]

tower = Tower(TowerType.medium_range, (160,160))
tile_size = board.tile_size

spawn_point = ((0 * tile_size) + math.floor(tile_size/2), (tile_size * 5) + math.floor(tile_size/2))
print(spawn_point)
enemy = Enemy(EnemyType.normal, spawn_point)



while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_clicks(event)
        if event.type == pygame.QUIT:
            running = False

    for _button in buttons:
        _button.hover_loop(pygame.mouse.get_pos())
   
    # draw entities onto the screen
    board.draw_board(screen)

    button.draw(screen)

    screen.blit(tower.image, (120,120))
    enemy.draw(screen)
    enemy.move(board.tile_size)
    

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second


# next steps get the pathfinding for enemies working
# player select tile and build/remove tower
# menus for starting, ending and adjusting the game 
#
#