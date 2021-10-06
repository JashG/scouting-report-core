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
# Wait for these elements to confirm the TEAM_URL page has loaded
TEAM_SELECTOR = "#quickinfo_teamselector"
YEARLY_STATS_BTN = "li#st2021"
# We will navigate through each of these sections that make up a roster
ROSTER_NAVIGATION = dict(
    OFFENSE="#tableWrap-O tr",
    KICKER="#tableWrap-K tr",
    DEFENSE="#tableWrap-DT tr"
)
# If viewing the matchup screen, both rosters are shown on the same screen.
# So, navigate a bit differently
ROSTER_NAVIGATION_MATCHUP = dict(
    OFFENSE_TOP=".teamWrap-1 #tableWrap-O tr",
    OFFENSE_BOTTOM=".teamWrap-2 #tableWrap-O tr",
    KICKER_TOP=".teamWrap-1 #tableWrap-K tr",
    KICKER_BOTTOM=".teamWrap-2 #tableWrap-K tr",
    DEFENSE_TOP=".teamWrap-1 #tableWrap-DT",
    DEFENSE_BOTTOM=".teamWrap-2 #tableWrap-DT"
)

COMMON_PLAYER_DATA_KEYS = [
    "teamPos",
    "",
    [
        "playerName",
        "playerPos",
        "playerTeam"
    ],
    "opp",
    "gameDetails",
]
# Each index, n, maps to the data represented by the n + 1 column in the roster table
# Each value is the key we will use to represent the data in that column
# If a value is empty, we don't need the data in that column
PLAYER_DATA_KEYS = dict(
    OFFENSE=[
        *COMMON_PLAYER_DATA_KEYS,
        "passYards",
        "passTD",
        "passInt",
        "rushYards",
        "rushTD",
        "rec",
        "recYards",
        "recTD",
        "retTD",
        "",
        "twoPtConv",
        "fumbles",
        "fantasyPts"
    ],
    KICKER=[
        *COMMON_PLAYER_DATA_KEYS,
        "pats",
        "fg0_19",
        "fg20_29",
        "fg30_39",
        "fg40_49",
        "fg50",
        "fantasyPts"
    ],
    DEFENSE=[
        *COMMON_PLAYER_DATA_KEYS,
        "sacks",
        "int",
        "fumRec",
        "fumForced",
        "safety",
        "td",
        "block",
        "retTD",
        "ptsAllow",
        "yardsAllow",
        "fantasyPts"
    ]
)
