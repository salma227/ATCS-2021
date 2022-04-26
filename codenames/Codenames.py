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
