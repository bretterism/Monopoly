from enum import Enum, auto


class Actions(Enum):
    MOVE_TO_TILE = auto(),
    MOVE_DIRECTLY_TO_TILE_PASS_GO = auto(),
    MOVE_DIRECTLY_TO_TILE_DO_NOT_PASS_GO = auto(),
    MOVE_DIRECTLY_TO_NEAREST_UTILITY = auto(),
    MOVE_DIRECTLY_TO_NEAREST_RAILROAD = auto(),
    RECEIVE_MONEY = auto(),
    RECEIVE_MONEY_FROM_EACH_PLAYER = auto(),
    PAY_MONEY = auto(),
    PAY_MONEY_TO_EACH_PLAYER = auto(),
    PAY_INCOME_TAX = auto(),
    BUY_PROPERTY = auto(),
    BUY_HOUSE = auto(),
    PROPERTY_REPAIR = auto(),
    GET_OUT_OF_JAIL_FREE = auto()
