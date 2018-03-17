class Board:
    def __init__(self, height, width):
        """class constructor"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
        a = self.width + (self.width + 1)
        s += "-" * a
        s += "\n"
        for i in range(self.width):
            s += " "
            s += str(i%10)

        return s

    def add_checker(self, checker, col):
        """ Fuctions adds one checker on the board to the col column
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while row <= (self.height-1) and self.slots[row][col] == " ":
            row += 1
        self.slots[row-1][col] = checker

    def reset(self):
        """Function resets the board"""
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
                # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """Functions checks if player can add a checker to coloumn col"""
        if 0 <= col < self.width and self.slots[0][col] == " ":
            return True
        else:
            return False
            
    def is_full(self):
        """Function checks if the board is completely full or not"""
        if " " not in self.slots[0]:
            return True
        else:
            return False

    def remove_checker(self, col):
        """Function removes top checker from one column"""
        row = 0
        while row <= (self.height-2) and self.slots[row][col] == " ":
            row += 1
        self.slots[row][col] = " "

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
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
        """ Checks for a diagonal(down) win for the specified checker.
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
        """ Checks for a diagonal(up) win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ Fucntion checks if "checker" player won the game or not
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) or \
           self.is_vertical_win(checker) or \
           self.is_down_diagonal_win(checker) or \
           self.is_up_diagonal_win(checker):
            return True
        else:
            return False



