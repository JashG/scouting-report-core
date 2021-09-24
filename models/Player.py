from selenium.webdriver.remote.webelement import WebElement
from config.constants import PLAYER_DATA_KEYS
from utils.player_utils import get_data_from_column

class Player:

    def __init__(self, player_data_html: [], player_type: str):
        self.player_data_html = player_data_html
        self.player_type = player_type
        # self.player_data = self.parse_player_data_html()

    # def parse_player_data_html(self):
    #     player_json = dict()
    #     if len(self.player_data) <= 0:
    #         return player_json
    #
    #     td: WebElement
    #     for td, idx in self.player_data_html:
    #         if self.player_type == "OFFENSE":
    #             td_key = PLAYER_DATA_KEYS["OFFENSE"][idx]
    #             # All the keys are strings that have a one-to-one mapping with a column,
    #             # except for player data, which is an array
    #             if not isinstance(td_key, list):
    #                 player_json[td_key] = get_data_from_column(td, td_key)
    #             else:
    #                 pass
    #
    #     for key in player_json:
    #         print(key)
    #         print(player_json[key])
    #         print("\n")

    @staticmethod
    def get_basic_json():
        return None

    @staticmethod
    def get_full_json(self):
        return None
