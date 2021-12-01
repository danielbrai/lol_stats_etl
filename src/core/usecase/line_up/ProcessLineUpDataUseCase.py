from src.core.usecase.line_up.RetrieveChampionshipInfoUseCase import RetrieveChampionshipInfoUseCase
from src.core.usecase.line_up.lineup.PlayerTeamModel import PlayerTeamModel
from src.core.usecase.line_up.lineup.SavePlayerTeamInfoInDatabaseUseCase import SavePlayerTeamInfoInDatabaseUseCase
from src.core.usecase.line_up.player.SavePlayerDataInDatabaseUseCase import SavePlayerDataInDatabaseUseCase
from src.core.usecase.line_up.teams.GetTeamByNameUseCase import GetTeamByNameUseCase
from src.core.usecase.line_up.teams.SaveTeamDataInDatabaseUseCase import SaveTeamDataInDatabaseUseCase


class ProcessLineUpDataUseCase:

    def __init__(self,
                 retrieve_championship_info_use_case: RetrieveChampionshipInfoUseCase,
                 save_team_in_database_use_case: SaveTeamDataInDatabaseUseCase,
                 get_team_by_name_use_case: GetTeamByNameUseCase,
                 save_player_use_case: SavePlayerDataInDatabaseUseCase,
                 save_player_team_info_in_database_use_case: SavePlayerTeamInfoInDatabaseUseCase):
        self.save_player_team_info_in_database_use_case = save_player_team_info_in_database_use_case
        self.save_player_use_case = save_player_use_case
        self.get_team_by_name_use_case = get_team_by_name_use_case
        self.save_team_in_database_use_case = save_team_in_database_use_case
        self.retrieve_championship_info_use_case = retrieve_championship_info_use_case

    def execute(self):
        championship = self.retrieve_championship_info_use_case.execute()
        for line_up in championship.line_up:
            team_in_database = self.get_team_by_name_use_case.execute(line_up.team.name)
            if not team_in_database:
                line_up.team.id = self.save_team_in_database_use_case.execute(line_up.team)
            else:
                line_up.team = team_in_database
            for player in line_up.lineup:
                player = self.save_player_use_case.execute(player)
                player_team_info = PlayerTeamModel(player.id, line_up.team.id, championship.season, championship.split)
                self.save_player_team_info_in_database_use_case.execute(player_team_info)

        return championship
