import random
from Card import *

class Board:
    def __init__(self):
        color_list = open("./color_list.txt", "r")
        word_list = open("./word_list.txt", "r")
        needed_colors = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "red", "red", "red", "red",
                         "red", "red", "red", "red", "beige", "beige", "beige", "beige", "beige", "beige", "beige",
                         "beige", "black"]
        used_words = []
        self.cards = []
        for x in range(25):
            card_word = word_list.readline(random.randint(1, 1526)).strip()
            while card_word in used_words:
                card_word = word_list.readline(random.randint(1, 1526)).strip()
            used_words.append(card_word)
            card_color = color_list.readline().strip()
            i = 2
            while card_color not in needed_colors:
                card_color = color_list.readline()
                i+=1
            needed_colors.remove(card_color)
            print(needed_colors)
            self.cards.append(Card(card_color, card_word))

        for x in range(25):
            card_word = word_list.readline(random.randint(1, 1526))
            card_color = color_list.readline(0)

    def print_board(self):
        for i in range(0, 26):
            if self.cards[i].guessed is False:
                print(self.cards[i].word)
            else:
                print(self.cards[i].color)
            if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
                print("/t")
