import json
import hashlib
from selenium.webdriver.remote.webelement import WebElement
from config.constants import COMMON_PLAYER_DATA_KEYS
from models.PlayerTableData import PlayerTableData
# from utils.player_utils import get_data_from_column


class Player:

    def __init__(self, player_data_html: [], player_type: str):
        self.player_table_data: PlayerTableData = PlayerTableData(player_data_html, player_type)
        self.player_type = player_type

    @staticmethod
    def get_player_id(name, pos, nfl_team):
        m = hashlib.md5()
        m.update(str(name + pos + nfl_team).encode("utf-8"))
        return str(int(m.hexdigest(), 16))[0:12]

    def to_json(self, as_dict=False):
        player_dict = dict()

        if not self.player_table_data.get_table_data():
            return json.dumps(player_dict, indent=4) if not as_dict else player_dict

        # td element in column 3 stores the data we want
        # name = get_data_from_column(td_element, COMMON_PLAYER_DATA_KEYS[2][0])
        player_dict = self.player_table_data.get_table_data()
        player_dict["id"] = Player.get_player_id(player_dict.get("playerName"),
                                                 player_dict.get("playerPos"),
                                                 player_dict.get("playerTeam"))
        return json.dumps(player_dict, indent=4) if not as_dict else player_dict
