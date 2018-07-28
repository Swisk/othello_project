from piece import Piece

class Tile:
    def __init__(self):
        self._piece = []

    #getter
    @property
    def piece(self):
        return self._piece

    #setter, controls intializing piece only if tile is empty and value type
    @piece.setter
    def piece(self, val):
        if self.isempty():
            if isinstance(val, Piece):
                self._piece = val

    #check if tile is empty
    def isempty(self):
        if self.piece == []:
            return True
        return False

    #add piece to tile (only can be done once)
    def place_piece(self, color):
        self.piece = Piece(color)
        
    #change color of piece
    def flip_piece(self):
        if not self.isempty():
            self.piece.flip()

    #return color of piece within tile
    def piece_color(self):
        if not self.isempty():
            return self.piece.color


def test():
    test_tile = Tile()
    assert test_tile.isempty() == True
    assert test_tile.piece == []
    assert test_tile.flip_piece() == None
    assert test_tile.piece_color() == None
    test_tile.place_piece('white')
    assert test_tile.piece_color() == 'white'
    test_tile.flip_piece()
    assert test_tile.piece_color() == 'black'

if __name__ == '__main__':
    test()