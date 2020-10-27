import logging
from src.game import Game

logging.basicConfig(filename='monopoly.log', level=logging.INFO)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_players = 3
    Game(num_players).play_game()
