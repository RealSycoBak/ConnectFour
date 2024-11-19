class Player:
    """ Player in C4
    """
    def __init__(self, checker):
        """ Initializes objects atributes
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    
    def __repr__(self):
        """ Returns a string representation of the object
        """
        return "Player " + self.checker
    
    
    def opponent_checker(self):
        """ Returns opponents checker
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ Get a next move for this player that is valid
            for the board b.
        """
        self.num_moves+=1
        while True:
            column = int(input("Enter a column: "))
            if b.can_add_to(column):
                return column
            print("Try again!")
            
    