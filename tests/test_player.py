import unittest
from src.actions import Actions
from src.player import Player
from src.properties import Properties, _init_properties


class MyTestCase(unittest.TestCase):
    def test_move_player(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        self.player.action(Actions.MOVE_TO_TILE, 11)
        self.assertEqual(self.player.position, 11, 'Moving from 0, 11 spaces. Should be 11')
        self.assertEqual(self.player.cash, 1500, 'Should be 1500. Not passing GO (1)')

        self.player.action(Actions.MOVE_TO_TILE, 11)
        self.assertEqual(self.player.position, 22, 'Moving from 11, 11 spaces. Should be 22')
        self.assertEqual(self.player.cash, 1500, 'Should be 1500. Not passing GO (2)')

        self.player.action(Actions.MOVE_TO_TILE, 11)
        self.assertEqual(self.player.position, 33, 'Moving from 22, 11 spaces. Should be 33')
        self.assertEqual(self.player.cash, 1500, 'Should be 1500. Not passing GO (3)')

        self.player.action(Actions.MOVE_TO_TILE, 11)
        self.assertEqual(self.player.position, 4, 'Moving from 33, 11 spaces. Should be 4')
        self.assertEqual(self.player.cash, 1700, 'Should be 1700 after passing GO')

    def test_move_directly(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        self.player.action(Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 30)
        self.assertEqual(self.player.position, 30, 'Moving directly to 30')
        self.assertEqual(self.player.cash, 1500, 'Should still be 1500 after moving to 30')

        self.player.action(Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 10)
        self.assertEqual(self.player.position, 10, 'Moving directly to 10 from 30')
        self.assertEqual(self.player.cash, 1700, 'Should have passed GO after moving to 10 from 30')

    def test_move_directly_do_not_pass_go(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        self.player.action(Actions.MOVE_DIRECTLY_TO_TILE_DO_NOT_PASS_GO, 30)
        self.assertEqual(self.player.position, 30, 'Moving directly to 30 (Do not pass GO)')
        self.assertEqual(self.player.cash, 1500, 'Should still be 1500 after moving to 30 (Do not pass GO)')

        self.player.action(Actions.MOVE_DIRECTLY_TO_TILE_DO_NOT_PASS_GO, 10)
        self.assertEqual(self.player.position, 10, 'Moving directly to 10 from 30 (Do not pass GO)')
        self.assertEqual(self.player.cash, 1500, 'Should have passed GO after moving to 10 from 30. Cash stays same.')

    def test_receive_money(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        self.player.action(Actions.RECEIVE_MONEY, 30)
        self.assertEqual(self.player.cash, 1530, 'Received 30 dollars. Started at 1500. Should now be 1530')

        self.player.action(Actions.RECEIVE_MONEY, 47)
        self.assertEqual(self.player.cash, 1577, 'Received 47 dollars. Started at 1530. Should now be 1577')

    def test_buy_properties(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        self.player.action(Actions.BUY_PROPERTY, 'Boardwalk')
        self.assertEqual(self.player.cash, 1100, 'Bought Boardwalk, should have 1100 leftover')

        boardwalk = Properties.get_property_by_name('Boardwalk')
        self.assertEqual(boardwalk.property_owner, self.player.game_piece, 'New owner should be player')

    def test_buy_houses(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        self.player.action(Actions.BUY_PROPERTY, 'Boardwalk')
        self.player.action(Actions.BUY_PROPERTY, 'Park Place')

        # Should have 750 cash at this point
        self.player.action(Actions.BUY_HOUSE, 'Boardwalk')
        self.assertEqual(Properties.get_property_by_name('Boardwalk').num_houses, 1, 'Got a house on Boardwalk')
        self.assertEqual(self.player.cash, 550, 'Had 750, house cost 200, should now have 550')

    def test_pay_money(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        self.player.action(Actions.BUY_PROPERTY, 'Boardwalk')
        self.player.action(Actions.BUY_PROPERTY, 'Park Place')

        # Should have 750 at this point
        self.player.action(Actions.BUY_HOUSE, 'Boardwalk')
        self.assertEqual(self.player.cash, 550, 'Started at 750, bought a house for 200, should be 550 cash')
        self.assertEqual(Properties.get_property_by_name('Boardwalk').num_houses, 1, 'Num houses should be 1')

        # Paying 1 dollar more than we have in cash. Will have to sell house.
        self.player.action(Actions.PAY_MONEY, 551)
        self.assertEqual(self.player.cash, 99, 'Had 1300, sell house for 100, left with 99')
        self.assertEqual(Properties.get_property_by_name('Boardwalk').num_houses, 0, 'Num houses should be 0')

        # cash = 99
        # mortgage Park Place = 350 / 2 = 175
        # mortgage Boardwalk = 400 / 2 = 200
        # total = $474
        money = self.player.action(Actions.PAY_MONEY, 1000)
        self.assertEqual(money, 474, 'Player did not have enough money. The function returned amount of cash on hand')

    def test_property_repair(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        # Resetting game pieces
        Player._game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']
        self.player = Player()

        # Some shopping money
        self.player.action(Actions.RECEIVE_MONEY, 100000)

        self.player.action(Actions.BUY_PROPERTY, 'Boardwalk')
        self.player.action(Actions.BUY_PROPERTY, 'Park Place')

        self.player.action(Actions.BUY_HOUSE, 'Boardwalk')
        self.player.action(Actions.BUY_HOUSE, 'Park Place')
        self.player.action(Actions.BUY_HOUSE, 'Boardwalk')
        self.player.action(Actions.BUY_HOUSE, 'Park Place')
        self.player.action(Actions.BUY_HOUSE, 'Boardwalk')
        self.player.action(Actions.BUY_HOUSE, 'Park Place')
        self.player.action(Actions.BUY_HOUSE, 'Boardwalk')
        self.player.action(Actions.BUY_HOUSE, 'Park Place')
        self.player.action(Actions.BUY_HOUSE, 'Boardwalk')

        self.assertEqual(
            Properties.get_property_by_name('Boardwalk').num_houses, 5, 'Boardwalk should be hotel status'
        )

        self.assertEqual(
            Properties.get_property_by_name('Park Place').num_houses, 4, 'Park Place should have 4 houses'
        )

        # Chance:  4 houses = 25 per house = 100, 1 hotel = 100, total = $200
        # CC: 4 houses = 40 per house = 160, 1 hotel = 115, total = $275
        repair_amount = self.player.action(Actions.PROPERTY_REPAIR, 'Chance')
        self.assertEqual(repair_amount, 200, 'Chance repairs should be 200')

        repair_amount = self.player.action(Actions.PROPERTY_REPAIR, 'Community Chest')
        self.assertEqual(repair_amount, 275, 'Community Chest repairs should be 275')


if __name__ == '__main__':
    unittest.main()
