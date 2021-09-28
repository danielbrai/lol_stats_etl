from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.LeagueModel import LeagueModel


class SaveTeamsInfoInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, league_info: LeagueModel):
        teams = []
        for team in league_info.teams:
            teams.append(team.name)
        self.repository.save_teams(teams)