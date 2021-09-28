from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.maps.MapModel import MapModel


class SaveMapsDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, items_data: List[MapModel]):
        self.repository.save_maps_in_database(items_data)
