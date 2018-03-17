#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game 
#   

from Board import *
from Player import *
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """Function makes one move specified by a human player"""
    c = player.__repr__()
    print(c, "'s turn")
    move = player.next_move(board)
    board.add_checker(player.checker, move)
    print()
    print(board)
    if board.is_win_for(player.checker):
        i = player.num_moves
        print(player.__repr__(), "wins in ", i, "moves")
        print("Congratulations!")
        return True
    elif board.is_full() and not board.is_win_for(player.checker):
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    
    def next_move(self, board):
        """Function makes a random move on the board"""
        lc = [x for x in range(board.width) if board.can_add_to(x)]
        column = random.choice(lc)
        self.num_moves += 1
        return column











    




