from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.game_modes.GameModeModel import GameModeModel


class SaveGameModesDataInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, items_data: List[GameModeModel]):
        self.repository.save_game_modes_in_database(items_data)
