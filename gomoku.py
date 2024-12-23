# 调用pygame库
import pygame
import sys
# 调用常用关键字常量
from pygame.locals import QUIT, KEYDOWN
from settings import Settings


class Gomoku:

    # 管理整个游戏资源的总体类
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 设置屏幕标题
        pygame.display.set_caption('Gomoku')
        # 创建一个Settings对象
        self.settings = Settings()
        # 设置屏幕参数
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()  # 创建一个Clock对象
        self.clock.tick(60)  # 控制游戏以60帧每秒运行

        while True:  # 不断训练刷新画布
            for event in pygame.event.get():  # 获取事件，如果鼠标点击右上角关闭按钮，关闭
                if event.type in (QUIT, KEYDOWN):
                    sys.exit()
            self.screen.fill(self.settings.screen_color)  # 清屏
            self.drawchessboard()
            # 获取鼠标坐标信息
            x, y = pygame.mouse.get_pos()
            x, y = self.find_pos(x, y)
            pygame.draw.rect(self.screen, [0, 229, 238], [x - 22, y - 22, 44, 44], 2, 1)
            pygame.display.update()  # 刷新显示

    def drawchessboard(self):
        w = self.settings.screen_width
        h = self.settings.screen_height
        b = int(self.settings.border)  # 与上下边框的距离
        m = 2 * (self.settings.chess_radius + self.settings.chess_distance)  # 间距
        diff = int((w - h) / 2)  # 宽度与高度的差值
        # 绘制棋盘
        for i in range(b + diff, w - b - diff + 1, m):
            # 先画竖线
            if i == b + diff or i == w - b - diff:  # 边缘线稍微粗一些
                pygame.draw.line(self.screen, self.settings.line_color, [i, b], [i, h - b], 4)
            else:
                pygame.draw.line(self.screen, self.settings.line_color, [i, b], [i, h - b], 2)
        for i in range(b, h - b + 1, m):
            # 再画横线
            if i == b or i == h - b:  # 边缘线稍微粗一些
                pygame.draw.line(self.screen, self.settings.line_color, [b + diff, i], [w - b - diff, i], 4)
            else:
                pygame.draw.line(self.screen, self.settings.line_color, [b + diff, i], [w - b - diff, i], 2)
        # 在棋盘中心换一个圆点
        pygame.draw.circle(self.screen, self.settings.line_color, [b + diff + m * 9, b + m * 9], 6, 0)

    def find_pos(self, x, y):  # 找到显示的可以落子的位置
        w = self.settings.screen_width
        h = self.settings.screen_height
        b = int(self.settings.border)  # 与上下边框的距离
        m = 2 * (self.settings.chess_radius + self.settings.chess_distance)  # 间距
        diff = int((w - h) / 2)  # 宽度与高度的差值
        for i in range(b + diff, w, m):
            for j in range(b, h, m):
                L1 = i - self.settings.chess_radius + self.settings.chess_distance
                L2 = i + self.settings.chess_radius + self.settings.chess_distance
                R1 = j - self.settings.chess_radius + self.settings.chess_distance
                R2 = j + self.settings.chess_radius + self.settings.chess_distance
                if L1 <= x <= L2 and R1 <= y <= R2:
                    return i, j
        return x, y


if __name__ == '__main__':
    # 创建一个游戏实例，并运行游戏。
    game = Gomoku()
