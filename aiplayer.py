import random  
from player import Player

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """Initializes player atributes
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ Returns a string representation of the object
        """
        return "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
    
    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score
        """
        max_score = max(scores)
        indices = [i for i in range(len(scores)) if scores[i] == max_score]
        if self.tiebreak == "LEFT":
            return indices[0]
        elif self.tiebreak == "RIGHT":
            return indices[-1]
        else:
            return random.choice(indices)
        
    def scores_for(self, b):
        """ returns a list of scores one for each col in board b 
        """
        scores = [50] * b.width
        for col in range(b.width):
            if not b.can_add_to(col):
               scores[col] = -1
            elif b.is_win_for(self.checker) or b.is_win_for(self.opponent_checker()):
               if b.is_win_for(self.checker):
                   scores[col] = 100
               else:
                   scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                AIOpponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = AIOpponent.scores_for(b)
                col_opp_score = max(opp_scores)
                if col_opp_score == 0:
                    scores[col] = 100
                elif col_opp_score == 100:
                    scores[col] = 0
                elif col_opp_score == 50:
                    scores[col] = 50
                else:
                    scores[col] = col_opp_score
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ Get a AI selected/predicted next move for this player that is valid
            for the board b.
        """
        self.num_moves+=1
        return self.max_score_column(self.scores_for(b))