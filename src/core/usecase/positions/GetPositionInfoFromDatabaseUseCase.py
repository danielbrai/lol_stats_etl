from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetPositionInfoFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, position_name: str):
        return self.repository.get_position_by_name(position_name)
