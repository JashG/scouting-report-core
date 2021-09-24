import json
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config, secrets, constants
from models.Player import Player
from models.Roster import Roster


def get_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=options)
    return driver


# Process team stats for the given week
def parse_team_roster_page(driver, team_id):
    # Navigate to URL for the given team ID
    driver.get(config.TEAM_URL + str(team_id))

    # Wait for the DOM to finish loading
    WebDriverWait(driver, constants.TIMEOUT_DEFAULT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, constants.TEAM_SELECTOR))
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


def create_team_roster(driver, curr_team, roster: dict):
    roster_obj = Roster(curr_team, config.CURRENT_WEEK)

    for player in roster.get("offense"):
        player_data_html = player.find_elements_by_tag_name("td")
        if player_data_html:
            roster_obj.add_player(Player(player_data_html, "OFFENSE"))

    return roster_obj


def main():
    # Collect each team's stats for the current week
    driver = get_driver()

    curr_team = 1
    num_teams = len(config.TEAM_MAP)

    while curr_team <= num_teams:
        team_players_html = parse_team_roster_page(driver, curr_team)
        print("Generating team roster")
        team_roster = create_team_roster(driver, curr_team, team_players_html)


main()
