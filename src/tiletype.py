from enum import Enum, auto


class TileType(Enum):
    GO = auto(),
    PROPERTY = auto(),
    RAILROAD = auto(),
    UTILITY = auto(),
    COMMUNITY_CHEST = auto(),
    CHANCE = auto(),
    INCOME_TAX = auto(),
    LUXURY_TAX = auto(),
    JAIL = auto(),
    GO_TO_JAIL = auto(),
    FREE_PARKING = auto()
