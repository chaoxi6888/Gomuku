class User:
    # 管理玩家的类
    def __init__(self):
        self.money = 0  # 货币
        self.score = [0, 0, 0, 0, 0]  # 存放每回合分数的列表,只使用后4个
        self.cards = [None, None, None]
        self.flag = [False, False, False, False]  # 用于判断每回合是否胜利
