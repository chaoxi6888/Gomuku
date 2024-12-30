class CardChoice:
    def __init__(self, card, choice):
        self.card = card
        self.choice = choice

    def __str__(self):
        return f"{self.card} {self.choice}"