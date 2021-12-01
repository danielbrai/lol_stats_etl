from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetPlatformByNameUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, platform_name: str):
        a = self.repository.get_game_platform_by_name(platform_name)
        return a

