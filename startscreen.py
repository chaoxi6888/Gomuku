import pygame
import sys


class StartScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 834))
        self.background_image = pygame.image.load('image/游戏主界面.png')
        self.font = pygame.font.Font(None, 74)
        self.buttons = {
            "start": pygame.Rect(540, 200, 200, 50),
            "settings": pygame.Rect(540, 300, 200, 50),
            "quit": pygame.Rect(540, 400, 200, 50)
        }

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
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

    def show_settings(self):
        # 显示设置界面
        pass
