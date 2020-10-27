import random
import logging
from src.actions import Actions
from src.properties import Properties
from src.tiletype import TileType


class Player:
    _game_pieces = ['battleship', 'dog', 'iron', 'shoe', 'thimble', 'top hat', 'wheelbarrow']

    def __init__(self):
        # Pick a random game piece
        self.game_piece = Player._game_pieces.pop(random.randrange(len(Player._game_pieces)))
        # Every player starts with $1,500
        self.cash = 1500
        # Starting at 0 (GO)
        self.position = 0

    def __str__(self):
        properties = ', '.join(Properties.get_property_names_by_owner(self.game_piece))
        if properties:
            return f'{self.game_piece}: ${self.cash} cash, owns properties {properties}.'
        else:
            return f'{self.game_piece}: ${self.cash} cash, owns no properties.'

    def _move_to_tile(self, amount):
        # TODO: pass number of tiles instead of hard-coding value
        num_tiles = 40
        current_position = self.position
        new_position = (current_position + amount) % num_tiles

        self.position = new_position

        # Check if we passed GO
        if new_position < current_position:
            logging.info(f'{self.game_piece} has passed GO.')
            self._receive_money(200)

        return self.position

    def _move_directly_to_tile_pass_go(self, new_position):
        current_position = self.position
        self.position = new_position

        # Check if we passed GO
        if new_position < current_position:
            logging.info(f'{self.game_piece} has passed GO.')
            self._receive_money(200)

        return self.position

    def _move_directly_to_tile_do_not_pass_go(self, new_position):
        self.position = new_position

        return self.position

    def _receive_money(self, amount):
        self.cash += amount
        logging.info(f'{self.game_piece} received ${amount}, now has ${self.cash}')
        return amount

    def _pay_money(self, amount):
        if self.cash > amount:
            # We have enough cash to pay.
            self.cash -= amount
            logging.info(f'{self.game_piece} paid ${amount}, now has ${self.cash}')

            return amount

        # If we reached this far, it means there's not enough cash to pay.
        # Find if there are any houses to sell
        properties_owned = Properties.get_properties_by_owner(self.game_piece)
        for p in properties_owned:
            # Check if we got enough cash from selling houses.
            if self.cash > amount:
                break

            if p.num_houses > 0:
                # Found a house. We'll need to make sure we're keeping houses evenly distributed across the group.
                properties_in_same_color = [g for g in properties_owned if g.color == p.color]
                # Start with the property with the most houses
                properties_in_same_color.sort(key=lambda l: l.num_houses, reverse=True)
                # Sell some properties
                for i in properties_in_same_color:
                    self.cash += i.mortgage_house()
                    # Check after each house sold to see if we got enough cash
                    if self.cash > amount:
                        break

        # See if we can bow out of this action after selling houses
        if self.cash > amount:
            self.cash -= amount
            return amount

        # If we reached this far, it means we didn't have enough houses to sell. Start mortgaging properties.
        for p in properties_owned:
            if self.cash > amount:
                break

            self.cash += p.mortgage_property()

        # Finally see if we have enough money to pay up.
        # If we have enough cash, return the full amount.
        # If there wasn't enough, just send whatever cash is available.
        # This will indicate the player is out and should be removed from the game.
        if self.cash > amount:
            self.cash -= amount
            return amount
        else:
            available_cash = self.cash
            self.cash = 0
            return available_cash

    def _pay_income_tax(self):
        # Player shall pay 10% of total assets or $200, whichever is less.
        props = Properties.get_properties_by_owner(owner_name=self.game_piece)

        # Get all property values
        sum_prop_values = 0
        sum_house_values = 0
        for prop in props:
            # Get all the property values
            if prop.is_mortgaged:
                sum_prop_values += prop.mortgage_value
            else:
                sum_prop_values += prop.property_value

            # For each property, get all house values
            if prop.tile_type == TileType.PROPERTY:
                sum_house_values += prop.num_houses * prop.cost_per_house

        # Add all assets together
        sum_assets = sum_prop_values + sum_house_values + self.cash

        # Get 10% of assets
        sum_assets = int(sum_assets * 0.1)

        # If 10% of the assets < 200, pay assets
        if sum_assets < 200:
            amount_paid = self._pay_money(sum_assets)
        else:
            amount_paid = self._pay_money(200)

        return amount_paid

    def _get_property_repair_amount(self, card_type):
        # Here, we need 'Chance' or 'Community Chest' for card type, as they drive different values.
        amount_to_pay = 0
        price_per_house = 0
        price_per_hotel = 0

        if card_type == 'Chance':
            # For each house pay $25, for each hotel (num_houses =  5) pay $100
            price_per_house = 25
            price_per_hotel = 100
        if card_type == 'Community Chest':
            # For each house pay $40, for each hotel (num_houses =  5) pay $115
            price_per_house = 40
            price_per_hotel = 115

        properties_owned = Properties.get_properties_by_owner(owner_name=self.game_piece, tile_type=TileType.PROPERTY)
        for p in properties_owned:
            if 0 < p.num_houses < 5:
                amount_to_pay += price_per_house * p.num_houses

            if p.num_houses == 5:
                amount_to_pay += price_per_hotel

        return amount_to_pay

    def _buy_property(self, property_name):
        logging.info(f'{self.game_piece} is attempting to buy the property {property_name}.')
        property_to_buy = Properties.get_property_by_name(property_name)
        current_owner = property_to_buy.property_owner

        if self.cash > property_to_buy.property_value and current_owner == 'Bank':
            self.cash -= property_to_buy.property_value
            property_to_buy.update_property_owner(self.game_piece)

            logging.info(f'{self.game_piece} bought property {property_name} '
                         f'for ${property_to_buy.property_value}, has ${self.cash} left.')
            return True

        logging.info(f'{self.game_piece} did not buy property {property_name}, has ${self.cash} left.')
        return False

    def _buy_house(self, property_name):
        logging.info(f'{self.game_piece} is attempting to buy a house on {property_name}.')
        properties_owned = Properties.get_properties_by_owner(self.game_piece, TileType.PROPERTY)

        if properties_owned:
            if property_name not in [p.name for p in properties_owned]:
                e = 'Property' + property_name + ' not owned by player.'
                logging.error(e)
                raise Exception(e)

        # Get the property to put a house on.
        prop = Properties.get_property_by_name(property_name)

        # Make sure we're dealing with the right type of property first...
        if prop.tile_type != TileType.PROPERTY:
            return 0

        # See if player can afford to buy a house.
        if self.cash < prop.cost_per_house:
            logging.warning(f'{self.game_piece} could not afford a house on {property_name}. '
                            f'Still has {prop.num_houses} houses.')
            return prop.num_houses

        # Verifying player owns all the properties of that color before buying houses.
        properties_owned_in_same_color = Properties.get_properties_by_owner(
            owner_name=self.game_piece,
            tile_type=prop.tile_type,
            color=prop.color)

        prop_colors = Properties.get_properties_by_color(prop.color)

        if len(properties_owned_in_same_color) != len(prop_colors):
            logging.warning(f'{self.game_piece} does not own all properties of the same color '
                            f'and cannot purchase a house. Still has {prop.num_houses} houses.')
            return prop.num_houses

        # We also need to verify we don't own too many houses on one property.
        min_houses_in_same_color = min([p.num_houses for p in properties_owned_in_same_color])
        if prop.num_houses > min_houses_in_same_color:
            logging.warning(f'{self.game_piece} cannot put a house on this property '
                            f'before putting houses on the other properties first.')
            return prop.num_houses

        # If we made it this far, we are eligible to purchase a house on this property.
        # prop.add_house() will make sure we don't add more than 5 properties.
        house_count = prop.add_house()
        if house_count != -1:
            self.cash -= prop.cost_per_house
            logging.info(f'{self.game_piece} added a house to'
                         f' property {property_name} and now has {prop.num_houses} '
                         f'houses for {prop.cost_per_house}, has ${self.cash} left.')
        else:
            logging.warning(f'{self.game_piece} tried adding a house but already has too many.')
        return prop.num_houses

    def action(self, action, payload):
        if action == Actions.MOVE_TO_TILE:
            return self._move_to_tile(payload)

        if action == Actions.MOVE_DIRECTLY_TO_TILE_DO_NOT_PASS_GO:
            return self._move_directly_to_tile_do_not_pass_go(payload)

        if action == Actions.MOVE_DIRECTLY_TO_TILE_PASS_GO:
            return self._move_directly_to_tile_pass_go(payload)

        if action == Actions.RECEIVE_MONEY:
            return self._receive_money(payload)

        if action == Actions.PAY_MONEY:
            return self._pay_money(payload)

        if action == Actions.PAY_INCOME_TAX:
            return self._pay_income_tax()

        if action == Actions.PROPERTY_REPAIR:
            amount_to_pay = self._get_property_repair_amount(payload)
            return self._pay_money(amount_to_pay)

        if action == Actions.BUY_PROPERTY:
            return self._buy_property(payload)

        if action == Actions.BUY_HOUSE:
            return self._buy_house(payload)
