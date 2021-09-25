from selenium.webdriver.remote.webelement import WebElement
from config.config import NFL_TEAM_LOGO_SRC


def get_nfl_team_logo_src(team_abbr):
    if team_abbr:
        return NFL_TEAM_LOGO_SRC.replace("_x", "_" + team_abbr)

    return ""
