import pygame
from const import BLUE, WHITE, screen
button_width = 50
button_height = 20
class Button:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, button_width, button_height)
        self.text = text
    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
    def on_press(self, event, diff, s):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                diff = s