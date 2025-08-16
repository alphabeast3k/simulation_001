import pygame 
from tile import Tile
from board import Board
from player import Player
from enemy_manager import EnemyManager
from you_lose_toast import YouLoseToast
from screen_manager import ScreenManager
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

tp.init(screen=screen, theme=tp.theme_human) 
running = True

# player will handle all the states related to player 
player = Player(base_pos=(14,5))
board = Board(width=board_size[0], height=board_size[1], screen=screen, spawn_point=(0,5), player=player)

enemy_manager = EnemyManager(board=board, player=player)
        
screen.fill("white") 

tile_size = board.tile_size


data_card_obj = DataCard((1090, 0), (150, 250))


build_button = Button("build", (1110, 200), (100, 40), player.build_tower)
spawn_button = Button("spawn", (1110, 300), (100, 40), enemy_manager.spawn_enemies)


#ui elements we always want drawn last so they appear on top
ui_draw_list = [data_card_obj, build_button, spawn_button]
# towers need to be drawn after the tiles and can also be used to check if they are being clicked
tower_draw_list = []

you_lose_toast: YouLoseToast = YouLoseToast(screen)

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

screen_manager = ScreenManager(
    screen=screen,
    display_size=(display_width, display_height),
    board=board,
    enemy_manager=enemy_manager,
    player=player,
    ui_draw_list=ui_draw_list,
    handle_mouse_clicks_fn=handle_mouse_clicks,
    render_health_fn=render_health,
    render_currency_fn=render_currency,
)

while running:
    events = pygame.event.get()
    mouse_rel = pygame.mouse.get_rel()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        screen_manager.handle_event(event)

    screen_manager.update_and_draw()

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second


# next steps get the pathfinding for enemies working
# player select tile and build/remove tower
# menus for starting, ending and adjusting the game 
# game loop idea:
# deckbuilder roguelike tower defense
# - Start with a basic deck of towers
# - Each wave of enemies gives rewards to upgrade or add to the deck
# - Players can build towers on the board using their deck
# - Implement a shop system to buy/sell cards between waves
# - Unlock new tower types as the player progresses
# - Have action cards that can be played for special effects