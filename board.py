import random

class Board:
    '''
    Board class for the tictactoe Game.
    Holds functionality of placing elements and checking wins
    '''
    def __init__(self, arr=[]):
        '''Init'''
        self.arr = arr

    def __repr__(self):
        '''Represents in the board in this manner. 
            |O|.|.|
            |.|.|.|
            |.|X|.|
        which makes it readble to the user.'''
        board = ''
        for i in range(len(self.arr)):
            line = ''
            for e in range(len(self.arr[i])):
                line = line + "|" + self.arr[i][e]
            line += "|"
            board += line + "\n"
        return board
    
    def get_arr(self):
        '''Returns the boards 2D array.'''
        return self.arr

    def board_is_full(self):
        '''Checks if the board is full with pieces.'''
        checker = True
        for inner in self.arr:
            for el in inner:
                if el == '.':
                    checker = False
        return checker
    
    def replace_element(self, symbol, row, column):
        '''Replaces an element on the masterboard'''

        if self.arr[row - 1][column - 1] == '.':
            self.arr[row - 1][column - 1] = symbol
        else:
            print('Spot full, please choose another spot.')
    
    def remove_element(self, row, column):
        '''Removes an existing elemet from the masterboard'''
        
        if self.arr[row - 1][column -1] != '.':
            self.arr[row - 1][column - 1] = '.'
        else:
            print('This spot is already empty.')
    
    def check_win(self):
        '''Checks if there is a win!'''
        arr = self.arr
        if arr[0][0] == arr[0][1] == arr[0][2] != '.':
            return arr[0][0]
        elif arr[1][0] == arr[1][1] == arr[1][2] != '.':
            return arr[1][0]
        elif arr[2][0] == arr[2][1] == arr[2][2] != '.':
            return arr[2][0]
        elif arr[0][0] == arr[1][0] == arr[2][0] != '.':
            return arr[0][0]
        elif arr[0][1] == arr[1][1] == arr[2][1] != '.':
            return arr[0][1]
        elif arr[0][2] == arr[1][2] == arr[2][2] != '.':
            return arr[0][2]
        elif arr[0][0] == arr[1][1] == arr[2][2] != '.':
            return arr[0][0]
        elif arr[0][2] == arr[1][1] == arr[2][0] != '.':
            return arr[0][2]
        else:
            return '.'
    
    def find_empty_spots(self):
        '''Finds all the empty spots on the 
        board and returns a list of tuples of 
        such spaces'''
        lst = []
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.arr[i][j] == ".":
                    lst.append((i+1, j+1))
        return lst

    def random_placement(self, symbol):
        '''Replaces Random element'''
        checker = True
        while checker:
            first = random.randint(0,2)
            second = random.randint(0,2)
            if self.arr[first][second] == ".":
                self.replace_element(symbol, first+1, second+1)
                checker = False
            