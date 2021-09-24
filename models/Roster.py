from models import Player
from config.config import TEAM_MAP

class Roster:

    def __init__(self,
                 team_id: int,
                 players: [] = []
                 ):
        self.team_id = team_id
        if 1 <= team_id <= len(TEAM_MAP):
            self.team_name = TEAM_MAP[team_id - 1]
        self.players = players

    def add_player(self, player: Player):
        if player:
            self.players.append(player)

    def num_players(self):
        return len(self.players)

    def to_json(self):
        output = dict(
            team_id=self.team_id,
            team_name=self.team_name,
            week=self.week,
            players=[]
        )

        for player in self.players:
            if player and isinstance(player, Player):
                output["players"].append(player.to_json())
