# 调用pygame库
import pygame
import sys
# 调用常用关键字常量
from pygame.locals import QUIT, KEYDOWN
from settings import Settings
from gamelogic import Gamelogic
from image import Image
from music import Music
from user import User


class Gomoku:

    # 管理整个游戏资源的总体类
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 设置屏幕标题
        pygame.display.set_caption('Gomoku')
        # 创建一个Settings对象
        self.settings = Settings()
        # 创建一个gamelogic对象
        self.gamelogic = Gamelogic()
        # 创建两个user对象，即黑白方
        self.user1 = User()  # user1为黑方
        self.user2 = User()  # user2为白方
        # 创建一个image对象
        self.image = Image()
        self.round1 = self.image.image1  # 创建一个Round对象
        self.blackchess = self.image.image2  # 创建一个黑棋图像对象
        self.whitechess = self.image.image3  # 创建一个白棋图像对象
        self.background = self.image.image5
        self.font1 = pygame.font.Font(None, 48)  # 创建一个字体对象,用来显示黑方分数
        self.font2 = pygame.font.Font(None, 48)  # 创建一个字体对象，用来显示白方分数
        self.font3 = pygame.font.Font(None, 48)
        # 创建一个Music对象，指定音频文件路径
        self.music = Music("music/play_chess.mp3")
        # 播放背景音乐
        Music.play_background_music("music/bgm.wav", 0)

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

        while True:
            # 不断训练刷新画
            # 获取事件，如果鼠标点击右上角关闭按钮或点击esc，关闭
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    sys.exit()
            # 清屏
            self.screen.fill(self.settings.screen_color)
            # 生成Round1,黑棋，白棋
            self.image.blit(self.screen, self.round1, 620, 10)
            self.image.blit(self.screen, self.blackchess, 10, 10)
            self.image.blit(self.screen, self.whitechess, 1060, 10)
            # 渲染文本，第一个参数是文本内容，第二个参数是是否抗锯齿，第三个参数是文本颜色
            self.text_surface1 = self.font1.render(f'BLACK SCORE: {self.user1.score[0]}', True,
                                                   self.settings.black_color)
            # 渲染文本，第一个参数是文本内容，第二个参数是是否抗锯齿，第三个参数是文本颜色
            self.text_surface2 = self.font2.render(f'WHITE SCORE: {self.user2.score[0]}', True,
                                                   self.settings.black_color)
            # 生成黑方score
            self.image.blit(self.screen, self.text_surface1, 100, 40)
            # 生成黑方score
            self.image.blit(self.screen, self.text_surface2, 1150, 40)
            # 生成卡槽
            self.image.blit(self.screen, self.image.image4, 0, 210)
            self.image.blit(self.screen, self.image.image4, 1265, 210)
            # 生成棋盘
            self.gamelogic.drawchessboard(self.b, self.diff, self.w, self.m, self.screen, self.h,
                                          self.settings.line_color)
            # 判断是否存在五子连心
            res = self.gamelogic.check_win(self.over_pos, self.b, self.diff, self.m, self.w_color)
            if res[0] == 1:
                # 黑方加分
                self.user1.score[0] += 10
                for pos in res[1]:
                    # 调用棋子移除函数
                    self.gamelogic.remove_chess(self.image, self.over_pos, pos, self.screen, self.background,
                                                self.b, self.diff, self.m, self.b_color)
            if res[0] == 2:
                # 白方加分
                self.user2.score[0] += 10
                for pos in res[1]:
                    # 调用棋子移除函数
                    self.gamelogic.remove_chess(self.image, self.over_pos, pos, self.screen, self.background,
                                                self.b, self.diff, self.m, self.w_color)
            # 获取鼠标坐标信息
            x, y = pygame.mouse.get_pos()
            x, y = self.image.find_pos(x, y, self.b, self.diff, self.w, self.h, self.m, self.distance)
            # 先判断鼠标是否在棋盘范围内
            if self.click_check_board(x, y):
                if self.gamelogic.check_over_pos(x, y, self.over_pos):  # 判断是否可以落子，再显示
                    pygame.draw.rect(self.screen, [0, 229, 238], [x - self.distance, y - self.distance,
                                                                  self.m, self.m], 2, 1)
            # 获取鼠标按键信息
            keys_pressed = pygame.mouse.get_pressed()
            # 鼠标左键表示落子,tim用来延时的，因为每次循环时间间隔很断，容易导致明明只按了一次左键，却被多次获取，认为我按了多次
            if self.click_check_board(x, y):
                if keys_pressed[0] and self.tim == 0:
                    self.flag = True
                    if self.gamelogic.check_over_pos(x, y, self.over_pos):  # 判断是否可以落子，再落子
                        if len(self.over_pos) % 2 == 0:  # 黑子
                            self.over_pos.append([[x, y], self.b_color])
                        else:
                            self.over_pos.append([[x, y], self.w_color])
                    self.music.play_sound()  # 播放音效
            # 调用延长时间函数
            self.time_last()
            # 调用显示棋子函数
            self.gamelogic.showchess(self.over_pos, self.screen)
            # 刷新显示
            pygame.display.update()

    def time_last(self):
        # 鼠标左键延时作用
        if self.flag:
            self.tim += 1
        if self.tim % 50 == 0:  # 延时50ms
            self.flag = False
            self.tim = 0

    def click_check_board(self, x, y):
        if self.b + self.diff <= x <= self.w - self.b - self.diff and self.b <= y <= self.h - self.b:
            return True
        else:
            return False


if __name__ == '__main__':
    # 创建一个游戏实例，并运行游戏。
    game = Gomoku()
