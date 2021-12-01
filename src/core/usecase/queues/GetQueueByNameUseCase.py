from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetQueueByNameUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, game_type: str):
        a = self.repository.get_queue_by_name(game_type)
        return a

