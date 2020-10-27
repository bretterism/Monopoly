import random
from src.actions import Actions


class Card:
    def __init__(self, card_type, name, action, amount):
        self.card_type = card_type
        self.name = name
        self.action = action
        self.amount = amount

        if card_type not in ['Chance', 'Community Chest']:
            raise Exception('Card type needs either "Chance" or "Community Chest"')

        if not isinstance(action, Actions):
            raise Exception('Card action needs to be of type Actions Enum')


class _Cards:
    def __init__(self):
        self.next_card = 0
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards[self.next_card]

        # Remove the "Get out of jail free" card if player draws it.
        if card.action == Actions.GET_OUT_OF_JAIL_FREE:
            self.cards.remove(card)

        # Figuring out the next card to return.
        self.next_card = (self.next_card + 1) % len(self.cards)

        return card

    def _insert_jail_card(self, card_type):
        # Adding the "Get out of jail free" card to the end of the stack.
        # This happens when the player uses the card and needs to put it back in the card pile.

        # First checking if card is already in pile
        for card in self.cards:
            if card.name == 'Get out of Jail Free' and card.card_type == card_type:
                return

        # If we made it this far, the card was not in the pile. Go ahead and add it.
        self.cards.insert(
            self.next_card - 1,
            Card(card_type, 'Get out of Jail Free', Actions.GET_OUT_OF_JAIL_FREE, None)
        )


class ChanceCards(_Cards):
    def __init__(self):
        super().__init__()

        self.cards = [
            Card('Chance', 'Advance to GO', Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 0),
            Card('Chance', 'Advance to Illinois Ave', Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 24),
            Card('Chance', 'Advance to St Charles Place', Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 11),
            Card('Chance', 'Advance to nearest utility', Actions.MOVE_DIRECTLY_TO_NEAREST_UTILITY, None),
            Card('Chance', 'Advance to nearest railroad', Actions.MOVE_DIRECTLY_TO_NEAREST_RAILROAD, None),
            Card('Chance', 'Advance to Reading Railroad', Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 5),
            Card('Chance', 'Advance to Boardwalk', Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 39),
            Card('Chance', 'Go Back 3 Spaces', Actions.MOVE_TO_TILE, -3),
            Card('Chance', 'Go Directly to Jail', Actions.MOVE_DIRECTLY_TO_TILE_DO_NOT_PASS_GO, 30),
            Card('Chance', 'Bank Pays Dividend', Actions.RECEIVE_MONEY, 50),
            Card('Chance', 'Elected Chairman of the Board', Actions.PAY_MONEY_TO_EACH_PLAYER, 50),
            Card('Chance', 'Building Loan Matures', Actions.RECEIVE_MONEY, 150),
            Card('Chance', 'Make General Repairs on Properties', Actions.PROPERTY_REPAIR, None),
            Card('Chance', 'Poor Tax', Actions.PAY_MONEY, 15),
            Card('Chance', 'Get out of Jail Free', Actions.GET_OUT_OF_JAIL_FREE, None)
        ]

    def insert_jail_card(self):
        self._insert_jail_card('Chance')


class CommunityChestCards(_Cards):
    def __init__(self):
        super().__init__()

        self.cards = [
            Card('Community Chest', 'Advance to GO', Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO, 0),
            Card('Community Chest', 'Bank Error in your Favor', Actions.RECEIVE_MONEY, 200),
            Card('Community Chest', 'Xmas Fund Matures', Actions.RECEIVE_MONEY, 100),
            Card('Community Chest', 'Income Tax Refund', Actions.RECEIVE_MONEY, 20),
            Card('Community Chest', 'Life Insurance Matures', Actions.RECEIVE_MONEY, 100),
            Card('Community Chest', 'Consultancy Fee', Actions.RECEIVE_MONEY, 25),
            Card('Community Chest', 'Second Place in Beauty Contest', Actions.RECEIVE_MONEY, 10),
            Card('Community Chest', 'Sale of Stock', Actions.RECEIVE_MONEY, 50),
            Card('Community Chest', 'Grand Opera Night', Actions.RECEIVE_MONEY_FROM_EACH_PLAYER, 50),
            Card('Community Chest', 'Doctors Fee', Actions.PAY_MONEY, 50),
            Card('Community Chest', 'Hospital Fee', Actions.PAY_MONEY, 100),
            Card('Community Chest', 'School Fee', Actions.PAY_MONEY, 150),
            Card('Community Chest', 'Assessed for Street Repairs', Actions.PROPERTY_REPAIR, None),
            Card('Community Chest', 'Go Directly to Jail', Actions.MOVE_DIRECTLY_TO_TILE_DO_NOT_PASS_GO, 30),
            Card('Community Chest', 'Get out of Jail Free', Actions.GET_OUT_OF_JAIL_FREE, None)
        ]

    def insert_jail_card(self):
        self._insert_jail_card('Community Chest')
