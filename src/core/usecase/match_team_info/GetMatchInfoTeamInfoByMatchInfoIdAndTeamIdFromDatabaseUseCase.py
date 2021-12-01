from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetMatchInfoTeamInfoByMatchInfoIdAndTeamIdFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, match_info_id: int, team_id: int):
        return self.repository.get_match_team_info_by_match_info_id_and_team_id(match_info_id, team_id)
