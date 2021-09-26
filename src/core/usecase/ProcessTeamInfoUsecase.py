from src.core.usecase.RetrieveLeagueInfoUsecase import RetrieveLeagueInfoUsecase
from src.core.usecase.SaveTeamsInfoInDatabaseUsecase import SaveTeamsInfoInDatabaseUsecase


class ProcessTeamInfoUsecase:

    def __init__(self, retrieve_league_info_usecase: RetrieveLeagueInfoUsecase,
                 save_teams_info_usecase: SaveTeamsInfoInDatabaseUsecase):
        self.retrieve_league_info_usecase = retrieve_league_info_usecase
        self.save_teams_info_usecase = save_teams_info_usecase

    def execute(self, league_file_name):
        test_json = self.retrieve_league_info_usecase.execute(league_file_name)
        self.save_teams_info_usecase.execute(test_json)
