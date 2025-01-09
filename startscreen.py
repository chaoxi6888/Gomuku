import pygame
import sys


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.buttons = {
            "start": pygame.Rect(540, 200, 200, 50),
            "settings": pygame.Rect(540, 300, 200, 50),
            "quit": pygame.Rect(540, 400, 200, 50)
        }

    def draw(self):
        self.screen.fill((153, 204, 255))
        for text, rect in self.buttons.items():
            pygame.draw.rect(self.screen, (0, 0, 0), rect)
            button_text = self.font.render(text.capitalize(), True, (255, 255, 255))
            self.screen.blit(button_text, (rect.x + 20, rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for text, rect in self.buttons.items():
                if rect.collidepoint(event.pos):
                    return text
        return None
