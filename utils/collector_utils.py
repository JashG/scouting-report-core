from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from config import config, constants
from models.Player import Player
from models.Roster import Roster


# Process team stats for the given week
def parse_team_roster_page(driver, is_yearly_page=False):
    if is_yearly_page:
        # Wait for the DOM to finish loading elements we need
        WebDriverWait(driver, constants.TIMEOUT_DEFAULT).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, constants.TEAM_SELECTOR))
        )

        WebDriverWait(driver, constants.TIMEOUT_DEFAULT).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, constants.YEARLY_STATS_BTN))
        )

    try:
        offense = driver.find_elements_by_css_selector(constants.ROSTER_NAVIGATION.get("OFFENSE"))
        kickers = driver.find_elements_by_css_selector(constants.ROSTER_NAVIGATION.get("KICKER"))
        defense = driver.find_elements_by_css_selector(constants.ROSTER_NAVIGATION.get("DEFENSE"))
        return dict(
            offense=offense,
            kickers=kickers,
            defense=defense
        )
    except NoSuchElementException as e:
        print(e)
        exit(1)


def create_team_roster(curr_team, roster: dict):
    roster_obj = Roster(curr_team, config.CURRENT_WEEK)

    for player in roster.get("offense"):
        player_data_html = player.find_elements_by_tag_name("td")
        if player_data_html:
            roster_obj.add_player(Player(player_data_html, "OFFENSE"))

    return roster_obj
