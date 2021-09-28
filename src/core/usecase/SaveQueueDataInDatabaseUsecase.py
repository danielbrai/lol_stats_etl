from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.models.Champion import Champion
from src.core.models.Queue import Queue


class SaveQueueDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, queue_data: List[Queue]):
        return self.repository.save_queue_in_database(queue_data)
