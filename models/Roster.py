import json
from models import Player
from config.config import TEAM_MAP


class Roster:

    def __init__(self,
                 team_id: int,
                 week: int,
                 players: [] = []
                 ):
        self.team_id = team_id
        self.week = week

        if 1 <= team_id <= len(TEAM_MAP):
            self.team_name = TEAM_MAP[team_id - 1]
        self.players = players or []

    def add_player(self, player: Player):
        if player:
            self.players.append(player)

    def num_players(self):
        return len(self.players)

    def get_basic_json(self):
        output = dict(
            team_id=self.team_id,
            team_name=self.team_name,
            week=self.week,
            players=[]
        )

        player: Player
        print("Getting roster for team " + str(self.team_id))
        for player in self.players:
            next_player = player.get_basic_json(True)
            output["players"].append(next_player)

        return json.dumps(output, indent=4)
