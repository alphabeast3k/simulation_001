import pygame
from button import Button
from game_manager import GameState
from you_lose_toast import YouLoseToast


class ScreenManager:
    def __init__(self, screen, display_size, board, enemy_manager, player,
                 ui_draw_list,
                 handle_mouse_clicks_fn,
                 render_health_fn,
                 render_currency_fn):
        self.screen = screen
        self.display_width, self.display_height = display_size
        self.board = board
        self.enemy_manager = enemy_manager
        self.player = player
        self.ui_draw_list = ui_draw_list
        self.handle_mouse_clicks = handle_mouse_clicks_fn
        self.render_health = render_health_fn
        self.render_currency = render_currency_fn

        self.state = GameState.START
        self.game_started = False
        self.game_over = False
        self.you_lose_toast = YouLoseToast(screen)

        # Build menu buttons
        menu_btn_size = (240, 60)
        menu_btn_x = self.display_width // 2 - menu_btn_size[0] // 2
        menu_btn_y0 = self.display_height // 2 - 100
        self.menu_layout = {"btn_x": menu_btn_x, "btn_y0": menu_btn_y0, "btn_size": menu_btn_size}

        def on_play():
            self.state = GameState.PLAYING
            if not self.game_started:
                self.enemy_manager.spawn_enemies()
                self.game_started = True

        def on_settings():
            self.state = GameState.SETTINGS

        def on_exit():
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        self.menu_buttons = [
            Button("Play", (menu_btn_x, menu_btn_y0), menu_btn_size, on_play),
            Button("Settings", (menu_btn_x, menu_btn_y0 + 90), menu_btn_size, on_settings),
            Button("Exit", (menu_btn_x, menu_btn_y0 + 180), menu_btn_size, on_exit),
        ]

        # Settings buttons
        def on_back():
            self.state = GameState.START

        self.settings_buttons = [
            Button("Back", (menu_btn_x, menu_btn_y0 + 180), menu_btn_size, on_back)
        ]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = (event.pos[0], event.pos[1])
            if self.state == GameState.START:
                for b in self.menu_buttons:
                    b.is_clicked(mouse_pos)
            elif self.state == GameState.SETTINGS:
                for b in self.settings_buttons:
                    b.is_clicked(mouse_pos)
            elif self.state == GameState.PLAYING and not self.game_over:
                self.handle_mouse_clicks(event)

    def update_and_draw(self):
        if self.state == GameState.START:
            self._draw_menu()
            return
        if self.state == GameState.SETTINGS:
            self._draw_settings()
            return
        if self.state == GameState.PLAYING:
            self._draw_gameplay()

    def _hover_buttons(self, buttons):
        mouse_pos = pygame.mouse.get_pos()
        for b in buttons:
            if hasattr(b, "hover_loop"):
                b.hover_loop(mouse_pos)

    def _draw_menu(self):
        self.screen.fill((30, 30, 30))
        title_font = pygame.font.Font(None, 72)
        title = title_font.render("Tower Defense", True, (255, 255, 255))
        self.screen.blit(title, (self.display_width//2 - title.get_width()//2, self.menu_layout["btn_y0"] - 120))
        self._hover_buttons(self.menu_buttons)
        for b in self.menu_buttons:
            b.draw(self.screen)

    def _draw_settings(self):
        self.screen.fill((20, 20, 40))
        title_font = pygame.font.Font(None, 64)
        title = title_font.render("Settings (Coming Soon)", True, (255, 255, 255))
        self.screen.blit(title, (self.display_width//2 - title.get_width()//2, self.menu_layout["btn_y0"] - 120))
        self._hover_buttons(self.settings_buttons)
        for b in self.settings_buttons:
            b.draw(self.screen)

    def _draw_gameplay(self):
        # Background and board
        self.screen.fill("white")
        self.board.draw_board(self.screen)

        # Game over trigger
        if not self.game_over and self.player.health <= 0:
            self.game_over = True
            self.you_lose_toast.show()

        # Update game state if not game over
        if not self.game_over:
            self.enemy_manager.update_enemies(tile_size=self.board.tile_size, screen=self.screen)
            self.board.update_tiles(self.enemy_manager.enemies)

        # HUD and UI
        self.render_health()
        self.render_currency()
        self._hover_buttons(self.ui_draw_list)
        for drawable in self.ui_draw_list:
            drawable.draw(self.screen)

        # Toast overlay
        if self.game_over:
            self.you_lose_toast.update()
