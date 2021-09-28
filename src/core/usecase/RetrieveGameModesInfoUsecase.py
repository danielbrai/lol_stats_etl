import os
from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.constraints.JsonConsumerConstarint import JsonConsumerConstraint
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint
from src.core.models.GameMode import GameMode
from src.core.models.Map import Map
from src.core.models.Queue import Queue


class RetrieveGameModesInfoUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint, repository: DatabaseRepositoryConstraint):
        self.dataprovider = dataprovider
        self.repository = repository

    def execute(self):
        response = self.dataprovider.get_game_modes_data()
        game_modes = response.json()
        return list(GameMode(game_mode=game_mode['gameMode'], description=game_mode['description']) for game_mode in game_modes)