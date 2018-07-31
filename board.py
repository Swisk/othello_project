from tile import Tile

class Board:
    def __init__(self):
        self._tile_array = [[Tile() for col in range(8)] for row in range(8)]

    #getter
    @property
    def tile_array(self):
        return self._tile_array

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

    
    def get_intermediate(self, row, col, color):
        #create list of all modifications to row, check_ tuple
        directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        #create output list of all intermediate tiles
        output = []

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
                        #add direction array to output only if direction is properly bounded
                        if self.tile_array[check_row][check_col].piece_color() == color:
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

    #TODO implement board cloning for AI
    def get_copy(self):
        pass


def test():
    test_board = Board()
    """
    pieces manually placed
    - x o
    - o - 
    - - -
    """

    #test check_valid_coord and correspondingly get_intermediate method
    assert test_board.check_valid_coord(1, 1, "white") == False
    test_board.tile_array[1][2].place_piece('white')
    test_board.tile_array[2][2].place_piece('black')
    assert test_board.check_valid_coord(3, 2, "white") == True
    assert test_board.check_valid_coord(3, 2, "black") == False
    test_board.tile_array[1][3].place_piece('black')
    assert test_board.check_valid_coord(1, 1, "black") == True
    test_board.tile_array[2][2].flip_piece()
    assert test_board.check_valid_coord(3, 2, "black") == False
    assert test_board.check_valid_coord(3, 2, "white") == False
    test_board.tile_array[2][2].flip_piece()

    #test place_piece method
    test_board.place_piece(1, 1, 'black')
    assert test_board.tile_array[1][1].piece_color() == 'black'
    assert test_board.tile_array[1][2].piece_color() == 'black'
    assert test_board.tile_array[1][3].piece_color() == 'black'
    assert test_board.tile_array[2][2].piece_color() == 'black'

    #test get_score method and correspondingly __iter__
    assert test_board.get_score() == (0, 4)

if __name__ == '__main__':
    test()