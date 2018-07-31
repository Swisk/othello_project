from tile import Tile
from board import Board

class UI:
    def __init__(self):
        self._board = Board()
        self.print_board()
        self.print_score()

    @property
    def board(self):
        return self._board

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
                if tile.piece_color == 'white':
                    char = 'o'
                elif tile.piece_color == 'black':
                    char = 'x' 
                else:
                    char = '-'
                print(' {} |'.format(char), end = '')
            print('')
            #print('  |   |   |   |   |   |   |   |   |')
            print('  +---+---+---+---+---+---+---+---+')
        

def test():
    test_UI = UI()

if __name__ == '__main__':
    test()