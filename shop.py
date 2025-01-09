import pygame
import tkinter as tk
from tkinter import simpledialog, messagebox


class Shop:
    def __init__(self, money, cards):
        self.money = money
        self.cards = cards  # 接收 Cards 类的实例
        self.screen = pygame.display.set_mode((1000, 600))
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load('image/shop.png')
        self.items = self.load_items_from_cards()  # 从 Cards 类加载商店列表
        self.buttons = self.create_buttons()

    def load_items_from_cards(self):
        # 从 Cards 类加载商店列表
        items = []
        for card in self.cards.shop_list:
            item = {
                "name": card,
                "price": card.price,
                "rect": pygame.Rect(card.x - 28, card.y - 2, 100, 100),
                "image": card.shop_image
            }
            items.append(item)
        return items

    def create_buttons(self):
        buttons = []
        for item in self.items:
            button_rect = pygame.Rect(item["rect"].x + 38, item["rect"].y + 170, 80, 40)
            buttons.append((button_rect, item))
        return buttons

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        for item in self.items:
            self.screen.blit(item["image"], item["rect"])  # 绘制图像
            self.draw_text(f"cost-{item['price']}", item["rect"].x + 40, item["rect"].y + 140)
        for button_rect, _ in self.buttons:
            pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
            self.draw_text("Buy", button_rect.x + 15, button_rect.y + 10)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_surface1 = self.font.render(f'money:{self.money}', True, (0, 0, 0))
        self.screen.blit(text_surface, (x, y))
        self.screen.blit(text_surface1, (10, 10))

    def handle_event(self, event, cs):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button_rect, item in self.buttons:
                if button_rect.collidepoint(event.pos):
                    if self.money >= item['price']:
                        root = tk.Tk()
                        root.withdraw()  # 隐藏主窗口
                        skill_number = simpledialog.askinteger("替换技能", "输入要替换的技能编号 (1-3):")
                        root.destroy()
                        if skill_number in [1, 2, 3]:
                            self.money -= item['price']
                            cs[skill_number - 1] = item['name']  # 替换技能
                            print(f"用 {item['name']} 替换了技能 {skill_number}，花费 ${item['price']}")
                        else:
                            messagebox.showinfo("无效输入", "请输入有效的技能编号 (1-3)。")
                    else:
                        root = tk.Tk()
                        root.withdraw()  # 隐藏主窗口
                        messagebox.showinfo("购买失败", "没有足够的货币来购买")
                        root.destroy()
