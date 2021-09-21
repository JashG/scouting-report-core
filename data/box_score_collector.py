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


def get_driver():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=options)
    return driver


# Process team stats for the given week
def handle_weekly_box_scores(driver):
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
        tm = matchup.find_element_by_css_selector(constants.MATCHUP_NAVIGATION["TEAM_FIRST"])
        pts = matchup.find_element_by_css_selector(constants.MATCHUP_NAVIGATION["POINTS_FIRST"])
        print(tm.text)
        print(pts.text)


def main():
    # Collect each team's stats for the current week
    driver = get_driver()
    driver.get(config.GAMECENTER_URL)

    # Wait for navbar that allows us to toggle to "Box Score" to load
    WebDriverWait(driver, constants.TIMEOUT_DEFAULT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, constants.GAMECENTER_BOX_SCORE))
    )

    handle_weekly_box_scores(driver)


main()
