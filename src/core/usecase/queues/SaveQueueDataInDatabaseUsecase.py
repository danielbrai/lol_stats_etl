from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.queues.QueueModel import QueueModel


class SaveQueueDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, queue_data: List[QueueModel]):
        self.repository.save_queue_in_database(queue_data)
