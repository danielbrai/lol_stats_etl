from typing import List

from src.core.usecase.line_up.teams.TeamModel import TeamModel


class LeagueModel:

    def __init__(self, season: int, split: int, teams: List[TeamModel]):
        self.season = season
        self.split = split
        self.teams = teams
