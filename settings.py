class Settings:
    #  设置界面参数的类

    def __init__(self):
        # 游戏的静态设置
        self.screen_width = 1480  # 屏幕宽度
        self.screen_height = 780  # 屏幕高度
        self.screen_color = (255, 140, 0)  # 设置画布颜色,橙色
        self.line_color = [0, 0, 0]  # 设置线条颜色，[0,0,0]对应黑色
        self.chess_radius = 15  # 棋子半径
        self.chess_distance = 2  # 棋子间隔
        # 计算出棋盘和屏幕的距离
        self.border = (self.screen_height - 2 * (self.chess_distance + self.chess_radius) * (19 - 1)) / 2
        self.white_color = [255, 255, 255]  # 白棋颜色
        self.black_color = [0, 0, 0]  # 黑棋颜色
