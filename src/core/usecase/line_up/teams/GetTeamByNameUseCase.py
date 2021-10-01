from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.line_up.teams.TeamModel import TeamModel


class GetTeamByNameUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, team_name: str) -> TeamModel:
        return self.repository.get_team_by_name(team_name)
