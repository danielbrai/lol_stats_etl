from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.models.League import League


class SaveTeamsInfoInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, league_info: League):
        teams = []
        for team in league_info.teams:
            teams.append(team.name)
        self.repository.save_teams(teams)