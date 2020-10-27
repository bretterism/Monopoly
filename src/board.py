from src.cards import ChanceCards, CommunityChestCards
from src.tiles import Tiles


class Board:
    def __init__(self):

        # Initialize Chance cards
        self.chance_cards = ChanceCards()
        self.chance_cards.shuffle()

        # Initialize Community Chest cards
        self.community_chest_cards = CommunityChestCards()
        self.community_chest_cards.shuffle()

        # Initialize the tiles
        self.tiles = Tiles.get_tiles()
        self.num_tiles = len(self.tiles)

    def get_tile_position(self, tile_name):
        for idx, tile in enumerate(self.tiles):
            if tile[0] == tile_name:
                return idx

    def get_tile_from_position(self, tile_idx):
        return self.tiles[tile_idx]
