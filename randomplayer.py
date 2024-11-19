import random
from player import Player

class RandomPlayer(Player):
    def next_move(self, b):
        """ Get a random next move for this player that is valid
            for the board b.
        """
        self.num_moves+=1
        valid_columns = [col for col in range(b.width) if b.can_add_to(col)]
        return random.choice(valid_columns)