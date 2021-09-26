import csv
import json
from config import config

all_player_trade_values = dict()

# Map player name to their trade value
with open("data/db/player_values.csv", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        if len(row) == 3:
            player = row[0]
            player_name = " ".join(player.split(" ")[:-1])
            value = row[2]
            all_player_trade_values[player_name] = value

curr_team = 1
num_teams = len(config.TEAM_MAP)

# Append trade value as a field to each player
while curr_team < num_teams:
    # 1) Dump current team's roster into a dict
    curr_team_dict = dict()
    try:
        with open("data/db/roster_" + str(curr_team) + ".json", newline="") as curr_team_file:
            curr_team_dict = json.load(curr_team_file)
    except ValueError:
        continue

    # 2) Get value for each player
    players = curr_team_dict.get("players") or []
    for player in players:
        player_name = player.get("playerName", "")
        if player_name:
            player_value = all_player_trade_values.get(player_name, "0")
            player["playerValue"] = player_value

    # 3) Write back to json
    try:
        with open("data/db/roster_" + str(curr_team) + ".json", "w") as curr_team_file:
            json.dump(curr_team_dict, curr_team_file, indent=4)
    except ValueError:
        pass

    curr_team += 1
