# 5/10/2022
# Salma Siddiqui

import random
from Card import *


class Board:
    def __init__(self):  # constructs a game board and fills with cards
        word_list = open("./word_list.txt", "r")
        words = word_list.read().splitlines()
        needed_colors = ["RED", "RED", "RED", "RED", "RED", "RED", "RED", "RED", "RED", "RED", "RED", "RED",
                         "RED", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BLACK",
                         "BLACK", "BLACK"]
        self.used_words = []  # the words on the board
        self.cards = []  # the cards on the board
        for x in range(25):
            # getting the random card word
            card_word = words.pop(random.randint(0, (len(words)-1)))
            while card_word in self.used_words:
                card_word = words.pop(random.randint(0, (len(words)-1)))
            self.used_words.append(card_word)

            # getting the random assigned color
            card_color = needed_colors.pop(random.randint(0, (len(needed_colors)-1)))

            self.cards.append(Card(card_color, card_word))

    def print_board(self):  # print out board with formatting (diff tab #s for longer or shorter words)
        for i in range(0, 25):
            if self.cards[i].guessed is False:
                if len(self.cards[i].word) < 4:
                    print(self.cards[i].word, end="\t\t\t\t")
                elif len(self.cards[i].word) < 8:
                    print(self.cards[i].word, end="\t\t\t")
                elif len(self.cards[i].word) < 12:
                    print(self.cards[i].word, end="\t\t")
                else:
                    print(self.cards[i].word, end="\t")
            # if card already guessed, print out '---'
            else:
                print("---", end="\t\t\t\t")
            # if need new line
            if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
                print('\t')
                for n in range(i-4, i+1):
                    if len(self.cards[n].color) < 4:
                        print(self.cards[n].color, end="\t\t\t\t")
                    elif len(self.cards[n].color) < 8:
                        print(self.cards[n].color, end="\t\t\t")
                    elif len(self.cards[n].color) < 12:
                        print(self.cards[n].color, end="\t\t")
                    else:
                        print(self.cards[n].color, end="\t")
                print('\t')
                print('\t')
                print('\t')