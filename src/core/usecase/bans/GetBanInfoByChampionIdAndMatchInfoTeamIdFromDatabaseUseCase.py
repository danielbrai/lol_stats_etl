from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetBanInfoByChampionIdAndMatchInfoTeamIdFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, champion_id: int, match_info_team_id: int):
        return self.repository.get_ban_info_by_champion_id_and_match_info_team_id(champion_id=champion_id, match_info_team_id=match_info_team_id)
