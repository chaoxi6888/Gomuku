import pygame
import sys


class StartScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 834))
        self.background_image = pygame.image.load('image/游戏主界面.png')
        self.font = pygame.font.Font(None, 74)
        self.buttons = {
            "start": pygame.Rect(390, 400, 286, 98),  # 开始按钮，位置 (390, 400)，宽度 286，高度 98
            "settings": pygame.Rect(380, 550, 305, 98),  # 设置按钮，位置 (380, 550)，宽度 305，高度 98
            "quit": pygame.Rect(400, 700, 268, 98)  # 退出按钮，位置 (400, 700)，宽度 268，高度 98
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
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # 向上滚动
                        pygame.mixer.music.set_volume(min(pygame.mixer.music.get_volume() + 0.1, 1.0))
                    elif event.button == 5:  # 向下滚动
                        pygame.mixer.music.set_volume(max(pygame.mixer.music.get_volume() - 0.1, 0.0))

            self.screen.fill((0, 0, 0))
            volume_text = self.font.render(f'音量: {pygame.mixer.music.get_volume():.1f}', True, (255, 255, 255))
            self.screen.blit(volume_text, (
            self.screen.get_width() // 2 - volume_text.get_width() // 2, self.screen.get_height() // 2))
            pygame.display.flip()
