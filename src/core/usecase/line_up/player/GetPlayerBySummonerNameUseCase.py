from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetPlayerBySummonerNameUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, summoner_name: str):
        return self.repository.get_player_by_summoner_name(summoner_name)
