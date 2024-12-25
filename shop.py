import pygame
import sys


class Shop:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        # 定义商店中的物品，每个物品都有名称、价格和位置矩形
        self.items = [
            {"name": "Item 1", "price": 100, "rect": pygame.Rect(50, 80, 100, 100)},
            {"name": "Item 2", "price": 200, "rect": pygame.Rect(250, 80, 100, 100)},
            {"name": "Item 3", "price": 300, "rect": pygame.Rect(450, 80, 100, 100)},
            {"name": "Item 4", "price": 100, "rect": pygame.Rect(650, 80, 100, 100)},
            {"name": "Item 5", "price": 200, "rect": pygame.Rect(850, 80, 100, 100)},

            {"name": "Item 6", "price": 300, "rect": pygame.Rect(50, 320, 100, 100)},
            {"name": "Item 7", "price": 100, "rect": pygame.Rect(250, 320, 100, 100)},
            {"name": "Item 8", "price": 200, "rect": pygame.Rect(450, 320, 100, 100)},
            {"name": "Item 9", "price": 300, "rect": pygame.Rect(650, 320, 100, 100)},
            {"name": "Item 10", "price": 100, "rect": pygame.Rect(850, 320, 100, 100)},
        ]
        self.buttons = []

    def draw(self):
        # 填充背景颜色为白色
        self.screen.fill((255, 255, 255))

        # 绘制每个物品的矩形、名称、价格和购买按钮
        for item in self.items:
            # 绘制物品的矩形
            pygame.draw.rect(self.screen, (0, 0, 255), item["rect"])
            # 绘制物品的名称和价格
            self.draw_text(f"{item['name']} - {item['price']}", item["rect"].x, item["rect"].y + 110)
            # 定义购买按钮的位置和大小
            button_rect = pygame.Rect(item["rect"].x + 10, item["rect"].y + 150, 80, 40)
            # 绘制购买按钮
            pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
            # 在购买按钮上绘制文字 "Buy"
            self.draw_text("Buy", button_rect.x + 15, button_rect.y + 10)
            # 将按钮和对应的物品添加到按钮列表中
            self.buttons.append((button_rect, item))

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, (x, y))

    def handle_event(self, event):
        # 检测鼠标点击事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 检查是否点击了刷新按钮
            if self.refresh_button.collidepoint(event.pos):
                print("Refresh button clicked")
                # 在这里添加刷新逻辑
            # 检查是否点击了购买按钮
            for button_rect, item in self.buttons:
                # 检查鼠标点击是否在某个按钮的范围内
                if button_rect.collidepoint(event.pos):
                    print(f"Bought {item['name']} for ${item['price']}")


def main():
    # 初始化pygame
    pygame.init()
    # 创建显示窗口
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Shop")
    # 创建Shop类的实例
    shop = Shop(screen)

    # 主循环
    while True:
        for event in pygame.event.get():
            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 处理商店中的事件
            shop.handle_event(event)

        # 绘制商店界面
        shop.draw()
        # 更新显示
        pygame.display.flip()


if __name__ == "__main__":
    main()
