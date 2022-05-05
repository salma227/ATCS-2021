from Codenames import *
from Board import *

game = Codenames()
board = Board()
game.print_instructions()
board.print_SPYMASTER_board()
game.take_manual_turn(board)

