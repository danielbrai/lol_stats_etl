from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint
from src.core.usecase.game_modes.GameModeModel import GameModeModel


class RetrieveGameModesInfoUseCase:

    def __init__(self, dataprovider: RiotRestClientConstraint, repository: DatabaseRepositoryConstraint):
        self.dataprovider = dataprovider
        self.repository = repository

    def execute(self):
        response = self.dataprovider.get_game_modes_data()
        game_modes = response.json()
        return list(GameModeModel(game_mode=game_mode['gameMode'], description=game_mode['description']) for game_mode in game_modes)