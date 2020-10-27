from src.tiletype import TileType


class Tiles:
    @staticmethod
    def get_tiles():
        tiles = (
            ('GO', TileType.GO),
            ('Mediterranean Avenue', TileType.PROPERTY),
            ('Community Chest', TileType.COMMUNITY_CHEST),
            ('Baltic Avenue', TileType.PROPERTY),
            ('Income Tax', TileType.INCOME_TAX),
            ('Reading Railroad', TileType.RAILROAD),
            ('Oriental Avenue', TileType.PROPERTY),
            ('Chance', TileType.CHANCE),
            ('Vermont Avenue', TileType.PROPERTY),
            ('Connecticut Avenue', TileType.PROPERTY),
            ('Jail', TileType.JAIL),
            ('St. Charles Place', TileType.PROPERTY),
            ('Electric Company', TileType.UTILITY),
            ('States Avenue', TileType.PROPERTY),
            ('Virginia Avenue', TileType.PROPERTY),
            ('Pennsylvania Railroad', TileType.RAILROAD),
            ('St. James Place', TileType.PROPERTY),
            ('Community Chest', TileType.COMMUNITY_CHEST),
            ('Tennessee Avenue', TileType.PROPERTY),
            ('New York Avenue', TileType.PROPERTY),
            ('Free Parking', TileType.FREE_PARKING),
            ('Kentucky Avenue', TileType.PROPERTY),
            ('Chance', TileType.CHANCE),
            ('Indiana Avenue', TileType.PROPERTY),
            ('Illinois Avenue', TileType.PROPERTY),
            ('B. & O. Railroad', TileType.RAILROAD),
            ('Atlantic Avenue', TileType.PROPERTY),
            ('Ventnor Avenue', TileType.PROPERTY),
            ('Water Works', TileType.UTILITY),
            ('Marvin Gardens', TileType.PROPERTY),
            ('Go to Jail', TileType.GO_TO_JAIL),
            ('Pacific Avenue', TileType.PROPERTY),
            ('North Carolina Avenue', TileType.PROPERTY),
            ('Community Chest', TileType.COMMUNITY_CHEST),
            ('Pennsylvania Avenue', TileType.PROPERTY),
            ('Short Line', TileType.RAILROAD),
            ('Chance', TileType.CHANCE),
            ('Park Place', TileType.PROPERTY),
            ('Luxury Tax', TileType.LUXURY_TAX),
            ('Boardwalk', TileType.PROPERTY)
        )

        return tiles
