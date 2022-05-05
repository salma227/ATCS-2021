import random
from nltk.corpus import wordnet as wn
from itertools import product

class Codenames:
    def __init__(self):
        self.players = 0
        self.codeword = ""
        self.num_cards = 0
        self.answer_cards = []
        self.guesses = []

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
        while True:
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
        similarity_scores = [4, 5, 6, 2, 1]
        wordx, wordy = "cat", "dog"
        for x in range (0, len(board.cards)):
            code_word_s, board_word_s = wn.synsets(board.cards[x].word), wn.synsets(self.codeword)
            maxscore = 0
            for i, j in list(product(*[code_word_s, board_word_s])):
                score = i.wup_similarity(j)  # Wu-Palmer Similarity
                maxscore = score if maxscore < score else maxscore
            similarity_scores.append(maxscore)
        similarity_scores.sort()
        similarity_scores.reverse()
        for i in range(0, self.num_cards):
            self.guesses.append(similarity_scores[i])
        print("JUDI: Hmmmm....")
        print("My guesses are:")
        for b in self.guesses:
            print(b)
