import random
import unittest
from src.dice import Dice


class TestDice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        random.seed(123)

    def test_roll(self):
        results = []
        for x in range(1000):
            results.append(Dice.roll())

        self.assertEqual(min(results), 2, 'Minimum value should be 2')
        self.assertEqual(max(results), 12, 'Maximum value should be 12')

        self.assertEqual(results.count(2), 25, 'Count of 2s')
        self.assertEqual(results.count(3), 61, 'Count of 3s')
        self.assertEqual(results.count(4), 81, 'Count of 4s')
        self.assertEqual(results.count(5), 138, 'Count of 5s')
        self.assertEqual(results.count(6), 124, 'Count of 6s')
        self.assertEqual(results.count(7), 159, 'Count of 7s')
        self.assertEqual(results.count(8), 126, 'Count of 8s')
        self.assertEqual(results.count(9), 95, 'Count of 9s')
        self.assertEqual(results.count(10), 103, 'Count of 10s')
        self.assertEqual(results.count(11), 60, 'Count of 11s')
        self.assertEqual(results.count(12), 28, 'Count of 12s')


if __name__ == '__main__':
    unittest.main()
