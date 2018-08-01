# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:04:06 2018

@author: shane
"""

from board import Board
import random


class Random():
    def __init__(self, board_state):
        self.board_state = board_state
        
    def play(self):
        #return a random move from all available moves
        return random.choice(self.board_state.get_valid_moves())

#greedy will always assume it is black. to process white, pass in an inverted board
class Greedy():
    def __init__(self, board_state):
        self.turn = 'black'
        self.board_state = board_state
        
    def play(self):
        #find highest scoring moves
        moves = self.weigh_moves()
        
        #return a random move from chosen set
        return random.choice(moves)
        
    
    def weigh_moves(self):
        max_score = 0
        moves = []
        
        #select moves that rank the best in the scoring function
        for move in self.board_state.get_valid_moves(self.turn):
            #advance the board by action
            stepped_board = self.step_state(move)
            
            #score the new state 
            score = self.score_state(stepped_board)
            if score > max_score:
                max_score = score
                moves = [move]
            elif score == max_score:
                moves.append(move)
            
        return moves
        

        
    #assume that action is a tuple for row and coordinate to place piece
    def step_state(self, action):
        #make a copy of the board to analyse
        board_copy = self.board_state.get_copy()
        
        #make the action on the copied board
        board_copy.place_piece(action[0], action[1], self.turn)
        
        return board_copy
    
    #score the function as point difference
    def score_state(self, state):
        return state.get_score()[1] - state.get_score()[0]
    
class Human():
    def __init__(self, board_state):
        self.board_state = board_state
        
    def play(self):
        move = self.get_input()
        return move
    
    def get_input(self):
        prompt = True
        while prompt:
            prompt = self.prompt_input()
        return prompt
        
    def prompt_input(self):
        command = input('Enter co-ordinates to place piece:')
        #quit command as long as command begins with q
        if len(command) < 1:
            print('Illegal command registered!')
            return True
        elif command[0] == 'q':
            return False
        
        else:
            try:
                row = ord(command[0].upper()) - 65
                col = int(command[1:]) - 1
                
                #bound checking for input
                assert row >= 0 and row < 8
                assert col >= 0 and col < 8
                
                #returns false if no more valid moves left in game
                return row, col
                
            except:
                print('Error in co-ordinates input!')
        return True