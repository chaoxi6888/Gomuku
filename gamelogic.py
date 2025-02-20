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

    def roundend(self, gameround, score_b, score_w, money, flag1, flag2, user1_cs, user2_cs, abilities):
        # 判断轮次是否结束的函数
        # 每回合胜利的人获得相应的金钱奖励
        if gameround == 1:
            if score_b == 10:  # 黑方获胜
                money[0] += 100  # 黑方获得100金币
                money[1] += 70  # 白方获得70金币
                user1_cs[0] = abilities[0]  # 黑方获得技能一
                user2_cs[0] = abilities[3]  # 白方获得技能四
                flag1[0] = True
                return True
            if score_w == 10:  # 白方获胜
                money[1] += 100  # 白方获得100金币
                money[0] += 70  # 黑方获得70金币
                user1_cs[0] = abilities[3]  # 黑方获得技能四
                user2_cs[0] = abilities[0]  # 白方获得技能一
                flag2[0] = True
                return True
        if gameround == 2:
            if score_b == 40:  # 40
                money[0] += 100
                money[1] += 70
                user1_cs[1] = abilities[1]  # 黑方获得技能二
                user2_cs[1] = abilities[4]  # 白方获得技能五
                flag1[1] = True
                return True
            if score_w == 40:
                money[1] += 100
                money[0] += 70
                user1_cs[1] = abilities[4]  # 黑方获得技能五
                user2_cs[1] = abilities[1]  # 白方获得技能二
                flag2[1] = True
                return True
        if gameround == 3:
            if score_b == 90:  # 90
                money[0] += 100
                money[1] += 70
                user1_cs[2] = abilities[2]  # 黑方获得技能三
                user2_cs[2] = abilities[5]  # 白方获得技能六
                flag1[2] = True
                return True
            if score_w == 90:
                money[1] += 100
                money[0] += 70
                user1_cs[2] = abilities[5]  # 黑方获得技能六
                user2_cs[2] = abilities[2]  # 白方获得技能三
                flag2[2] = True
                return True
        if gameround == 4:
            if score_b == 150:
                flag1[3] = True
                return True
            if score_w == 150:
                flag2[3] = True
                return True

    def roundinit(self, gameround, over_pos, cr_s):  # 初始化函数
        if gameround == 2:
            cr_s[0] = 2
            cr_s[3] = 2
        if gameround == 3:
            cr_s[0] = 3
            cr_s[3] = 3
            cr_s[1] = 2
            cr_s[4] = 2
        if gameround == 4:
            cr_s[0] = 5
            cr_s[3] = 5
            cr_s[1] = 4
            cr_s[4] = 4
            cr_s[2] = 3
            cr_s[5] = 3
        # 调用棋子移除函数移除所有函数:
        for pos in list(over_pos):
            over_pos.remove(pos)
