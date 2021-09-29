from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.game_types.GameTypeModel import GameTypeModel


class SaveGameTypesDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, items_data: List[GameTypeModel]):
        self.repository.save_game_types_in_database(items_data)
