
class Board:
    def __init__(self, height, width):
        """ Initilaize board atributes
        """
        self.width = width
        self.height = height
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         

        for row in range(self.height):
            s += '|'  

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n' 

        for hyphen in range((self.width * 2) + 1):
            s+="-"
        s+='\n'
        s+=" "
        for num_col in range(self.width):
            s+=str(num_col % 10) + " "
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)

        row = self.height - 1
        while self.slots[row][col] != ' ' and row > 0:
            row -= 1
        self.slots[row][col] = checker

    
    def reset(self):
        """ Clears the entire board
        """
        self.slots = [[' '] * self.width for row in range(self.height)]
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X' 

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ Checks if you can add a checker to specified column
        """
        if 0 <= col < self.width:
           for row in range(self.height):
               if self.slots[row][col] == ' ':
                   return True
           return False
        else:
            return False
        
    def is_full(self):
        """ Returns True if the board is full with checkers
        """
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True
    
    def remove_checker(self, col):
        """ Removes the top checker from specified column
        """
        if 0 <= col < self.width:
            for row in range(self.height):
                if self.slots[row][col] != ' ':
                    self.slots[row][col] = ' '
                    break;
                    
    def is_win_for(self, checker):
        """ Checks if the plaayer with specified checker wins
        """
        assert(checker == 'X' or checker == 'O')
        return self.is_horizontal_win(checker) or \
            self.is_vertical_win(checker) or \
            self.is_down_diagonal_win(checker) or \
            self.is_up_diagonal_win(checker)
        
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
        
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a down diaganol win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True  
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True     
        return False
    
    
    
                
            