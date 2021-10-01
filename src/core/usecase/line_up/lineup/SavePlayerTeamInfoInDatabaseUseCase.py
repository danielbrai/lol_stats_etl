from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.line_up.lineup.PlayerTeamModel import PlayerTeamModel


class SavePlayerTeamInfoInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, player_team: PlayerTeamModel):
        if player_team.player_id:
            self.repository.save_team_player_info_in_database(player_team)
