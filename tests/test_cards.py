import unittest
from src.actions import Actions
from src.cards import ChanceCards, CommunityChestCards


class TestCards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chance_cards = ChanceCards()
        cls.community_chest_cards = CommunityChestCards()

    def test_draw_chance(self):
        chance = self.chance_cards.draw()
        # didn't shuffle so top card should always be the same
        self.assertEqual(chance.card_type, 'Chance', 'Chance card type')
        self.assertEqual(chance.name, 'Advance to GO', 'Chance name')
        self.assertEqual(chance.action, Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 'Chance action')
        self.assertEqual(chance.amount, 0, 'Chance Amount')

    def test_draw_community_chest(self):
        cc = self.community_chest_cards.draw()
        # didn't shuffle so top card should always be the same
        self.assertEqual(cc.card_type, 'Community Chest', 'Community Chest card type')
        self.assertEqual(cc.name, 'Advance to GO', 'Community Chest name')
        self.assertEqual(cc.ation, Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 'Community Chest action')
        self.assertEqual(cc.amount, 0, 'Community Chest Amount')


if __name__ == '__main__':
    unittest.main()
