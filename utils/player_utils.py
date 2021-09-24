from selenium.webdriver.remote.webelement import WebElement
from config.constants import PLAYER_DATA_KEYS

OFFENSE_KEYS = PLAYER_DATA_KEYS["OFFENSE"]
KICKER_KEYS = PLAYER_DATA_KEYS["KICKER"]
DEFENSE_KEYS = PLAYER_DATA_KEYS["DEFENSE"]


def get_data_from_column(td: WebElement, key: str):
    if not td:
        return None

    # Some columns are formatted differently, so handle them here
    # The remaining columns are just <span> elements
    # TODO Look into improving this
    if key == OFFENSE_KEYS["playerName"]:
        return td.find_element_by_class_name("playerNameFull").get_attribute("innerHtml")

    if key == OFFENSE_KEYS["playerPos"] or key == OFFENSE_KEYS["playerTeam"]:
        name_and_team = td.find_element_by_css_selector("td em")
        return (name_and_team.get_attribute("innerHtml").split("-")[0].strip()
                if key == OFFENSE_KEYS["playerPos"]
                else name_and_team.get_attribute("innerHtml").split("-")[1].strip())

    if key == OFFENSE_KEYS["opp"]:
        return td.find_element_by_css_selector("td a").get_attribute("innerHtml")

    if key == OFFENSE_KEYS["gameDetails"]:
        date_and_time = td.find_elements_by_css_selector("td span")
        return date_and_time[0].get_attribute("innerHtml") + date_and_time[1].get_attribute("innerHtml") + ""

    element = td.find_element_by_css_selector("td span")
    return element.get_attribute("innerHtml")
