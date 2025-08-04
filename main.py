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
board = Board(width=board_size[0], height=board_size[1], screen=screen, spawn_point=(0,5), player=player)

enemy_manager = EnemyManager(board=board, player=player)
        
screen.fill("white") 

tile_size = board.tile_size

spawn_point = ((0 * tile_size) + math.floor(tile_size/2), (tile_size * 5) + math.floor(tile_size/2))


data_card_obj = DataCard((1090, 0), (150, 250))


build_button = Button("build", (1110, 200), (100, 40), player.build_tower)
spawn_button = Button("spawn", (1110, 300), (100, 40), enemy_manager.spawn_enemies)


#ui elements we always want drawn last so they appear on top
ui_draw_list = [data_card_obj, build_button, spawn_button]
# towers need to be drawn after the tiles and can also be used to check if they are being clicked
tower_draw_list = []

def render_health():
    font = pygame.font.Font(None, 36)
    health_text = font.render(f'Health: {player.health}', True, (0,0,0))
    screen.blit(health_text, (1110, 600))  

def render_currency():
    font = pygame.font.Font(None, 36)
    health_text = font.render(f'Money: {player.bank}', True, (0,0,0))
    screen.blit(health_text, (1110, 650))  

def before_gui(): #add here the things to do each frame before blitting gui elements
    screen.fill((250,)*3)

def handle_mouse_clicks(event):
    if event.button == 1:
        mouse_pos = (event.pos[0],event.pos[1])
        button_clicked = False

        for element in ui_draw_list:
            if element.clickable():
                if element.is_clicked(mouse_pos):
                    element.click()
        
        if not button_clicked:
            tile : Tile = board.get_tile_at_pos(mouse_pos)
            if not tile:
                return
            data_vis = player.change_selection(screen,tile)

            data_card_obj.set_visible(data_vis)

# actions we want to check on every frame
def enemy_loop():
    enemy_manager.update_enemies(tile_size=tile_size, screen=screen)

def tower_loop():
    board.update_tiles(enemy_manager.enemies)

def player_loop():
    render_health()
    render_currency()

enemy_manager.spawn_enemies()

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


    enemy_loop()
    tower_loop()
    player_loop()
    
    for drawable in ui_draw_list:
        drawable.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second


# next steps get the pathfinding for enemies working
# player select tile and build/remove tower
# menus for starting, ending and adjusting the game 