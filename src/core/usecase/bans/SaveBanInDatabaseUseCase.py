from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.bans.BanModel import BanModel
from src.core.usecase.bans.GetBanInfoByChampionIdAndMatchInfoTeamIdFromDatabaseUseCase import \
    GetBanInfoByChampionIdAndMatchInfoTeamIdFromDatabaseUseCase


class SaveBanInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint,
                 get_ban_info_by_champion_id_and_match_info_team_id_from_database_use_case: GetBanInfoByChampionIdAndMatchInfoTeamIdFromDatabaseUseCase):
        self.repository = repository
        self.get_ban_info_by_champion_id_and_match_info_team_id_from_database_use_case = get_ban_info_by_champion_id_and_match_info_team_id_from_database_use_case

    def execute(self, ban: BanModel):
        ban_info_saved = self.get_ban_info_by_champion_id_and_match_info_team_id_from_database_use_case.execute(
            ban.champion_id, ban.match_info_team_id)

        if ban_info_saved:
            return ban_info_saved.id
        else:
            return self.repository.save_ban_in_database(ban)
