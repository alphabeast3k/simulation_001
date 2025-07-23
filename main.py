import pygame 
from tile import Tile
from board import Board
from player import Player
from game_manager import GameManager
from enemy_manager import EnemyManager


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
game_manager = GameManager()
enemy_manager = EnemyManager(spawn_points=[(0,5)], clock=clock)

board = Board(width=board_size[0], height=board_size[1], screen=screen, enemy_manager=enemy_manager, player=player)

def handle_mouse_clicks(event):
    if event.button == 1:
        tile : Tile = board.get_tile_at_pos(event.pos[0],event.pos[1])
        player.change_selection(tile)
        
screen.fill("white") 
board.draw_board(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_clicks(event)
        if event.type == pygame.QUIT:
            running = False
   
    # draw entities onto the screen
    board.draw_board(screen)
    screen.blit(enemy_manager.get_snake_sprite(clock), (32, 32))

    pygame.display.flip()
    clock.tick(60)  # Limit to 480 frames per second