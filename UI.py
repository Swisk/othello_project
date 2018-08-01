from tile import Tile
from board import Board
import random
from agent import *
import time

class UI:
    def __init__(self):
        self._board = Board()
        self._turn = random.choice(['black', 'white'])

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

    #control user input
    def control_state(self):
        command = input('Enter co-ordinates to place piece:')
        #quit command as long as command begins with q
        if len(command) < 1:
            print('Illegal command registered!')
            return True
        elif command[0] == 'q':
            return False
        
        #used for forcing weird game states in debugging
        elif command == 'pass':
            self.change_turn()
        else:
            try:
                row = ord(command[0].upper()) - 65
                col = int(command[1:]) - 1
                
                #bound checking for input
                assert row >= 0 and row < 8
                assert col >= 0 and col < 8
                
                #returns false if no more valid moves left in game
                return self.place_piece(row, col)
                
            except:
                print('Error in co-ordinates input!')
        return True
            
    
    def place_piece(self, row, col):
        #need error handling if piece is placed wrongly
        valid_turn = self.board.place_piece(row, col, self.turn)
        if valid_turn:
            self.change_turn()
            
            #if the current player has no legal moves, switch turns again
            if not self.board.get_valid_moves(self.turn):
                self.change_turn()
                
                #if no valid moves again, end the game
                if not self.board.get_valid_moves(self.turn):
                    return False
        else:
            print('Illegal co-ordinates input for current player!')
            
        return True

    def ai_handler(self):
        move = Greedy(self.board).play()
        if move:
            print('AI is thinking...')
            time.sleep(random.uniform(1, 3))
            self.place_piece(move[0], move[1])
        
    def change_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        elif self.turn == 'black':
            self.turn = 'white'
    
    def start(self):
        self.board.setup_board()
        self.print_board()
        self.print_score()
        cont = True
        while cont:
            if self.turn == 'black':
                self.ai_handler()
            elif self.turn == 'white':
                cont = self.control_state()
            self.print_board()
            self.print_score()
        self.print_board()
        self.print_score()
        

def test():
    test_UI = UI()
    test_UI.start()

if __name__ == '__main__':
    test()