#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#  

from Board import *

# write your class below

class Player:
    def __init__(self, checker):
        """class constructor"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """Function show what checker does player play with"""
        c = "Player " + str(self.checker)
        return c
    
    def opponent_checker(self):
        """Function shows the opponent checker"""
        if self.checker == "X":
            c = "O"
        else:
            c = "X"
        return c

    def next_move(self, board):
        """Fuctions does one specific move in the game"""
        move = int(input("Enter a colomn: "))
        if 0 <= move < board.width:
            self.num_moves += 1
            return move
        else:
            print("Try a different column number")
            return self.next_move(board)












