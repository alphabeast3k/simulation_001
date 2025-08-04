import pygame 
from tile import Tile
from board import Board
from player import Player
from enemy_manager import EnemyManager, Enemy, EnemyType
from tower import TowerType, Tower
from button import Button
from data_card import DataCard
import thorpy as tp 
import math


# encapsulate the display dimensions and board size at some point
display_width = 1280
display_height = 720

board_size = (15,10) # 10x10 board
active_selection = []

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# ui stuff maybe
tp.init(screen=screen, theme=tp.theme_human) 

# allow specific events
# pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

running = True

# player will handle all the states related to player 
player = Player(base_pos=(14,5))
enemy_manager = EnemyManager(spawn_points=[(0,5)], clock=clock)

board = Board(width=board_size[0], height=board_size[1], screen=screen, enemy_manager=enemy_manager, player=player)
        
screen.fill("white") 

# tp button
my_button = tp.Button("Hello, world.\nThis button uses the default theme.")
my_ui_elements = tp.Group([my_button])
updater = my_ui_elements.get_updater() 

tower = Tower(TowerType.medium_range, (160,160))
tile_size = board.tile_size

spawn_point = ((0 * tile_size) + math.floor(tile_size/2), (tile_size * 5) + math.floor(tile_size/2))
enemy = Enemy(EnemyType.normal, spawn_point)

data_card_obj = DataCard((1090, 0), (150, 250))

#ui elements we always want drawn last so they appear on top
ui_draw_list = [data_card_obj]
# towers need to be drawn after the tiles and can also be used to check if they are being clicked
tower_draw_list = []

def before_gui(): #add here the things to do each frame before blitting gui elements
    screen.fill((250,)*3)

def handle_mouse_clicks(event):
    if event.button == 1:
        button_clicked = False
        
        if not button_clicked:
            tile : Tile = board.get_tile_at_pos(event.pos[0],event.pos[1])
            if not tile:
                return
            data_vis = player.change_selection(screen,tile)

            data_card_obj.set_visible(data_vis)



while running:
    events = pygame.event.get()
    mouse_rel = pygame.mouse.get_rel()

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_clicks(event)
        if event.type == pygame.QUIT:
            running = False
   
    # effectively clear the screen 
    screen.fill("white") 
    # draw entities onto the screen
    board.draw_board(screen)

    screen.blit(tower.image, (120,120))
    enemy.draw(screen)
    enemy.move(board.tile_size)

    for drawable in ui_draw_list:
        drawable.draw(screen)
    

    updater.update(events=events,
                   mouse_rel=mouse_rel)
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second


# next steps get the pathfinding for enemies working
# player select tile and build/remove tower
# menus for starting, ending and adjusting the game 