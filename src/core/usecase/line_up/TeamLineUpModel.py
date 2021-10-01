from typing import List

from src.core.usecase.line_up.player.PlayerModel import PlayerModel
from src.core.usecase.line_up.teams.TeamModel import TeamModel


class TeamLineUpModel:

    def __init__(self, team: TeamModel, lineup: List[PlayerModel]):
        self.team = team
        self.lineup = lineup
