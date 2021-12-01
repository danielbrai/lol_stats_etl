from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.match_team_info.GetMatchInfoTeamInfoByMatchInfoIdAndTeamIdFromDatabaseUseCase import \
    GetMatchInfoTeamInfoByMatchInfoIdAndTeamIdFromDatabaseUseCase
from src.core.usecase.match_team_info.MatchTeamInfoModel import MatchTeamInfoModel


class SaveMatchTeamInfoInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint,
                 get_match_team_info_by_match_info_id_and_team_id_from_database_use_case: GetMatchInfoTeamInfoByMatchInfoIdAndTeamIdFromDatabaseUseCase):
        self.repository = repository
        self.get_match_team_info_by_match_info_id_and_team_id_from_database_use_case = get_match_team_info_by_match_info_id_and_team_id_from_database_use_case

    def execute(self, match_team_info: MatchTeamInfoModel):
        match_team_info_saved = self.get_match_team_info_by_match_info_id_and_team_id_from_database_use_case.execute(match_team_info.match_info_id, match_team_info.team_id)

        if match_team_info_saved:
            return match_team_info_saved.id
        else:
            return self.repository.save_match_team_info_in_database(match_team_info)
