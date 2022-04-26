import random
from Card import *

class Board:
    def __init__(self):
        used_colors = ""
        used_words = ""
        self.cards = []
        for x in range(25):
            card_word = list.readline(random.randint(1, 1526))
            while card_word in used_words:
                card_word = list.readline(random.randint(1, 1526))
            used_words.append(card_word)
            card_color = list.readline(0)
            self.cards.append(Card(card_color, card_word))


        for x in range(25):
            card_word = list.readline(random.randint(1, 1526))
            card_color = list.readline(0)
