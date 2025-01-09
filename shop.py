import pygame


class Shop:
    def __init__(self, money):
        self.money = money
        self.screen = pygame.display.set_mode((1000, 600))
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load('image/shop.png')
        self.items = [
            {"name": "Item 1", "price": 100, "rect": pygame.Rect(230, 80, 100, 100)},
            {"name": "Item 2", "price": 200, "rect": pygame.Rect(485, 80, 100, 100)},
            {"name": "Item 3", "price": 300, "rect": pygame.Rect(740, 80, 100, 100)},
            {"name": "Item 4", "price": 100, "rect": pygame.Rect(230, 350, 100, 100)},
            {"name": "Item 5", "price": 200, "rect": pygame.Rect(485, 350, 100, 100)},
            {"name": "Item 6", "price": 300, "rect": pygame.Rect(740, 350, 100, 100)},
        ]
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        for item in self.items:
            button_rect = pygame.Rect(item["rect"].x + 10, item["rect"].y + 170, 80, 40)
            buttons.append((button_rect, item))
        return buttons

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        for item in self.items:
            pygame.draw.rect(self.screen, (0, 0, 255), item["rect"])
            self.draw_text(f"{item['name']} - {item['price']}", item["rect"].x, item["rect"].y + 120)
        for button_rect, _ in self.buttons:
            pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
            self.draw_text("Buy", button_rect.x + 15, button_rect.y + 10)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_surface1 = self.font.render(f'money:{self.money}', True, (0, 0, 0))
        self.screen.blit(text_surface, (x, y))
        self.screen.blit(text_surface1, (10, 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button_rect, item in self.buttons:
                if button_rect.collidepoint(event.pos):
                    print(f"Bought {item['name']} for ${item['price']}")
