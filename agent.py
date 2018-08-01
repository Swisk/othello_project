# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:04:06 2018

@author: shane
"""

from board import Board
import random

#agent will always assume it is black. to process white, pass in an inverted board
class Agent():
    def __init__(self, board_state):
        self.turn = 'black'
        self.board_state = board_state

    def weigh_moves(self):
        max_score = 0
        moves = []
        
        #select moves that rank the best in the scoring function
        for move in self.board_state.get_valid_moves():
            #advance the board by action
            stepped_board = self.step_state(move)
            
            #score the new state 
            score = self.score_state(stepped_board)
            if score > max_score:
                max_score = score
                moves = [move]
            elif score == max_score:
                moves.append(move)
            
        #return a random move from chosen set
        return random.choice(moves)

        
    #assume that action is a tuple for row and coordinate to place piece
    def step_state(self, action):
        #make a copy of the board to analyse
        board_copy = self.board_state.get_copy()
        
        #make the action on the copied board
        board_copy.place_piece(action[0], action[1], self.turn)
        
        return board_copy
    
    #greedy
    #score the function as point difference
    def score_state(self, state):
        return state.get_score()[1] - state.get_score()[0]
    
    #random
    #all moves are ranked equally
#    def score_state(self, state):
#        return 1
    