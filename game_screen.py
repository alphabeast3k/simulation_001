
import pygame
from you_lose_toast import YouLoseToast


class GameScreen:
    def __init__(self, board, enemy_manager, player, screen):
        self.board = board
        self.enemy_manager = enemy_manager
        self.player = player
        self.screen = screen
        self.you_lose_toast = YouLoseToast(screen)
        self.lost = False

    def on_start(self):
        pass

    def update(self, screen):
        self.board.update_tiles(self.enemy_manager.enemies)
        self.enemy_manager.update_enemies(tile_size=self.board.tile_size, screen=screen)

    def draw(self, screen):
        self.board.draw_board(screen)
        self.enemy_manager.draw_enemies(screen)
    
    def game_loop(self, screen):
        # Example: call this in your main loop
        if not self.lost and self.player.health <= 0:
            self.lost = True
            self.you_lose_toast.show()
        if self.lost:
            # Show toast, block game updates
            if not self.you_lose_toast.update():
                # Toast finished, you can add logic to reset or quit
                pass
            return
        # ...existing game update/draw logic...