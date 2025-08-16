import thorpy
import pygame

class YouLoseToast:
    def __init__(self, screen, message="You Lose!", duration=2.0):
        self.screen = screen
        self.message = message
        self.duration = duration  # seconds
        self.toast = None
        self.start_time = None

    def show(self):
        self.toast = thorpy.Text(text=self.message, font_size=40, font_color=(255,0,0))
        box = thorpy.Box([self.toast])
        x = self.screen.get_width()//2 - box.get_rect().size[0]//2
        y = self.screen.get_height()//2 - box.get_rect().size[1]//2
        box.set_topleft(x, y)
        self.box = box
        self.start_time = pygame.time.get_ticks()
        self.box.draw()

    def update(self):
        if self.start_time is None:
            return False
        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000.0
        if elapsed > self.duration:
            return False
        self.box.draw()
        return True
