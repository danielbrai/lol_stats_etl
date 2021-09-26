from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.models.Item import Item


class SaveMapsDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, items_data: List[Item]):
        return self.repository.save_maps_in_database(items_data)