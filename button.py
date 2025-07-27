import pygame
import os


class Button:
    def __init__(self, text, pos, size, action=None):
        self.text = text
        self.pos = pos
        self.size = size
        self.action = action
        #base surface 
        self.img: pygame.Surface =  pygame.image.load(os.path.join("assets", "buttons", "button_1", "UI_Button02a_1.png")) 
        self.img = pygame.transform.scale(self.img, self.size)
        self.img_hover: pygame.Surface = pygame.image.load(os.path.join("assets", "buttons", "button_1", "UI_Button02a_2.png"))
        self.img_hover = pygame.transform.scale(self.img_hover, self.size)

        self.active_img = self.img
    
    def set_image(self, image):
        self.active_img = image

    def draw(self, screen):
        # Draw the button on the screen # Scale the image to fit the button size
        screen.blit(self.img, self.pos)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.pos[0] + 10, self.pos[1] + 10))

    def click(self):
        if self.action:
            self.action()

    def hover_loop(self, mouse_pos):
        if self.is_hovered(mouse_pos):
            self.set_image(self.img_hover)
        else:
            self.set_image(self.img)

    def is_hovered(self, mouse_pos):
        x, y = self.pos
        width, height = self.size
        if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
            return True
        return False

    def is_clicked(self, mouse_pos):
        if self.is_hovered(mouse_pos):
            self.click()
            return True
        return False

