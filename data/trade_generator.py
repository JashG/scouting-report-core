import json
from config import config


def create_trades(sending_team, receiving_team):
    trades = []

    # Generate one-for-ones
    for player1 in sending_team:
        player1_value = player1["playerValue"]
        if player1["playerPos"] == "QB":
            player1_value = int(round(int(player1_value) * 1.5))

        # Find potential partners
        for player2 in receiving_team:
            player2_value = player2["playerValue"]
            if player2["playerPos"] == "QB":
                player2_value = int(round(int(player2_value) * 1.5))

            if abs(int(player1_value) - int(player2_value)) <= 2:
                trades.append(dict(
                    send=[player1],
                    receive=[player2]
                ))

    return trades


def trade_generator():
    curr_team = 1
    num_teams = len(config.TEAM_MAP)
    all_rosters = []
    # Load all rosters from JSON
    while curr_team <= num_teams:
        with open("data/db/roster_" + str(curr_team) + ".json", newline="") as curr_team_file:
            curr_team_roster = json.load(curr_team_file)
            # Sort players by trade value
            curr_team_players = curr_team_roster["players"]
            curr_team_roster_sorted = sorted(curr_team_players,
                                             key=lambda item: item["playerValue"],
                                             reverse=True
                                             )
            all_rosters.append(curr_team_roster_sorted)

        curr_team += 1
        # Reset this variable - for some reason, the previous data remains in memory
        curr_team_roster = dict()

    # Each value in the list is a dict of the players sent vs. received
    all_trades = []
    curr_team = 1
    while curr_team <= num_teams:
        trades_for_curr_team = []
        for i in range(1, num_teams + 1):
            if i == curr_team:
                continue
            trades_for_curr_team = trades_for_curr_team + create_trades(all_rosters[curr_team - 1], all_rosters[i-1])

        all_trades.append(trades_for_curr_team)
        curr_team += 1

    return all_trades
    # print(json.dumps(all_trades, indent=4))


data = trade_generator()

for idx, team in enumerate(data):
    print("Team " + str(idx + 1) + " trades")
    # Write trade to file
    with open("data/db/team" + str(idx + 1) + "/trades.json", "w") as file:
        file.write(json.dumps(team, indent=4))
    for trade in team:
        send1 = trade.get("send")[0]["playerName"]
        # send2 = trade.get("send")[1]["playerName"]
        get1 = trade.get("receive")[0]["playerName"]
        # get2 = trade.get("receive")[1]["playerName"]
        print("Send: ")
        print(send1)
        # print(send2)
        print("Get: ")
        print(get1)
        # print(get2)
        print("\n")

# Analyze results
