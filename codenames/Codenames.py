import random
from Card import *
from Board import *

from nltk.corpus import wordnet as wn
from itertools import product

class Codenames:
    def __init__(self):
        self.players = 0
        self.codeword = ""
        self.num_cards = 0
        self.answer_cards = []
        self.guesses = []
        self.still_playing = True

    def print_instructions(self):
        print("Welcome to Codenames!")
        print("Each word on the board has an assigned color! Red will score you points, beige is neutral, and black "
              "will end the game and you lose! ")
        print("you are the SPYMASTER. You will be giving your AI guesser, JUDI, a codeword that corresponds to certain "
              "words on the board.")
        print("You can make your codeword correspond to as many words on the board as you'd like")
        print("just remember that JUDI will be looking for the words with the most similarity.")
        print("You want your guesser to guess all the red words with as few turns as possible.")
        print("Good luck!")
        print('\n\n\n')

    def take_manual_turn(self, board):
        # SPYMASTER turn, always first
        self.codeword = input("SPYMASTER! Enter codeword: ")
        while self.codeword in board.used_words:
            self.codeword = input("Code word cannot be present on the board! Enter VALID codeword: ")
        self.num_cards = int(input("Enter number of words: "))
        for i in range(0, self.num_cards):
            a_card = input("Enter one corresponding word from the board: ")
            while a_card not in board.used_words:
                a_card = input("Enter one VALID corresponding word from the board: ")
            self.answer_cards.append(a_card)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


    def take_AI_turn(self, board):
        similarity_scores = []
        guesses_dict = {}
        for x in range(0, len(board.cards)):
            board_word_s, code_word_s = wn.synsets(board.cards[x].word), wn.synsets(self.codeword)
            maxscore = 0
            for i, j in list(product(*[code_word_s, board_word_s])):
                score = i.wup_similarity(j)  # Wu-Palmer Similarity
                maxscore = score if maxscore < score else maxscore
            similarity_scores.append(maxscore)
            guesses_dict[board.cards[x].word] = maxscore
        similarity_scores.sort()
        similarity_scores.reverse()

        sorted_guesses_dict = sorted(guesses_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(0, self.num_cards):
            self.guesses = []
            print(sorted_guesses_dict[i][0])
            self.guesses.append(sorted_guesses_dict[i][0])
        print("JUDI: Hmmmm.... ", self.codeword, "?")
        print("My guesses are:")
        for b in self.guesses:
            print(b)

    def update_board (self, board):
        for i in self.guesses:
            board.cards[i].guessed = True

    def check_lose(self, board):
        for i in range(len(self.guesses)):
            if board.cards[i].guessed is True and board.cards[i].color == "BLACK":
                return True
            return False

    def check_win(self, board):
        for i in range(len(board.cards)):
            if board.cards[i].color == "RED":
                return False
        return True


    def play_game(self):
        board = Board()
        board.print_SPYMASTER_board()
        while self.still_playing is True:
            self.take_manual_turn(board)
            board.print_board()
            self.take_AI_turn(board)
            board.print_SPYMASTER_board()
            if self.check_win(board) is True:
                print("You've won! Congrats!")
                self.still_playing is False
            elif self.check_lose(board) is True:
                print("Judi guessed the black card! You lose!")
                self.still_playing is False
