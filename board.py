from tile import Tile

class Board:
    def __init__(self):
        self._tile_array = [[Tile() for y in range(8)] for x in range(8)]



def test():
    pass

if __name__ == '__main__':
    test()