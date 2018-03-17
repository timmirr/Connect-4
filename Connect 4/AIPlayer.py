#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from Player import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ class constructor
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """Function shows the settings for AI Player"""
        c = "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
        return c

    def max_score_column(self, scores):
        """Function shows the columns with max score"""
        m = max(scores)
        lc = []
        for i in range(len(scores)):
            if scores[i] == m:
                lc += [i]
        if len(lc) > 1:
            if self.tiebreak == "LEFT":
                column = lc[0]
            elif self.tiebreak == "RIGHT":
                column = lc[-1]
            else:
                column = random.choice(lc)
            return column
        else:
            return lc[0]

    def scores_for(self, board):
        """Function recursively calculates the scores for each move"""
        scores = [1]*board.width
        for i in range(board.width):
            if not board.can_add_to(i):
                scores[i] = -1
            elif board.is_win_for(self.checker):
                scores[i] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                board.add_checker(self.checker, i)
                other = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                other_scores = other.scores_for(board)
                if max(other_scores) == 100:
                    scores[i] = 0
                elif max(other_scores) == 50:
                    scores[i] = 50
                elif max(other_scores) == 0:
                    scores[i] = 100
                board.remove_checker(i)
        return scores

    def next_move(self, board):
        """Function does the best move for AI Player"""
        scores = self.scores_for(board)
        self.num_moves += 1
        return self.max_score_column(scores)










                
