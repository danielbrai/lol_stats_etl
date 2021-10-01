from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.LeagueModel import LeagueModel


class SaveTeamsLineupInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, league_info: LeagueModel):

        for team in league_info.teams:
            team_id = self.repository.get_team_id(team.summoner_name)
            for player in team.lineup:
                self.repository.save_player(player, team_id, league_info.season, league_info.split)
        self.repository.save_teams(None)
