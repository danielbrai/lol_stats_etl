from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint
from src.core.usecase.game_types.GameTypeModel import GameTypeModel


class RetrieveGameTypesInfoUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint, repository: DatabaseRepositoryConstraint):
        self.dataprovider = dataprovider
        self.repository = repository

    def execute(self):
        response = self.dataprovider.get_game_types_data()
        game_types = response.json()
        return list(GameTypeModel(game_type=game_type['gametype'], description=game_type['description']) for game_type in game_types)
