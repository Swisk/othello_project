from tile import Tile
from board import Board
import random

class UI:
    def __init__(self):
        self._board = Board()
        self._turn = 'black'
        
        

    @property
    def board(self):
        return self._board

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, val):
        if val == 'white' or val == 'black':
            self._turn = val

    #print the current score
    def print_score(self):
        score = self.board.get_score()
        print('Current Score is White: {}, Black: {}'.format(score[0], score[1]))

    #print the board
    def print_board(self):
        print('    1   2   3   4   5   6   7   8')
        print('  +---+---+---+---+---+---+---+---+')
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']
        for row in range(8):
            #('  |   |   |   |   |   |   |   |   |')
            #need to iterate over tile objects
            print(letters[row], end = ' |')
            for tile in self.board.tile_array[row]:
                if tile.piece_color() == 'white':
                    char = 'o'
                elif tile.piece_color() == 'black':
                    char = 'x' 
                else:
                    char = '-'
                print(' {} |'.format(char), end = '')
            print('')
            #print('  |   |   |   |   |   |   |   |   |')
            print('  +---+---+---+---+---+---+---+---+')
        print("Its {}'s turn to move!".format(self.turn.title()))

    #place piece
    def place_piece(self, row, col, color):
        self.board.place_piece(row, col, color)

    #control user input
    def control_state(self):
        command = input('Enter co-ordinates to place piece:')
        #quit command as long as command begins with q
        if command[0] == 'q':
            return False
        else:
            try:
                row = ord(command[0].upper()) - 65
                col = int(command[1]) - 1

                #need error handling if piece is placed wrongly
                self.board.place_piece(row, col, self.turn)
                if self.turn == 'white':
                    self.turn = 'black'
                elif self.turn == 'black':
                    self.turn = 'white'
                self.print_board()
            except:
                print('Error in co-ordinates input!')
                self.control_state()
        return True

    def start(self):
        cont = True
        while cont:
            self.print_board()
            self.print_score()
            cont = self.control_state()
        

def test():
    test_UI = UI()
    test_UI.start()

if __name__ == '__main__':
    test()