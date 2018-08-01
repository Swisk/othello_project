from tile import Tile

class Board:
    def __init__(self):
        self._tile_array = [[Tile() for col in range(8)] for row in range(8)]

    #getter
    @property
    def tile_array(self):
        return self._tile_array
    
    def setup_board(self):
        #manually place starting pieces
        self._tile_array[3][3].place_piece('white')
        self._tile_array[4][4].place_piece('white')
        self._tile_array[3][4].place_piece('black')
        self._tile_array[4][3].place_piece('black')

    def check_valid_coord(self, row, col, color):
        #return true if there are valid intermediate tiles
        if self.get_intermediate(row, col, color):
            return True
        return False
        
    def place_piece(self, row, col, color):
        #check if piece is appropriate before placing
        if self.check_valid_coord(row, col, color):
            self.tile_array[row][col].place_piece(color)
            
            #flip all intermediate pieces
            for intermediate_tile in self.get_intermediate(row, col, color):
                intermediate_tile.flip_piece()
            return True
        return False

    
    def get_intermediate(self, row, col, color):
        #create list of all modifications to row, check_ tuple
        directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        #create output list of all intermediate tiles
        output = []

        #check only if tile is empty
        if not self.tile_array[row][col].isempty():
            for dir in directions:
                check_row = row + dir[0]
                check_col = col + dir[1]
                dir_arr = []

                #skip over directions that lead out of bounds
                if check_row < 0 or check_row >= 8 or check_col < 0 or check_col >= 8:
                    continue

                else:
                    #if no piece there, invalid direction and move on
                    if self.tile_array[check_row][check_col].isempty():
                        continue

                    #if piece check_or is different from current piece, check if there is piece of player color 
                    #to create matching caps
                    elif self.tile_array[check_row][check_col].piece_color() != color:
                        #update search in the same direction as before until piece is found or out of bounds
                        #we update first to ensure loop conditions hold
                        #add current tile to array
                        dir_arr.append(self.tile_array[check_row][check_col])

                        #move to next tile in direction
                        check_row += dir[0]
                        check_col += dir[1]

                        while (check_row >= 0 and check_row < 8 and check_col >= 0 and check_col < 8):
                            if self.tile_array[check_row][check_col].isempty():
                                break
                            #add direction array to output only if direction is properly bounded
                            elif self.tile_array[check_row][check_col].piece_color() == color:
                                #add valid intermediate tiles to output array
                                output.extend(dir_arr)
                                #exit the loop for current direction
                                break

                            #add current tile to array
                            dir_arr.append(self.tile_array[check_row][check_col])

                            #move to next tile in direction
                            check_row += dir[0]
                            check_col += dir[1]
            
        return output
    
    #method to iterate over all tiles in the tile array
    def __iter__(self):
        for row in self.tile_array:
            for tile in row:
                yield tile

    #returns a tuple of white score and black score
    def get_score(self):
        white_score = 0
        black_score = 0
        for tile in self:
            if not tile.isempty():
                if tile.piece_color() == 'white':
                    white_score += 1
                elif tile.piece_color() == 'black':
                    black_score += 1
                else:
                    print('error')
        return (white_score, black_score)
    

    #get board clone for AI
    def get_copy(self):
        new_board = Board()
        for row in range(8):
            for col in range(8):
                if self.tile_array[row][col].isempty():
                    continue
                else:
                    color = self.tile_array[row][col].piece_color()
                    new_board.tile_array[row][col].place_piece(color)
        return new_board
            
    #returns a list containing all posible move tuples
    def get_valid_moves(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                if self.check_valid_coord(row, col, color):
                    moves.append((row, col))
        return moves
   
def test():
    board = Board()
    """
    pieces manually placed
    - - - -
    - o x -
    - x o -
    - - - -
    """
    
    #test get_copy method
    board.setup_board()
    test_board = board.get_copy()
    
    

    #test get_score method and correspondingly __iter__
    assert test_board.get_score() == (2, 2)

    #test check_valid_coord and correspondingly get_intermediate method
    assert test_board.check_valid_coord(0, 0, "white") == False
    assert test_board.check_valid_coord(1, 1, "white") == False

    assert test_board.check_valid_coord(2, 2, "white") == False
    assert test_board.check_valid_coord(2, 2, "black") == False

    assert test_board.check_valid_coord(2, 3, "white") == False
    assert test_board.check_valid_coord(2, 3, "black") == True
    
    test_board.tile_array[6][6].place_piece('black')
    assert test_board.check_valid_coord(2, 2, "white") == False
    assert test_board.check_valid_coord(2, 2, "black") == False
    test_board.tile_array[6][6] = Tile()
    
    #test get_valid_moves method
    assert test_board.get_valid_moves('white') == [(2, 4), (3, 5), (4, 2), (5, 3)]
    assert test_board.get_valid_moves('black') == [(2, 3), (3, 2), (4, 5), (5, 4)]

    #test place_piece method
    assert test_board.place_piece(2, 3, 'black') == True
    assert test_board.tile_array[2][3].piece_color() == 'black'
    assert test_board.tile_array[3][3].piece_color() == 'black'
    assert test_board.tile_array[4][3].piece_color() == 'black'
    assert test_board.tile_array[3][4].piece_color() == 'black'
    assert test_board.tile_array[4][4].piece_color() == 'white'

    assert test_board.place_piece(7, 7, 'black') == False
    assert test_board.tile_array[2][3].piece_color() == 'black'
    assert test_board.tile_array[3][3].piece_color() == 'black'
    assert test_board.tile_array[4][3].piece_color() == 'black'
    assert test_board.tile_array[3][4].piece_color() == 'black'
    assert test_board.tile_array[4][4].piece_color() == 'white'
    
    #test get_score method and correspondingly __iter__
    assert test_board.get_score() == (1, 4)
    assert test_board.get_valid_moves('white') == [(2, 2), (2, 4), (4, 2)]
    assert test_board.get_valid_moves('black') == [(4, 5), (5, 4), (5, 5)]
    

    test_board = Board()
    test_board.tile_array[1][4].place_piece('white')
    test_board.tile_array[2][4].place_piece('white')
    test_board.tile_array[3][4].place_piece('white')
    test_board.tile_array[4][4].place_piece('white')
    test_board.tile_array[5][4].place_piece('black')
    test_board.tile_array[2][3].place_piece('black')
    test_board.tile_array[3][3].place_piece('black')
    test_board.tile_array[4][3].place_piece('black')
    test_board.tile_array[5][3].place_piece('black')
    test_board.tile_array[2][4].place_piece('black')
    test_board.tile_array[5][4].place_piece('black')
    assert test_board.check_valid_coord(6, 4, "white") == True
    assert test_board.get_valid_moves('white') == [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 4)]
    assert test_board.get_valid_moves('black') == [(0, 4), (0, 5), (1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (5, 5)]

if __name__ == '__main__':
    test()