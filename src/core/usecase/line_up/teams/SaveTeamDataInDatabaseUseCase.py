from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.line_up.teams.TeamModel import TeamModel


class SaveTeamDataInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, team: TeamModel):
        return self.repository.save_team_info_in_database(team)
