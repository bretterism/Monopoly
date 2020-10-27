import unittest
from src.board import Board


# TODO: Board is no longer responsible for initializing players. Need to refactor tests here

class TestBoard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.board = Board()

    def test_get_tile_position(self):
        pos = self.board.get_tile_position('Marvin Gardens')
        self.assertEqual(pos, 29, 'Marvin Gardens should be 29')

    def test_get_tile_from_position(self):
        tile = self.board.get_tile_from_position(29)
        self.assertEqual(tile[0], 'Marvin Gardens', 'Tile should be Marvin Gardens')


if __name__ == '__main__':
    unittest.main()
