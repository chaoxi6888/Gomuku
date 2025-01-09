import pygame
import sys


class StartScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 834))
        self.background_image = pygame.image.load('image/游戏主界面.png')
        self.font = pygame.font.Font(None, 74)
        self.buttons = {
            "start": pygame.Rect(390, 400, 286, 98),
            "settings": pygame.Rect(380, 550, 305, 98),
            "quit": pygame.Rect(400, 700, 268, 98)
        }
        self.button_images = {
            "start": pygame.image.load('image/游戏开始按钮.png'),
            "settings": pygame.image.load('image/设置按钮.png'),
            "quit": pygame.image.load('image/退出按钮.png')
        }

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        for text, rect in self.buttons.items():
            button_image = self.button_images[text]
            self.screen.blit(button_image, rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for text, rect in self.buttons.items():
                if rect.collidepoint(event.pos):
                    return text
        return None

    def show_settings(self):
        # Display settings screen
        pass
