import unittest
from src.game import Game
from src.player import Player
from src.tiles import Tiles


class MyTestCase(unittest.TestCase):
    def test_get_player(self):
        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']

        self.game = Game(3)
        self.game.players[0].game_piece = 'test'
        player = self.game.get_player('test')

        self.assertEqual(player.game_piece, 'test', 'Game Piece should be test')

    def test_get_current_player(self):
        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']

        self.game = Game(4)

        self.game.player_turn = 2
        test_current = self.game.players[2]
        current_player = self.game.get_current_player()

        self.assertEqual(test_current.game_piece, current_player.game_piece, 'Should be the same player')

    def test_next_player_turn(self):
        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']

        self.game = Game(4)
        self.game.player_turn = 0

        next_player = self.game.next_player_turn()
        self.assertEqual(next_player, 1, 'Next player should be 1')

        next_player = self.game.next_player_turn()
        self.assertEqual(next_player, 2, 'Next player should be 2')

        next_player = self.game.next_player_turn()
        self.assertEqual(next_player, 3, 'Next player should be 3')

        next_player = self.game.next_player_turn()
        self.assertEqual(next_player, 0, 'Next player should be 0')

    def test_player_action(self):
        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']

        self.game = Game(4)
        self.game.player_turn = 0

        tiles = Tiles.get_tiles()
        mediterranean_avenue = tiles[1]

        self.game.player_action(mediterranean_avenue)

    def test_play_turn(self):
        pass


if __name__ == '__main__':
    unittest.main()
