import unittest
from src.properties import Properties, TileProperty, _init_properties


class TestProperties(unittest.TestCase):
    def test_get_property_by_name(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        prop = Properties.get_property_by_name('Boardwalk')
        self.assertEqual(prop.name, 'Boardwalk', 'Property name should be Boardwalk')
        self.assertIsInstance(prop, TileProperty, 'Should be TileProperty class')

    def test_get_rent_by_name_color_properties(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        boardwalk = Properties.get_property_by_name('Boardwalk')
        park_place = Properties.get_property_by_name('Park Place')

        self.assertEqual(Properties.get_rent(property_name='Boardwalk'), 0, 'Bank owns property, rent should be 0')

        # Note: DO NOT JUST MANUALLY CHANGE OWNER IN ANY OTHER INSTANCE BESIDES TESTING!
        boardwalk.property_owner = 'Battleship'
        self.assertEqual(Properties.get_rent(property_name='Boardwalk'), 50,
                         'Boardwalk is owned, rent should be 50')

        park_place.property_owner = 'Battleship'
        self.assertEqual(Properties.get_rent(property_name='Boardwalk'), 100,
                         'All properties of same color are owned, rent should be 100')

        boardwalk.num_houses = 1

        self.assertEqual(Properties.get_rent(property_name='Boardwalk'), 200,
                         'Boardwalk rent with 1 house should be 200')

        self.assertEqual(Properties.get_rent(property_name='Park Place'), 70,
                         'Park Place rent should be 70 which is doubled still')

    def test_get_rent_by_name_railroads(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        railroad_1 = Properties.get_property_by_name('Reading Railroad')
        railroad_2 = Properties.get_property_by_name('Pennsylvania Railroad')
        railroad_3 = Properties.get_property_by_name('B. & O. Railroad')
        railroad_4 = Properties.get_property_by_name('Short Line')

        self.assertEqual(Properties.get_rent(property_name='Reading Railroad'), 0,
                         'Bank owns property, rent should be 0')

        # Note: DO NOT JUST MANUALLY CHANGE OWNER IN ANY OTHER INSTANCE BESIDES TESTING!
        railroad_1.property_owner = 'Car'
        self.assertEqual(Properties.get_rent(property_name='Reading Railroad'), 25,
                         'One railroad owned, rent should be 25')

        railroad_2.property_owner = 'Car'
        self.assertEqual(Properties.get_rent(property_name='Reading Railroad'), 50,
                         'Two railroads owned, rent should be 50')

        railroad_3.property_owner = 'Car'
        self.assertEqual(Properties.get_rent(property_name='Reading Railroad'), 100,
                         'Three railroads owned, rent should be 100')

        railroad_4.property_owner = 'Car'
        self.assertEqual(Properties.get_rent(property_name='Reading Railroad'), 200,
                         'Three railroads owned, rent should be 200')

    def test_get_rent_by_name_utilities(self):
        # Resetting property instance
        Properties.properties = _init_properties()

        utility_1 = Properties.get_property_by_name('Electric Company')
        utility_2 = Properties.get_property_by_name('Water Works')

        self.assertEqual(Properties.get_rent(property_name='Electric Company', dice_roll=12), 0,
                         'Bank owns property, rent should be 0')

        # Note: DO NOT JUST MANUALLY CHANGE OWNER IN ANY OTHER INSTANCE BESIDES TESTING!
        utility_1.property_owner = 'Iron'
        self.assertEqual(Properties.get_rent(property_name='Electric Company', dice_roll=12), 48,
                         'Dice roll 12, one utility owned, 12 * 4 = 48')

        utility_2.property_owner = 'Iron'
        self.assertEqual(Properties.get_rent(property_name='Electric Company', dice_roll=12), 120,
                         'Dice roll 12, two utilities owned, 12 * 10 = 120')


if __name__ == '__main__':
    unittest.main()
