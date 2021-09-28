from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetMapByNameUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, map_name: str):
        return self.repository.get_map_by_name(map_name)
