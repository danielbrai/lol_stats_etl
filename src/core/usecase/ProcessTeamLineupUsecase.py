from src.core.usecase.RetrieveLeagueInfoUsecase import RetrieveLeagueInfoUsecase
from src.core.usecase.SaveTeamsLineUpInDatabaseUsecase import SaveTeamsLineupInDatabaseUsecase


class ProcessTeamLineupUsecase:

    def __init__(self, retrieve_league_info_usecase: RetrieveLeagueInfoUsecase,
                 save_teams_lineup_usecase: SaveTeamsLineupInDatabaseUsecase):
        self.retrieve_league_info_usecase = retrieve_league_info_usecase
        self.save_teams_lineup_usecase = save_teams_lineup_usecase

    def execute(self, league_file_name):
        test_json = self.retrieve_league_info_usecase.execute(league_file_name)
        self.save_teams_lineup_usecase.execute(test_json)
