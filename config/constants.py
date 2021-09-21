"""
Selenium constants
"""
# Default timeout (in seconds) to wait for DOM elements to load
TIMEOUT_DEFAULT = 30

"""
Relevant CSS selectors
"""
# CSS to toggle the full box score
GAMECENTER_BOX_SCORE = "li#ptFbs"
# CSS for the elements in the navigation pane that allow us to toggle between matchups
MATCHUP_NAVIGATION = dict(
    CONTAINER="ul.ss.ss-6 > li",
    TEAM_FIRST="div.first > em",
    POINTS_FIRST="div.first > span",
    TEAM_LAST="div.last > em",
    POINTS_LAST="div.last > span"
)
