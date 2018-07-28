
class Piece:
    def __init__(self, color = 'black'):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        if val == 'white' or val == 'black':
            self._color = val
        else:
            raise ValueError('Incorrect color applied')

    def flip(self):
        if self.color == 'white':
            self.color = 'black'
        elif self.color == 'black':
            self.color = 'white'

def test():
    test_piece = Piece('black')
    assert test_piece.color == 'black'
    test_piece.flip()
    assert test_piece.color == 'white'

if __name__ == '__main__':
    test()