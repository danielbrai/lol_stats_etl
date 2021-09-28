from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.models.Champion import Champion


class SaveChampionsDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, champions_data: List[Champion]):
        self.repository.save_champions_in_database(champions_data)
