import pygame


class Cards:
    def __init__(self):
        self.ability2 = None
        self.ability4 = None
        self.ability5 = None
        self.ability6 = None
        """self.ability7 = None
        self.ability8 = None
        self.ability9 = None
        self.ability10 = None
        self.ability11 = None
        self.ability12 = None"""

    class Ability1:
        def __init__(self):
            self.image = pygame.image.load('image/ability1.png')
            self.name = 'ability1'
            self.description = '消去两个对方棋子'

        def ability(self, color, over_pos):
            # 技能1可以消去两个对方棋子
            count = 2
            for i in range(len(over_pos) - 1, -1, -1):
                if over_pos[i][1] == color and count > 0:  # 假设我们要移除白色棋子
                    over_pos.pop(i)
                    count -= 1

    class Ability2:
        def __init__(self):
            self.image = pygame.image.load('')
            self.name = 'ability2'
            self.description = ''

        def ability(self, color, over_pos):
            {}

    class Ability3:
        def __init__(self):
            self.image = pygame.image.load('image/ability3.png')
            self.name = 'ability3'
            self.description = '消去一个对方棋子'

        def ability(self, color, over_pos):
            # 技能2可以消去一个对方棋子
            count = 1
            for i in range(len(over_pos) - 1, -1, -1):
                if over_pos[i][1] == color and count > 0:  # 假设我们要移除白色棋子
                    over_pos.pop(i)
                    count -= 1
