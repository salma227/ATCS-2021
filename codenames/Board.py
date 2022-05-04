import random
from Card import *

class Board:
    def __init__(self):
        color_list = open("./color_list.txt", "r")
        word_list = open("./word_list.txt", "r")
        words = word_list.read().splitlines()

        needed_colors = ["BLUE", "BLUE", "BLUE", "BLUE", "BLUE", "BLUE", "BLUE", "BLUE", "RED", "RED", "RED", "RED",
                         "RED", "RED", "RED", "RED", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE", "BEIGE",
                         "BEIGE", "BLACK"]
        used_words = []
        self.cards = []
        for x in range(25):
            # getting the random card word
            card_word = words.pop(random.randint(0, (len(words)-1))) # Reads in that line
            while card_word in used_words:
                card_word = words.pop(random.randint(0, (len(words)-1)))
            used_words.append(card_word)

            # getting the color assigned
            card_color = needed_colors.pop(random.randint(0, (len(needed_colors)-1)))

            self.cards.append(Card(card_color, card_word))

    def print_board(self):
        # print out board with formatting
        for i in range(0, 25):
            if self.cards[i].guessed is False:
                if (len(self.cards[i].word) < 4):
                    print(self.cards[i].word, end="\t\t\t\t")
                elif (len(self.cards[i].word) < 8):
                    print(self.cards[i].word, end="\t\t\t")
                elif (len(self.cards[i].word) < 12):
                    print(self.cards[i].word, end="\t\t")
                else:
                    print(self.cards[i].word, end="\t")
            # if card already guessed, simply print out color
            else:
                print(self.cards[i].color, end="\t")
            if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
                print('\t')
