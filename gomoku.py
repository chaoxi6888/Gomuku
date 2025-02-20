# 调用pygame库
import pygame
import sys
# 调用常用关键字常量
from settings import Settings
from gamelogic import Gamelogic
from image import Image
from music import Music
from user import User
from cards import Cards
from shop import Shop
from startscreen import StartScreen


class Gomoku:

    # 管理整个游戏资源的总体类
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 设置屏幕标题
        pygame.display.set_caption('技能版五子棋')
        # 创建一个Settings对象
        self.settings = Settings()
        # 创建一个gamelogic对象
        self.gamelogic = Gamelogic()
        # 创建一个cards对象
        self.cards = Cards()
        # 创建两个user对象，即黑白方
        self.user1 = User()  # user1为黑方
        self.u1_cs = self.user1.cards  # 黑方卡槽初始化
        self.user2 = User()  # user2为白方
        self.u2_cs = self.user2.cards  # 白方卡槽初始化
        self.money = [self.user1.money, self.user2.money]  # 双方货币初始化
        # 创建六个技能对象和存放技能的列表
        self.ability1 = self.cards.Ability1()
        self.ability2 = self.cards.Ability2()
        self.ability3 = self.cards.Ability3()
        self.ability4 = self.cards.Ability4()
        self.ability5 = self.cards.Ability5()
        self.ability6 = self.cards.Ability6()
        # 定义商店技能组
        self.ability7 = self.cards.Ability7()
        self.ability8 = self.cards.Ability8()
        self.ability9 = self.cards.Ability9()
        self.ability10 = self.cards.Ability10()
        self.abilities = [self.ability1, self.ability2, self.ability3, self.ability4, self.ability5, self.ability6]
        # 创建一个image对象
        self.image = Image()
        self.blackchess = self.image.image2  # 创建一个黑棋图像对象
        self.whitechess = self.image.image3  # 创建一个白棋图像对象
        self.background = self.image.image5  # 创建一个背景图像对象
        self.referto = self.image.image6  # 创建一个箭头对象
        self.font1 = pygame.font.Font(None, 48)  # 创建一个字体对象
        self.font2 = pygame.font.Font('ttf/AiDianFengYaHei（ShangYongMianFei）-2.ttf', 60)  # 创建一个字体对象
        self.font3 = pygame.font.Font('ttf/AiDianFengYaHei（ShangYongMianFei）-2.ttf', 30)
        # 创建一个Music对象，指定音频文件路径
        self.music = Music("music/play_chess.mp3")
        # 播放背景音乐
        Music.play_background_music("music/bgm.wav", 0.2)

        self.round = 1
        self.distance = self.settings.chess_radius + self.settings.chess_distance  # 定义每根线之间的距离
        self.m = 2 * self.distance  # 间距
        self.w = self.settings.screen_width  # 屏幕宽度
        self.h = self.settings.screen_height  # 屏幕高度
        self.b = int(self.settings.border)  # 与上下边框的距离
        self.diff = int((self.w - self.h) / 2)  # 宽度与高度的差值

        self.enter_shop1 = False  # 进入黑方商店标志
        self.enter_shop2 = False  # 进入白方商店标志
        self.clock = pygame.time.Clock()  # 创建一个Clock对象
        self.clock.tick(60)  # 控制游戏以60帧每秒运行
        # 棋盘要使用的参数
        self.over_pos = []  # 表示已经落子的位置
        self.w_color = self.settings.white_color  # 白棋颜色
        self.b_color = self.settings.black_color  # 黑棋颜色
        self.k = 0
        # 初始化技能可使用次数
        self.cr_s = [0, 0, 0, 0, 0, 0]
        # 初始技能槽列表标志
        self.flags = [False, False, False, False, False, False]
        self.last_esc_time = 0  # 初始化 ESC 键的计时器
        self.bflag = [False, False]
        self.staflag = False
        # 初始化游戏开始屏幕
        self.start_screen = StartScreen()
        self.show_start_screen()
        # 设置屏幕参数
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        while self.staflag:
            # 清屏
            self.screen.fill(self.settings.screen_color)
            # 商店关闭标志
            self.shop1_closed = False
            self.shop2_closed = False
            while self.enter_shop1 or self.enter_shop2:
                if self.enter_shop1:
                    self.shop_screen1()
                    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
                    self.enter_shop1 = False
                if self.enter_shop2:
                    self.shop_screen2()
                    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
                    self.enter_shop2 = False

            pygame.display.set_caption('技能版五子棋')
            # 生成黑棋，白棋
            self.image.blit(self.screen, self.blackchess, 10, 10)
            self.image.blit(self.screen, self.whitechess, 1060, 10)
            # 渲染文本，第一个参数是文本内容，第二个参数是是否抗锯齿，第三个参数是文本颜色
            self.text_surface1 = self.font1.render(f'BLACK SCORE: {self.user1.score[self.round]}', True,
                                                   self.settings.black_color)
            self.text_surface2 = self.font1.render(f'WHITE SCORE: {self.user2.score[self.round]}', True,
                                                   self.settings.black_color)
            self.text_surface3 = self.font2.render(f'ROUND{self.round}', True, self.settings.black_color)
            self.text_surface4 = self.font3.render(f'现在轮到你了', True, self.settings.black_color)
            self.text_surface5 = self.font1.render(f'{self.cr_s[0]}', True, self.settings.black_color)
            self.text_surface6 = self.font1.render(f'{self.cr_s[1]}', True, self.settings.black_color)
            self.text_surface7 = self.font1.render(f'{self.cr_s[2]}', True, self.settings.black_color)
            self.text_surface8 = self.font1.render(f'{self.cr_s[3]}', True, self.settings.black_color)
            self.text_surface9 = self.font1.render(f'{self.cr_s[4]}', True, self.settings.black_color)
            self.text_surface10 = self.font1.render(f'{self.cr_s[5]}', True, self.settings.black_color)
            self.text_s1 = [self.text_surface5, self.text_surface6, self.text_surface7]
            self.text_s2 = [self.text_surface8, self.text_surface9, self.text_surface10]
            # 生成黑方score
            self.image.blit(self.screen, self.text_surface1, 100, 40)
            # 生成黑方score
            self.image.blit(self.screen, self.text_surface2, 1150, 40)
            # 生成round
            self.image.blit(self.screen, self.text_surface3, 627, 20)
            # 生成双方卡槽
            self.image.blit(self.screen, self.image.image4, 0, 210)
            self.image.blit(self.screen, self.image.image4, 1265, 210)
            # 生成黑方技能
            for i in range(3):
                if self.u1_cs[i] is not None:
                    self.image.blit(self.screen, self.u1_cs[i].image, 7, 217 + 569 / 3 * i)
            # 生成白方技能
            for i in range(3):
                if self.u2_cs[i] is not None:
                    self.image.blit(self.screen, self.u2_cs[i].image, 1272, 217 + 569 / 3 * i)

            # 绘制技能剩余可使用次数
            for i in range(3):
                self.image.blit(self.screen, self.text_s1[i], 190, 217 + 569 / 3 * i)
                self.image.blit(self.screen, self.text_s2[i], 1455, 217 + 569 / 3 * i)

            self.bf = False
            self.wf = False
            # 生成箭头
            if (len(self.over_pos) + self.k) % 2 == 0:  # 轮到黑子
                self.bf = True
                self.image.blit(self.screen, self.referto, 214, self.h - 124)
                self.image.blit(self.screen, self.text_surface4, 174 + 40, self.h - 164)
            else:  # 轮到白子
                self.wf = True
                self.image.blit(self.screen, self.referto, 1265 - 144, self.h - 124)
                self.image.blit(self.screen, self.text_surface4, 1185 - 144 + 40, self.h - 164)
            # 生成棋盘
            self.gamelogic.drawchessboard(self.b, self.diff, self.w, self.m, self.screen, self.h,
                                          self.settings.line_color)
            # 判断是否存在五子连心
            res = self.gamelogic.check_win(self.over_pos, self.b, self.diff, self.m, self.w_color)
            if res[0] == 1:
                # 黑方加分
                self.user1.score[self.round] += 10
                for pos in res[1]:
                    # 调用棋子移除函数
                    self.gamelogic.remove_chess(self.image, self.over_pos, pos, self.screen, self.background,
                                                self.b, self.diff, self.m, self.b_color)
            if res[0] == 2:
                # 白方加分
                self.user2.score[self.round] += 10
                for pos in res[1]:
                    # 调用棋子移除函数
                    self.gamelogic.remove_chess(self.image, self.over_pos, pos, self.screen, self.background,
                                                self.b, self.diff, self.m, self.w_color)
            # 判断回合是否结束
            if self.gamelogic.roundend(self.round, self.user1.score[self.round], self.user2.score[self.round],
                                       self.money, self.user1.flag, self.user2.flag,
                                       self.u1_cs, self.u2_cs, self.abilities):
                self.round += 1
                # 第二回合结束才开启商店
                if self.round == 4:
                    self.enter_shop1 = True  # 进入商店
                    self.enter_shop2 = True
                if self.round > 4:
                    break
                self.gamelogic.roundinit(self.round, self.over_pos, self.cr_s)  # 调用回合初始函数

            # 获取鼠标坐标信息
            x, y = pygame.mouse.get_pos()
            x, y = self.image.find_pos(x, y, self.b, self.diff, self.w, self.h, self.m, self.distance)

            # 先判断鼠标是否在棋盘范围内然后再显示
            if self.click_check_board(x, y):
                if self.gamelogic.check_over_pos(x, y, self.over_pos):  # 判断是否可以落子，再显示
                    pygame.draw.rect(self.screen, [0, 229, 238], [x - self.distance, y - self.distance,
                                                                  self.m, self.m], 2, 1)
            # 判断是否点击了技能卡槽,再显示
            self.side = 0
            self.n = 0
            if self.click_check_cards_board(x, y):
                if self.side == 1:
                    pygame.draw.rect(self.screen, [0, 229, 238], [0, 214 + 569 / 3 * (self.n - 1),
                                                                  214, (self.h - 210) / 3], 2, 5)
                if self.side == 2:
                    pygame.draw.rect(self.screen, [0, 229, 238], [1265, 214 + 569 / 3 * (self.n - 1),
                                                                  214, (self.h - 210) / 3], 2, 5)
            # 事件处理
            for event in pygame.event.get():
                self.side = 0
                self.n = 0
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检查鼠标点击是否在指定区域内
                    xt, yt = event.pos[0], event.pos[1]
                    if self.click_check_cards_board(xt, yt):
                        # 技能一
                        if self.side == 1 and self.n == 1 and self.cr_s[0] > 0:
                            if not self.bflag[0]:
                                self.flags[0] = True
                                self.k += 2
                                self.u1_cs[0].ability(self.w_color, 0, 0, self.over_pos, self.m)
                                self.cr_s[0] -= 1
                                self.flags[0] = False
                            elif self.bflag[0]:
                                self.flags[0] = True
                        # 技能二
                        if self.side == 1 and self.n == 2 and self.cr_s[1] > 0:
                            self.flags[1] = True
                        # 技能三
                        if self.side == 1 and self.n == 3 and self.cr_s[2] > 0:
                            self.flags[2] = True
                        # 技能四
                        if self.side == 2 and self.n == 1 and self.cr_s[3] > 0:
                            if not self.bflag[1]:
                                self.flags[3] = True
                                self.k += 1
                                self.u2_cs[0].ability(self.b_color, 0, 0, self.over_pos, self.m)
                                self.cr_s[3] -= 1
                                self.flags[3] = False
                            elif self.bflag[1]:
                                self.flags[3] = True
                        # 技能五
                        if self.side == 2 and self.n == 2 and self.cr_s[4] > 0:
                            self.flags[4] = True
                        # 技能六
                        if self.side == 2 and self.n == 3 and self.cr_s[5] > 0:
                            self.flags[5] = True
                    b, i = self.check_flags()
                    if self.click_check_board(xt, yt) and b:
                        x1, y1 = self.image.find_pos(xt, yt, self.b, self.diff, self.w, self.h, self.m, self.distance)
                        if self.gamelogic.check_over_pos(x1, y1, self.over_pos):  # 判断是否可以落子，再落子
                            if (len(self.over_pos) + self.k) % 2 == 0:  # 黑子
                                self.over_pos.append([[x1, y1], self.b_color])
                                self.music.play_sound()  # 播放音效
                            else:  # 白子
                                self.over_pos.append([[x1, y1], self.w_color])
                                self.music.play_sound()  # 播放音效
                    elif self.click_check_board(xt, yt) and not b:
                        x2, y2 = self.image.find_pos(xt, yt, self.b, self.diff, self.w, self.h, self.m, self.distance)
                        if i == 1:
                            if self.u1_cs[1].ability(self.w_color, x2, y2, self.over_pos, self.m):
                                self.cr_s[i] -= 1
                            self.flags[i] = False
                        if i == 4:
                            if self.u2_cs[1].ability(self.b_color, x2, y2, self.over_pos, self.m):
                                self.k += 1
                                self.cr_s[i] -= 1
                            self.flags[i] = False
                        if i == 2:
                            self.over_pos = self.u1_cs[2].ability(self.w_color, x2, y2, self.over_pos, self.m)
                            self.cr_s[2] -= 1
                            self.flags[i] = False
                        if i == 5:
                            self.over_pos = self.u2_cs[2].ability(self.b_color, x2, y2, self.over_pos, self.m)
                            self.cr_s[5] -= 1
                            self.flags[i] = False
                        if i == 0 and self.bflag[0]:
                            self.over_pos = self.u1_cs[0].ability(self.w_color, x2, y2, self.over_pos, self.m)
                            self.cr_s[0] -= 1
                            self.flags[i] = False
                        if i == 3 and self.bflag[1]:
                            self.over_pos = self.u2_cs[0].ability(self.b_color, x2, y2, self.over_pos, self.m)
                            self.cr_s[3] -= 1
                            self.flags[i] = False

            # 调用延长时间函数
            "self.time_last()"
            # 调用显示棋子函数
            self.gamelogic.showchess(self.over_pos, self.screen)
            # 刷新显示
            pygame.display.update()

        # 游戏结束生成积分板
        if self.staflag:
            self.game_over_screen()

    def click_check_board(self, x, y):
        # 判断鼠标是否在棋盘范围内
        if self.b + self.diff <= x <= self.w - self.b - self.diff and self.b <= y <= self.h - self.b:
            return True
        else:
            return False

    def click_check_cards_board(self, x, y):
        # 判断鼠标是否点击技能卡槽
        # 点击黑方卡槽第一个技能
        if (0 <= x <= 214 and 210 <= y <= 210 + (self.h - 210) / 3) and self.bf:
            self.side = 1
            self.n = 1
            return True
        # 点击黑方卡槽第二个技能
        elif (0 <= x <= 214 and 210 + (self.h - 210) / 3 <= y <= 210 + (self.h - 210) / 3 * 2) and self.bf:
            self.side = 1
            self.n = 2
            return True
        # 点击黑方卡槽第三个技能
        elif (0 <= x <= 214 and 210 + (self.h - 210) / 3 * 2 <= y <= self.h) and self.bf:
            self.side = 1
            self.n = 3
            return True
        # 点击白方卡槽第一个技能
        if (1265 <= x <= self.w and 210 <= y <= 210 + (self.h - 210) / 3) and self.wf:
            self.side = 2
            self.n = 1
            return True
        # 点击白方卡槽第二个技能
        elif (1265 <= x <= self.w and 210 + (self.h - 210) / 3 <= y <= 210 + (self.h - 210) / 3 * 2) and self.wf:
            self.side = 2
            self.n = 2
            return True
        # 点击白方卡槽第三个技能
        elif (1265 <= x <= self.w and 210 + (self.h - 210) / 3 * 2 <= y <= self.h) and self.wf:
            self.side = 2
            self.n = 3
            return True
        # 点击其他位置
        else:
            return False

    def check_flags(self):
        # 检查技能槽是否有一个处在点击状态
        for i in range(6):
            if self.flags[i]:
                return False, i
        return True, None

    # 添加一个方法来显示商店界面
    def shop_screen1(self):
        # 黑方的商店
        pygame.display.set_caption('黑方shop')
        shop1 = Shop(self.money[0], self.cards)
        while not self.shop1_closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                shop1.handle_event(event, self.u1_cs, self.money, 0, self.bflag)
            shop1.draw()
            pygame.display.flip()
            # 检查是否需要退出商店界面
            if self.check_exit_shop1():
                self.shop1_closed = True

    def shop_screen2(self):
        # 白方的商店
        pygame.display.set_caption('白方shop')
        shop2 = Shop(self.money[1], self.cards)
        while not self.shop2_closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                shop2.handle_event(event, self.u2_cs, self.money, 1, self.bflag)
            shop2.draw()
            pygame.display.flip()
            # 检查是否需要退出商店界面
            if self.check_exit_shop1():
                self.shop2_closed = True

    def check_exit_shop1(self):
        # 获取当前时间
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and current_time - self.last_esc_time > 2000:  # 1000 毫秒 = 1 秒
            self.last_esc_time = current_time  # 更新上次按下 ESC 键的时间
            return True
        return False

    def game_over_screen(self):
        # 创建一个新的屏幕
        game_over_screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Game Over')

        # 显示游戏结束信息
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over', True, (255, 0, 0))
        game_over_screen.fill((153, 204, 255))
        game_over_screen.blit(text, (self.settings.screen_width // 2 - text.get_width() // 2,
                                     self.settings.screen_height // 2 - text.get_height() // 2 - 200))
        win_image = pygame.image.load('image/win.png')

        # 显示其他数据
        score_text = font.render(f'Final Score: {self.user1.score[4]} - {self.user2.score[4]}', True,
                                 (255, 255, 255))
        score_text2 = font.render(f'first:{self.user1.score[1]} - {self.user2.score[1]}', True,
                                  (255, 255, 255))
        score_text3 = font.render(f'second:{self.user1.score[2]} - {self.user2.score[2]}', True,
                                  (255, 255, 255))
        score_text4 = font.render(f'third:{self.user1.score[3]} - {self.user2.score[3]}', True,
                                  (255, 255, 255))
        if self.user1.score[4] > self.user2.score[4]:
            text_win = font.render('BLACK Win!', True, (255, 255, 255))
        else:
            text_win = font.render('WHITE Win!', True, (255, 255, 255))
        game_over_screen.blit(score_text, (self.settings.screen_width // 2 - score_text.get_width() // 2,
                                           self.settings.screen_height // 2 + text.get_height()))
        game_over_screen.blit(score_text2, (self.settings.screen_width // 2 - score_text.get_width() // 2 + 120,
                                            self.settings.screen_height // 2 + text.get_height() + 50))
        game_over_screen.blit(score_text3, (self.settings.screen_width // 2 - score_text.get_width() // 2 + 38,
                                            self.settings.screen_height // 2 + text.get_height() + 100))
        game_over_screen.blit(score_text4, (self.settings.screen_width // 2 - score_text.get_width() // 2 + 103,
                                            self.settings.screen_height // 2 + text.get_height() + 150))
        game_over_screen.blit(text_win, (self.settings.screen_width // 2 - text_win.get_width() // 2,
                                         self.settings.screen_height // 2 - text_win.get_height() // 2 - 100))
        self.image.blit(game_over_screen, win_image, self.settings.screen_width // 2 - text_win.get_width() // 2 + 300,
                        self.settings.screen_height // 2 - text_win.get_height() // 2 - 100)

        pygame.display.flip()

        # 等待用户退出
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def show_start_screen(self):
        while not self.staflag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                action = self.start_screen.handle_event(event)
                if action == "start":
                    self.staflag = True
                    break
                elif action == "settings":
                    self.start_screen.show_settings()
                elif action == "quit":
                    pygame.quit()
                    sys.exit()
            self.start_screen.draw()
            pygame.display.flip()


if __name__ == '__main__':
    # 创建一个游戏实例，并运行游戏。
    game = Gomoku()
