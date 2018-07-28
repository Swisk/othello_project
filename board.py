from tile import Tile

class Board:
    def __init__(self):
        self._tile_array = [[Tile() for col in range(8)] for row in range(8)]

    #getter
    @property
    def tile_array(self):
        return self._tile_array

    def check_valid_coord(self, row, col, color):
        #store current player color to check against other pieces
        color = color

        #create list of all modifications to row, col tuple
        directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

        for dir in directions:
            row += dir[0]
            col += dir[1]

            #skip over directions that lead out of bounds
            if row < 0 or row >= 8 or col < 0 or col >= 8:
                continue

            else:
                #if no piece there, invalid direction and move on
                if self.tile_array[row][col].isempty():
                    continue

                #if piece color is different from current piece, check if there is piece of player color to create matching caps
                elif self.tile_array[row][col].piece_color() != color:
                    #update search in the same direction as before until piece is found or out of bounds
                    #we update first to ensure loop conditions hold
                    row += dir[0]
                    col += dir[1]
                    while (row >= 0 and row < 8 and col >= 0 and col < 8):
                        if self.tile_array[row][col].piece_color() == color:
                            return True

                        row += dir[0]
                        col += dir[1]


        #if fall all tests then invalid coord
        return False

    def place_piece(self, row, col, color):
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

if __name__ == '__main__':
    test()