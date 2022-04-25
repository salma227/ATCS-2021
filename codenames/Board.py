import random


class Board:
    def __init__(self, cards):
        self.words = 1

    def create_cards(self):
        list_of_words = open('word_list.txt', 'r')
        list_of_colors = open('color_list.txt', 'r')
        for x in range(25):
            card_word = list.readline(random.randint(1, 1526))
            card_color = list.readline(0)