from typing import List

from src.core.usecase.line_up.TeamLineUpModel import TeamLineUpModel


class ChampionshipModel:

    def __init__(self, season: int, split: int, line_up: List[TeamLineUpModel]):
        self.season = season
        self.split = split
        self.line_up = line_up
