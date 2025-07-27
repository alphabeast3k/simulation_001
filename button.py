import pygame

class Button:
    def __init__(self, text, pos, size, action=None):
        self.text = text
        self.pos = pos
        self.size = size
        self.action = action

    def draw(self, screen):
        # Draw the button on the screen
        pygame.draw.rect(screen, (255, 255, 255), (*self.pos, *self.size))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.pos[0] + 10, self.pos[1] + 10))

    def click(self):
        if self.action:
            self.action()

    def is_hovered(self, mouse_pos):
        x, y = mouse_pos
        return (self.pos[0] <= x <= self.pos[0] + self.size[0] and
                self.pos[1] <= y <= self.pos[1] + self.size[1])