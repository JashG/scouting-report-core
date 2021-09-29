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

    # TODO: We shouldn't do this on the fly
    def get_player_id(self, name, pos, nfl_team):
        m = hashlib.md5()
        m.update(name + pos + nfl_team)
        return str(int(m.hexdigest(), 16))[0:12]

    def to_json(self, as_dict=False):
        player_json = dict()

        if not self.player_table_data:
            return json.dumps(player_json, indent=4) if not as_dict else player_json

        # td element in column 3 stores the data we want
        # name = get_data_from_column(td_element, COMMON_PLAYER_DATA_KEYS[2][0])
        player_json = self.player_table_data.get_table_data()
        return json.dumps(player_json, indent=4) if not as_dict else player_json
