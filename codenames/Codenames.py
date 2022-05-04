import random

class Codenames:
    def __init__(self):
        self.players = 0

    def print_instructions(self):
        print("Welcome to Codenames!")
        return

    def print_board(self, board):
        for a in board:
            for b in a:
                print(board[a][b], "\t",  end="")
            print("")

    def take_turn(self):
        while True:
            codeword = int(input("SPYMASTER! Enter codeword: "))
            num_cards = int(input("Enter number of words: "))
            answer_cards = []
            a_card = int(input("Enter one corresponding word: "))
            answer_cards.append(a_card)
            if num_cards > 1:
                for i in range(1, num_cards):
                    a_card = int(input("Enter one corresponding word: "))
                    answer_cards.append(a_card)
            #valid = self.is_valid_move()
            #if valid:
            #    break
            #print("Please enter valid move.")
        #self.claim_card(_____, r, c)

    #def is_valid_move(self, color):
    #    return True
    #    return False

    #def claim_card(self, color, word, board):
    #    if board.cards[]:

