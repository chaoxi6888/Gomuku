import pygame


class Cards:
    def __init__(self):
        self.shop = [self.Ability7(), self.Ability8(), self.Ability9(), self.Ability10()]

    class Ability1:
        def __init__(self):
            self.image = pygame.image.load('image/ability1.png')
            self.name = 'ability1'
            self.description = '消去敌方最近下的两个棋子'

        def ability(self, color, center_x, center_y, over_pos, m):
            # 技能1可以消去两个对方棋子
            count = 2
            for i in range(len(over_pos) - 1, -1, -1):
                if over_pos[i][1] == color and count > 0:  # 假设我们要移除白色棋子
                    over_pos.pop(i)
                    count -= 1

    class Ability2:
        def __init__(self):
            self.image = pygame.image.load('image/ability2.png')
            self.name = 'ability2'
            self.description = '替换敌方棋子'

        def ability(self, color, over_pos, x1, y1, m):
            # 技能2可以将一个敌方棋子替换为我方棋子
            {}

    class Ability3:
        def __init__(self):
            self.image = pygame.image.load('image/ability3.png')
            self.name = 'ability3'
            self.description = '摧毁5*5区域'

        def ability(self, color, center_x, center_y, over_pos, m):
            # 技能3可以摧毁5*5区域
            # 定义5*5区域的边界
            left = center_x - 2 * m
            right = center_x + 2 * m
            top = center_y - 2 * m
            bottom = center_y + 2 * m
            # 创建一个新列表，排除在5*5区域内的位置
            over_pos1 = [pos for pos in over_pos if not (left <= pos[0][0] <= right and top <= pos[0][1] <= bottom)]
            return over_pos1  # 返回更新后的位置列表

    class Ability4:
        def __init__(self):
            self.image = pygame.image.load('image/ability4.png')
            self.name = 'ability4'
            self.description = '消去一个敌方最近下的棋子'

        def ability(self, color, center_x, center_y, over_pos, m):
            # 技能4可以消去一个对方棋子
            count = 1
            for i in range(len(over_pos) - 1, -1, -1):
                if over_pos[i][1] == color and count > 0:  # 假设我们要移除白色棋子
                    over_pos.pop(i)
                    count -= 1

    class Ability5:
        def __init__(self):
            self.image = pygame.image.load('image/ability5.png')
            self.name = 'ability5'
            self.description = '消去一个任意敌方棋子'

        def ability(self, x1, y1, color, over_pos, music):
            # 技能5可以将一个敌方棋子替换为我方棋子
            {}

    class Ability6:
        def __init__(self):
            self.image = pygame.image.load('image/ability6.png')
            self.name = 'ability6'
            self.description = '摧毁区域'

        def ability(self, color, center_x, center_y, over_pos, m):
            # 技能3可以摧毁5*5区域
            # 定义5*5区域的边界
            left = center_x - m
            right = center_x + m
            top = center_y - m
            bottom = center_y + m
            # 创建一个新列表，排除在5*5区域内的位置
            over_pos1 = [pos for pos in over_pos if not (left <= pos[0][0] <= right and top <= pos[0][1] <= bottom)]
            return over_pos1  # 返回更新后的位置列表

    class Ability7:
        def __init__(self):
            self.image = pygame.image.load('image/ability7.png')
            self.name = 'ability7'
            self.description = '消去一行的棋子'

        def ability(self, color, lis, row, over_pos, m):
            # 技能7可以消去一行棋子
            over_pos1 = [pos for pos in over_pos if pos[0][1] != row]
            return over_pos1

    class Ability8:
        def __init__(self):
            self.image = pygame.image.load('image/ability8.png')
            self.name = 'ability8'
            self.description = '消去一列的棋子'

        def ability(self, color, lis, row, over_pos, m):
            # 技能7可以消去一行棋子
            over_pos1 = [pos for pos in over_pos if pos[0][1] != lis]
            return over_pos1

    class Ability9:
        def __init__(self):
            self.image = pygame.image.load('image/ability9.png')
            self.name = 'ability9'
            self.description = '消去一个对角线的棋子'

        def ability(self, color, center_x, center_y, over_pos, m):
            # 技能9可以消去一个对角线的棋子
            over_pos1 = [pos for pos in over_pos if not (
                    (pos[0][0] - center_x == pos[0][1] - center_y) or
                    (pos[0][0] - center_x == center_y - pos[0][1])
            )]
            return over_pos1

    class Ability10:
        def __init__(self):
            self.image = pygame.image.load('image/ability10.png')
            self.name = 'ability10'
            self.description = '消去一个5*5十字范围的的棋子'

        def ability(self, color, center_x, center_y, over_pos, m):
            # 技能10可以消去一个5*5十字范围的棋子
            over_pos1 = [pos for pos in over_pos if not (
                    (center_x - m <= pos[0][0] <= center_x + m and pos[0][1] == center_y) or
                    (center_y - m <= pos[0][1] <= center_y + m and pos[0][0] == center_x)
            )]
            return over_pos1
