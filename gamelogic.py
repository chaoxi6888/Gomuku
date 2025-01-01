import numpy as np
import pygame


class Gamelogic:
    # 管理游戏逻辑的类

    def check_win(self, over_pos, b, diff, m, w_color):
        # 判断五子连心的函数
        mp = np.zeros([19, 19], dtype=int)
        for val in over_pos:
            x = int((val[0][0] - b - diff) / m)
            y = int((val[0][1] - b) / m)
            if val[1] == w_color:
                mp[x][y] = 2  # 表示白子
            else:
                mp[x][y] = 1  # 表示黑子

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 四个方向的移动向量

        for direction in directions:
            for i in range(19):
                for j in range(19):
                    pos1 = []
                    pos2 = []
                    for k in range(5):  # 只需要检查连续的五个位置
                        ni, nj = i + k * direction[0], j + k * direction[1]
                        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
                            break
                        if mp[ni][nj] == 1:
                            pos1.append([ni, nj])
                        else:
                            pos1 = []
                        if mp[ni][nj] == 2:
                            pos2.append([ni, nj])
                        else:
                            pos2 = []
                        if len(pos1) >= 5:
                            return [1, pos1]
                        if len(pos2) >= 5:
                            return [2, pos2]
        return [0, []]

    def check_over_pos(self, x, y, over_pos):
        # 检查当前的位置是否已经落子
        for val in over_pos:
            if val[0][0] == x and val[0][1] == y:
                return False
        return True  # 表示没有落子

    def drawchessboard(self, b, diff, w, m, screen, h, color):
        # 绘制棋盘
        for i in range(b + diff, w - b - diff + 1, m):
            # 先画竖线
            if i == b + diff or i == w - b - diff:  # 边缘线稍微粗一些
                pygame.draw.line(screen, color, [i, b], [i, h - b], 4)
            else:
                pygame.draw.line(screen, color, [i, b], [i, h - b], 2)
        for i in range(b, h - b + 1, m):
            # 再画横线
            if i == b or i == h - b:  # 边缘线稍微粗一些
                pygame.draw.line(screen, color, [b + diff, i],
                                 [w - b - diff, i], 4)
            else:
                pygame.draw.line(screen, color, [b + diff, i],
                                 [w - b - diff, i], 2)
        # 在棋盘中心换一个圆点
        pygame.draw.circle(screen, color, [b + diff + m * 9, b + m * 9], 6, 0)

    def showchess(self, over_pos, screen):
        # 展示所有棋子
        for val in over_pos:  # 显示所有落下的棋子
            pygame.draw.circle(screen, val[1], val[0], 15, 0)

    def remove_chess(self, image, over_pos, pos, screen, background, b, diff, m, color):
        # 假设 pos 是一个列表，其中包含要移除棋子的 x 和 y 坐标
        # background 是屏幕背景的 Surface 对象
        # 绘制背景来覆盖棋子
        over_pos.remove([[b + diff + pos[0] * m, b + pos[1] * m], color])
        "image.blit(screen, background, pos[0] - 15, pos[1] - 15)"

    def roundend(self, gameround, score_b, score_w, money_b, money_w):
        # 判断轮次是否结束的函数
        # 每回合胜利的人获得相应的金钱奖励
        if gameround == 1:
            if score_b == 10:  # 黑方获胜
                money_b += 100  # 黑方获得100金币
                money_w += 70  # 白方获得70金币
                return True
            if score_w == 10:  # 白方获胜
                money_w += 100  # 白方获得100金币
                money_b += 70  # 黑方获得70金币
                return True
        if gameround == 2:
            if score_b == 50:
                money_b += 100
                money_w += 70
                return True
            if score_w == 50:
                money_w += 100
                money_b += 70
                return True
        if gameround == 3:
            if score_b == 100:
                money_b += 100
                money_w += 70
                return True
            if score_w == 100:
                money_w += 100
                money_b += 70
                return True
        if gameround == 4:
            if score_b == 200:
                money_b += 100
                money_w += 70
                return True
            if score_w == 200:
                money_w += 100
                money_b += 70
                return True

    def roundinit(self, gameround, over_pos, cr1_1, cr1_2, cr2_1, cr2_2, cr3_1, cr3_2):  # 初始化函数
        if gameround == 2:
            cr1_1 = 3
            cr1_2 = 3
            cr2_1 = 3
            cr2_2 = 3
            cr3_1 = 3
            cr3_2 = 3
            # 调用棋子移除函数移除所有函数:
            for pos in list(over_pos):
                over_pos.remove(pos)

