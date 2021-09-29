import json
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Project dependencies
from config import config, secrets, constants
from utils.collector_utils import parse_team_roster_page, create_team_roster


def get_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=options)
    return driver


# Process team stats for the given week
def collect_weekly_box_scores(driver):
    # Click to toggle box score
    try:
        box_score_link = driver.find_element_by_css_selector(constants.GAMECENTER_BOX_SCORE)
    except NoSuchElementException as e:
        print(e)
        exit(1)
    box_score_link.click()

    # For each matchup this week, collect each team's stats
    try:
        all_matchups = driver.find_elements_by_css_selector(constants.MATCHUP_NAVIGATION["CONTAINER"])
    except NoSuchElementException as e:
        print(e)
        exit(1)

    for matchup in all_matchups:
        # Parse player stats for both teams in this matchup
        tm = matchup.find_element_by_css_selector(constants.MATCHUP_NAVIGATION["TEAM_FIRST"])
        pts = matchup.find_element_by_css_selector(constants.MATCHUP_NAVIGATION["POINTS_FIRST"])
        print(tm.text)
        print(pts.text)

    # List of <tr> elements, where each row is a player
    team_players_html = parse_team_roster_page(driver)
    # Parses each <tr> into a Player, and stores the list of Players in a Roster
    team_roster = create_team_roster(1, team_players_html)
    # Convert the Roster to JSON, which we will save to a file
    team_roster_json = team_roster.to_json() if team_roster is not None else None

    if team_roster_json is not None:
        with open("data/db/team1/week_1.json", "w") as file:
            file.write(team_roster_json)


def main():
    # Collect each team's stats for the current week
    driver = get_driver()
    driver.get(config.GAMECENTER_URL)

    # Wait for navbar that allows us to toggle to "Box Score" to load
    WebDriverWait(driver, constants.TIMEOUT_DEFAULT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, constants.GAMECENTER_BOX_SCORE))
    )

    collect_weekly_box_scores(driver)


main()
