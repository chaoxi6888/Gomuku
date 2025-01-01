import pygame


class Image:
    # 管理图像的类
    def __init__(self):
        self.image2 = pygame.image.load('image/blackchess.png')
        self.image3 = pygame.image.load('image/whitechess.png')
        self.image4 = pygame.image.load('image/card.png')
        self.image5 = pygame.image.load('image/background.png')
        self.image6 = pygame.image.load('image/referto.png')

    def find_pos(self, x, y, b, diff, w, h, m, distance):
        # 可以落子的位置
        for i in range(b + diff, w - b - diff + 1, m):
            for j in range(b, h - b + 1, m):
                L1 = i - distance
                L2 = i + distance
                R1 = j - distance
                R2 = j + distance
                if L1 <= x <= L2 and R1 <= y <= R2:
                    return i, j
        return x, y

    def blit(self, screen, image, x, y):
        # 将图片绘制到屏幕上
        screen.blit(image, (x, y))  # 图片显示在屏幕的(x,y)处
