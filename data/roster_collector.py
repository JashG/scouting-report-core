import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import config
from utils.collector_utils import parse_team_roster_page, create_team_roster


def get_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=options)
    return driver


def main():
    # Collect each team's stats for the current week
    driver = get_driver()

    curr_team = 1
    num_teams = len(config.TEAM_MAP)

    # Fetch and store each team's roster in a JSON obj
    # Stores the up-to-date roster with season stats up to this week for each player
    while curr_team <= num_teams:
        print("Fetching team " + str(curr_team))
        # Navigate to URL for the given team ID
        driver.get(config.TEAM_URL + str(curr_team) + config.TEAM_URL_YEARLY_STATS)
        # List of <tr> elements, where each row is a player
        team_players_html = parse_team_roster_page(driver, is_yearly_page=True)
        # Parses each <tr> into a Player, and stores the list of Players in a Roster
        team_roster = create_team_roster(curr_team, team_players_html)
        # Convert the Roster to JSON, which we will save to a file
        team_roster_json = team_roster.to_json() if team_roster is not None else None

        if team_roster_json is not None:
            with open("data/db/" + "roster_" + str(curr_team) + ".json", "w") as file:
                file.write(team_roster_json)

        curr_team += 1
        # Sleep before navigating to next team's URL
        time.sleep(5)


main()
