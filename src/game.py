import logging
from src.actions import Actions
from src.board import Board
from src.dice import Dice
from src.player import Player
from src.properties import Properties
from src.tiletype import TileType


class Game:
    def __init__(self, num_players):
        self.dice = 2

        # Initialize the players
        logging.info(f'Starting game with {num_players} players')

        self.players = []
        for i in range(num_players):
            self.players.append(Player())

        self.player_turn = 0

        # Initialize the board
        self.board = Board()

        players_initialized = ', '.join([p.game_piece for p in self.players])
        logging.info(f'Players initialized: {players_initialized}')

    def get_player(self, game_piece):
        for p in self.players:
            if p.game_piece == game_piece:
                return p

    def get_current_player(self):
        return self.players[self.player_turn]

    def next_player_turn(self):
        self.player_turn = (self.player_turn + 1) % len(self.players)
        return self.player_turn

    def remove_player_from_game(self, player_name):
        logging.info(f'{player_name} could not pay the full amount owed and has gone bankrupt!')
        player = self.get_player(player_name)
        self.players.remove(player)

    def player_action(self, tile):
        current_player = self.get_current_player()
        curr = current_player.game_piece
        logging.info(f'{curr} landed on tile {tile[0]}.')

        if tile[1] in [TileType.PROPERTY, TileType.UTILITY, TileType.RAILROAD]:
            property_owner = Properties.get_property_owner_by_name(tile[0])

            if property_owner == curr:
                # Player already owns property. Do nothing.
                logging.info(f'{curr} already owns property {tile[0]}. No action taken.')
                return

            if property_owner == 'Bank':
                # nobody owns property. Player can choose to buy or auction
                # TODO: buy or auction
                did_player_buy_property = current_player.action(Actions.BUY_PROPERTY, tile[0])
                if not did_player_buy_property:
                    # Chose not to buy house, or not enough money to buy house. Auction it!
                    # TODO: Auction house
                    return
                return

            # If we're here, that means another player owns the property and current player needs to pay rent.
            landlord_player = self.get_player(property_owner)
            amount_owed = Properties.get_rent(tile[0], self.dice)
            logging.info(f'{curr} owes {landlord_player.game_piece} ${amount_owed}')

            amount_paid = current_player.action(Actions.PAY_MONEY, amount_owed)
            landlord_player.action(Actions.RECEIVE_MONEY, amount_paid)

            if amount_owed != amount_paid:
                # Player could not pay the amount owed and has gone bankrupt.
                self.remove_player_from_game(curr)
            else:
                logging.info(f'{curr} has paid the full ${amount_paid}, has ${current_player.cash} left.')

        if tile[1] == TileType.LUXURY_TAX:
            logging.info(f'{curr} owes $75 luxury tax.')
            amount_owed = 75
            amount_paid = current_player.action(Actions.PAY_MONEY, amount_owed)
            if amount_paid != amount_owed:
                # Player could not pay the amount owed and has gone bankrupt.
                self.remove_player_from_game(curr)
            else:
                logging.info(f'{curr} has paid the full ${amount_paid}, has ${current_player.cash} left.')

        if tile[1] == TileType.INCOME_TAX:
            amount_paid = current_player.action(Actions.PAY_INCOME_TAX, None)
            logging.info(f'{curr} has paid income tax of {amount_paid}, has ${current_player.cash} left.')

        if tile[1] == TileType.GO_TO_JAIL:
            current_player.action(Actions.MOVE_DIRECTLY_TO_TILE_DO_NOT_PASS_GO, 10)
            logging.info(f'{curr} will go directly to jail.')

        if tile[1] == TileType.CHANCE:
            # TODO: implement Actions.PAY_MONEY_TO_EACH_PLAYER and Actions.RECEIVE_MONEY_FROM_EACH_PLAYER
            chance_card = self.board.chance_cards.draw()
            logging.info(f'{curr} drew Chance card: {chance_card.name}')
            current_player.action(chance_card.action, chance_card.amount)

        if tile[1] == TileType.COMMUNITY_CHEST:
            cc_card = self.board.community_chest_cards.draw()
            logging.info(f'{curr} drew Community Chest card: {cc_card.name}')
            current_player.action(cc_card.action, cc_card.amount)

        # GO, Jail (Just Visiting), and Free Parking do nothing.
        if tile[1] in [TileType.GO, TileType.JAIL, TileType.FREE_PARKING]:
            logging.info(f'{curr} takes no action.')

        return

    def play_turn(self, player):
        logging.info(player)
        logging.info(f'{player.game_piece} is starting their turn.')

        # Decide to purchase houses
        # TODO: Have player decide to purchase houses

        # Roll dice and move
        self.dice = Dice.roll()
        logging.info(f'{player.game_piece} rolled {self.dice}.')

        new_position = player.action(Actions.MOVE_TO_TILE, self.dice)

        # Take action based on where player lands on the board
        tile_landed = self.board.get_tile_from_position(new_position)
        self.player_action(tile_landed)

    def play_game(self):
        while len(self.players) > 1:
            self.play_turn(self.players[self.player_turn])
            self.next_player_turn()
