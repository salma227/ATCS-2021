import random
import time

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe! First player to get three in a row wins!")
        return

    def print_board(self):
        # TODO: Print the board
        print("\t0\t1\t2")
        i = 0
        for a in self.board:
            print(i, "\t", end="")
            i = i+1
            for b in a:
                print(b, "\t",  end="")
            print("")

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row > 2 or row < 0:
            return False
        if col > 2 or col < 0:
            return False
        if self.board[row][col] == '-':
            return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        while True:
            r = int(input("Enter row: "))
            c = int(input("Enter column: "))
            valid = self.is_valid_move(r, c)
            if valid:
                break
            print("Please enter valid move.")

        self.place_player(player, r, c)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        # sets AI minimax depth to 2
        if player == 'O':
            self.take_minimax_alpha_beta_turn(player, 2)
        else:
            self.take_manual_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win
        count = 0
        for i in range(3):
            for n in range(3):
                if self.board[n][i] == player:
                    count = count + 1
            if count == 3:
                return True
            count = 0
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        count = 0
        for a in self.board:
            for b in a:
                if b == player:
                    count = count + 1
            if count == 3:
                return True
            count = 0
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        count = 0
        for i in range(3):
            if self.board[i][i] == player:
                count = count + 1
        if count == 3:
            return True
        count = 0
        for a in range(3):
            if self.board[a][2-a] == player:
                count = count + 1
        if count == 3:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_col_win(player):
            return True
        if self.check_row_win(player):
            return True
        if self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        for a in self.board:
            for b in a:
                if b == '-':
                    return False
        if self.check_win('X'):
            return False
        if self.check_win('O'):
            return False
        return True

    def take_random_turn(self, player):
        while True:
            r = random.randint(0, 3)
            c = random.randint(0, 3)
            valid = self.is_valid_move(r, c)
            if valid:
                break
        self.place_player(player, r, c)

    def take_minimax_turn(self, player, depth):
        start = time.time()
        score, row, col = self.minimax(player, depth)
        end = time.time()
        self.place_player(player, row, col)
        print("This turn took: ", end-start, " seconds")

    def take_minimax_alpha_beta_turn(self, player, depth):
        start = time.time()
        score, row, col = self.minimax_alpha_beta(player, depth, -100, 100)
        end = time.time()
        self.place_player(player, row, col)
        print("This turn took: ", end - start, " seconds")

    def play_game(self):
        # TODO: Play game
        gameGoing = True
        player = 'X'
        self.print_instructions()
        self.print_board()
        while gameGoing:
            self.take_turn(player)
            self.print_board()
            if self.check_win(player):
                print(player , " won!")
                break
            if self.check_tie():
                print("You tied!")
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

        print("GAME OVER")

    def minimax(self, player, depth):
        opt_row = -1
        opt_col = -1
        if self.check_win("O"):
            return 10, None, None
        elif self.check_tie():
            return 0, None, None
        elif self.check_win("X"):
            return -10, None, None
        elif depth == 0:
            return 0, None, None
        if player == "O":
            best = -100
            for r in range(3):
                for c in range (3):
                    if self.board[r][c] == '-':
                        self.place_player("O", r, c)
                        score = self.minimax("X", depth-1)[0]
                        if best < score:
                            best = score
                            opt_row = r
                            opt_col = c
                        self.place_player('-', r, c)
            return best, opt_row, opt_col
        if player == "X":
            worst = 100
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == '-':
                        self.place_player("X", r, c)
                        score = self.minimax("O", depth-1)[0]
                        if worst > score:
                            worst = score
                            opt_row = r
                            opt_col = c
                        self.place_player('-', r, c)
            return worst, opt_row, opt_col

    def minimax_alpha_beta(self, player, depth, alpha, beta):
        opt_row = -1
        opt_col = -1
        if self.check_win("O"):
            return 10, None, None
        elif self.check_tie():
            return 0, None, None
        elif self.check_win("X"):
            return -10, None, None
        elif depth == 0:
            return 0, None, None
        if player == "O":
            best = -100
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == '-':
                        self.place_player("O", r, c)
                        score = self.minimax("X", depth-1)[0]
                        alpha = max(alpha, score)
                        if best < score:
                            best = score
                            opt_row = r
                            opt_col = c
                        if alpha >= beta:
                            return best, opt_row, opt_col
                        self.place_player('-', r, c)
            return best, opt_row, opt_col
        if player == "X":
            worst = 100
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == '-':
                        self.place_player("X", r, c)
                        score = self.minimax("O", depth-1)[0]
                        beta = max(beta, score)
                        if worst > score:
                            worst = score
                            opt_row = r
                            opt_col = c
                        if alpha >= beta:
                            return worst, opt_row, opt_col
                        self.place_player('-', r, c)
            return worst, opt_row, opt_col
