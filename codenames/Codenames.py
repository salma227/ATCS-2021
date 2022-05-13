# 5/10/2022
# Salma Siddiqui

from Board import *

from nltk.corpus import wordnet as wn
from itertools import product


class Codenames:
    def __init__(self):
        self.players = 0  # stretch goal, solitaire or multiplayer play
        self.codeword = ""  # console input codeword, changes every round
        self.num_cards = 0  # number of cards in play, changes every round
        self.answer_cards = []  # corresponding cards from the board, changes every round
        self.guesses = []  # current AI guesses, changes every round
        self.still_playing = True

    def print_instructions(self):  # print instructions for how to play the game
        print("Welcome to Codenames!")
        print("Each word on the board has an assigned color! Red will score you points, beige is neutral, and black "
              "will end the game and you lose! ")
        print("You are the SPYMASTER. You will be giving your AI guesser, JUDI, a codeword that corresponds to certain "
              "words on the board.")
        print("You can make your codeword correspond to as many words on the board as you'd like, ")
        print("just remember that JUDI will be looking for the words with the most similarity.")
        print("After JUDI guesses a word, it will disappear from the board.")
        print("You want JUDI to guess all the red words with as few turns as possible.")
        print("Good luck!")
        print('\n\n\n')

    def take_manual_turn(self, board):  # get input from the console SPYMASTER
        # SPYMASTER turn, always first
        self.codeword = input("SPYMASTER! Enter codeword: ")  # get codeword
        while self.codeword in board.used_words:  # make sure it isn't a word from the board
            self.codeword = input("Code word cannot be present on the board! Enter VALID codeword: ")
        self.num_cards = int(input("Enter number of words: "))  # set instance variable for how many cards are in play
        # get the corresponding words from the console
        for i in range(0, self.num_cards):  # (don't actually use these words, but would need for stretch goals)
            a_card = input("Enter one corresponding word from the board: ")
            while a_card not in board.used_words:
                a_card = input("Enter one VALID corresponding word from the board: ")
            self.answer_cards.append(a_card)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    def take_AI_turn(self, board): # the AI player (Judi)'s turn
        guesses_dict = {}
        # similarity code adapted from user alvas, September 18, 2013 (stackOverflow)
        for x in range(0, len(board.cards)):
            board_word_s, code_word_s = wn.synsets(board.cards[x].word), wn.synsets(self.codeword)
            maxscore = 0
            for i, j in list(product(*[code_word_s, board_word_s])):
                score = i.wup_similarity(j)  # Wu-Palmer Similarity
                # set maxscore equal to that card's similarity to the code word
                maxscore = score if maxscore < score else maxscore
            # add that similarity score and card word to guesses_dict
            guesses_dict[board.cards[x].word] = maxscore
        # sort the dictionary from greatest to lowest similarity score
        sorted_guesses_dict = sorted(guesses_dict.items(), key=lambda x: x[1], reverse=True)

        # clear self.guesses of previous turn's guesses
        self.guesses = []
        # loop through for num_cards the codeword corresponds to (ie number of guesses Judi can make)
        for i in range(0, self.num_cards):
            self.guesses.append(sorted_guesses_dict[i][0])
        print("JUDI: Hmmmm.... ", self.codeword, "?")
        print("My guesses are:")
        for b in self.guesses:
            print(b)  # print guesses (word on card)
        print("")

    def update_board(self, board):  # sets guessed cards on the board to empty, guessed strings
        for i in self.guesses:
            for x in range(len(board.cards)):
                if board.cards[x].word == i:
                    board.cards[x].guessed = True
                    board.cards[x].word = ""

    def check_lose(self, board):  # check if BLACK card has been guessed yet
        for x in range(len(board.cards)):
            if board.cards[x].guessed == True and board.cards[x].color == "BLACK":
                return True
        return False

    def check_win(self, board):  # check if there are unguessed RED cards left
        for i in range(len(board.cards)):
            if board.cards[i].color == "RED" and board.cards[i].guessed == False:
                return False
        return True

    def play_game(self):  # executes manual and AI turns until game is over
        board = Board()
        board.print_board()
        while self.still_playing is True:
            self.take_manual_turn(board)
            self.take_AI_turn(board)
            self.update_board(board)
            board.print_board()
            if self.check_win(board) is True:
                print("YOU'VE WON! CONGRATS! :o)")
                self.still_playing = False
            elif self.check_lose(board) is True:
                print("Bummer! JUDI guessed the black card! You lose! :(")
                print("Better luck next time!")
                self.still_playing = False
