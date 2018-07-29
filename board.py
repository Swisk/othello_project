from tile import Tile

class Board:
    def __init__(self):
        self._tile_array = [[Tile() for col in range(8)] for row in range(8)]

    #getter
    @property
    def tile_array(self):
        return self._tile_array

    def check_valid_coord(self, row, col, color):

        #create list of all modifications to row, check_ tuple
        directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

        for dir in directions:
            check_row = row + dir[0]
            check_col = col + dir[1]

            #skip over directions that lead out of bounds
            if check_row < 0 or check_row >= 8 or check_col < 0 or check_col >= 8:
                continue

            else:
                #if no piece there, invalid direction and move on
                if self.tile_array[check_row][check_col].isempty():
                    continue

                #if piece check_or is different from current piece, check if there is piece of player check_or to create matching caps
                elif self.tile_array[check_row][check_col].piece_color() != color:
                    #update search in the same direction as before until piece is found or out of bounds
                    #we update first to ensure loop conditions hold
                    check_row += dir[0]
                    check_col += dir[1]
                    while (check_row >= 0 and check_row < 8 and check_col >= 0 and check_col < 8):
                        if self.tile_array[check_row][check_col].piece_color() == color:
                            return True

                        check_row += dir[0]
                        check_col += dir[1]


        #if fall all tests then invalid coord
        return False

    def place_piece(self, row, col, color):
        #check if piece is appropriate before placing
        if self.check_valid_coord(row, col, color):
            self.tile_array[row][col].place_piece(color)
            #need to flip all intermediate pieces
    
    def flip_intermediate(self):
        pass

    def get_score(self):
        pass


def test():
    test_board = Board()
    assert test_board.check_valid_coord(1, 1, "white") == False
    # not supposed to be accessed like this 
    test_board.tile_array[1][2].place_piece('white')
    test_board.tile_array[2][2].place_piece('black')
    assert test_board.check_valid_coord(3, 2, "white") == True
    assert test_board.check_valid_coord(3, 2, "black") == False
    test_board.tile_array[1][3].place_piece('black')
    assert test_board.check_valid_coord(1, 1, "black") == True
    test_board.tile_array[2][2].flip_piece()
    assert test_board.check_valid_coord(3, 2, "black") == False
    assert test_board.check_valid_coord(3, 2, "white") == False

if __name__ == '__main__':
    test()