from typing import List

from src.core.models.Team import Team


class League:

    def __init__(self, season: int, split: int, teams: List[Team]):
        self.season = season
        self.split = split
        self.teams = teams
