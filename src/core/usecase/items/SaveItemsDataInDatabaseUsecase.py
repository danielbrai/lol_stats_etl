from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.items.ItemModel import ItemModel


class SaveItemsDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, items_data: List[ItemModel]):
        self.repository.save_items_in_database(items_data)
