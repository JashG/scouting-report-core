from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchAttributeException
from config.constants import PLAYER_DATA_KEYS

OFFENSE_KEYS = PLAYER_DATA_KEYS["OFFENSE"]
KICKER_KEYS = PLAYER_DATA_KEYS["KICKER"]
DEFENSE_KEYS = PLAYER_DATA_KEYS["DEFENSE"]


class PlayerTableData:

    def __init__(self, tr_element: [], player_type: str):
        self.table_row = tr_element
        self.player_type = player_type
        self.table_data = self.init_table_data()

    def init_table_data(self):
        keys = []
        table_data = dict()
        player_type = self.player_type

        if player_type == "OFFENSE":
            keys = OFFENSE_KEYS
        elif player_type == "KICKER":
            keys = KICKER_KEYS
        else:
            keys = DEFENSE_KEYS

        if len(keys) > len(self.table_row):
            return dict()

        for idx, key in enumerate(keys):
            if not key:
                continue

            matching_td = self.table_row[idx]
            if not isinstance(key, list):
                table_data[key] = self.__get_data_for_key(key, matching_td)
            else:
                for player_sub_key in key:
                    table_data[player_sub_key] = self.__get_data_for_key(player_sub_key, matching_td)

        return table_data

    def get_table_data(self):
        return self.table_data

    def get_data_for_key(self, key: str):
        if len(self.table_data) == 0:
            return ""

        return self.table_data.get(key, "")

    def __get_data_for_key(self, key: str, td: WebElement):
        if not td or self.player_type is not "OFFENSE":
            return None

        # A few columns are formatted differently, so handle them here
        # Otherwise, the data we want is stored in the text attribute
        if key == OFFENSE_KEYS[2][0]:
            try:
                return td.text.split("\n")[0]
            except (NoSuchAttributeException, IndexError) as e:
                return ""

        if key == OFFENSE_KEYS[2][1] or key == OFFENSE_KEYS[2][2]:
            try:
                return (td.text.split("\n")[1].split("-")[0].strip()
                        if key == OFFENSE_KEYS[2][1]
                        else td.text.split("\n")[1].split("-")[1].strip())
            except (NoSuchAttributeException, IndexError) as e:
                return ""

        try:
            return td.text or td.textContent or ""
        except NoSuchAttributeException as e:
            return ""
