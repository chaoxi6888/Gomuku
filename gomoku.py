# 调用pygame库
import pygame
import sys
# 调用常用关键字常量
from pygame.locals import QUIT, KEYDOWN
from settings import Settings
import numpy as np


class Gomoku:

    # 管理整个游戏资源的总体类
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 设置屏幕标题
        pygame.display.set_caption('Gomoku')
        # 创建一个Settings对象
        self.settings = Settings()
        self.distance = self.settings.chess_radius + self.settings.chess_distance  # 定义每根线之间的距离
        self.m = 2 * self.distance  # 间距
        self.w = self.settings.screen_width  # 屏幕宽度
        self.h = self.settings.screen_height  # 屏幕高度
        self.b = int(self.settings.border)  # 与上下边框的距离
        self.diff = int((self.w - self.h) / 2)  # 宽度与高度的差值
        # 设置屏幕参数
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()  # 创建一个Clock对象
        self.clock.tick(60)  # 控制游戏以60帧每秒运行
        self.tim = 0
        # 棋盘要使用的参数
        self.over_pos = []  # 表示已经落子的位置
        self.w_color = self.settings.white_color  # 白棋颜色
        self.b_color = self.settings.black_color  # 黑棋颜色
        self.flag = False

        while True:  # 不断训练刷新画布
            for event in pygame.event.get():  # 获取事件，如果鼠标点击右上角关闭按钮或点击esc，关闭
                if event.type in (QUIT, KEYDOWN):
                    sys.exit()
            self.screen.fill(self.settings.screen_color)  # 清屏
            self.drawchessboard()  # 生成棋盘

            # 获取鼠标坐标信息
            x, y = pygame.mouse.get_pos()
            x, y = self.find_pos(x, y)
            if self.check_over_pos(x, y, self.over_pos):  # 判断是否可以落子，再显示
                pygame.draw.rect(self.screen, [0, 229, 238], [x - self.distance, y - self.distance, self.m, self.m],
                                 2, 1)

            keys_pressed = pygame.mouse.get_pressed()  # 获取鼠标按键信息
            # 鼠标左键表示落子,tim用来延时的，因为每次循环时间间隔很断，容易导致明明只按了一次左键，却被多次获取，认为我按了多次
            if keys_pressed[0] and self.tim == 0:
                self.flag = True
                if self.check_over_pos(x, y, self.over_pos):  # 判断是否可以落子，再落子
                    if len(self.over_pos) % 2 == 0:  # 黑子
                        self.over_pos.append([[x, y], self.b_color])
                    else:
                        self.over_pos.append([[x, y], self.w_color])

            self.time_last()  # 调用延长时间函数
            for val in self.over_pos:  # 显示所有落下的棋子
                pygame.draw.circle(self.screen, val[1], val[0], 15, 0)
            pygame.display.update()  # 刷新显示

    def drawchessboard(self):
        # 绘制棋盘
        for i in range(self.b + self.diff, self.w - self.b - self.diff + 1, self.m):
            # 先画竖线
            if i == self.b + self.diff or i == self.w - self.b - self.diff:  # 边缘线稍微粗一些
                pygame.draw.line(self.screen, self.settings.line_color, [i, self.b], [i, self.h - self.b], 4)
            else:
                pygame.draw.line(self.screen, self.settings.line_color, [i, self.b], [i, self.h - self.b], 2)
        for i in range(self.b, self.h - self.b + 1, self.m):
            # 再画横线
            if i == self.b or i == self.h - self.b:  # 边缘线稍微粗一些
                pygame.draw.line(self.screen, self.settings.line_color, [self.b + self.diff, i],
                                 [self.w - self.b - self.diff, i], 4)
            else:
                pygame.draw.line(self.screen, self.settings.line_color, [self.b + self.diff, i],
                                 [self.w - self.b - self.diff, i], 2)
        # 在棋盘中心换一个圆点
        pygame.draw.circle(self.screen, self.settings.line_color,
                           [self.b + self.diff + self.m * 9, self.b + self.m * 9], 6, 0)

    def find_pos(self, x, y):
        # 找到显示的可以落子的位置
        for i in range(self.b + self.diff, self.w, self.m):
            for j in range(self.b, self.h, self.m):
                L1 = i - (self.settings.chess_radius + self.settings.chess_distance)
                L2 = i + (self.settings.chess_radius + self.settings.chess_distance)
                R1 = j - (self.settings.chess_radius + self.settings.chess_distance)
                R2 = j + (self.settings.chess_radius + self.settings.chess_distance)
                if L1 <= x <= L2 and R1 <= y <= R2:
                    return i, j
        return x, y

    def check_over_pos(self, x, y, over_pos):
        # 检查当前的位置是否已经落子
        for val in over_pos:
            if val[0][0] == x and val[0][1] == y:
                return False
        return True  # 表示没有落子

    def time_last(self):
        # 鼠标左键延时作用
        if self.flag:
            self.tim += 1
        if self.tim % 200 == 0:  # 延时200ms
            self.flag = False
            self.tim = 0




if __name__ == '__main__':
    # 创建一个游戏实例，并运行游戏。
    game = Gomoku()
