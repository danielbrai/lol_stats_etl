from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetPlayersPuuidFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self):
        return self.repository.get_players_puuid()
