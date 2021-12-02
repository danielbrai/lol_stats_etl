from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetChampionByRiotIdUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, riot_id: str):
        return self.repository.get_champion_by_riot_id(riot_id)
