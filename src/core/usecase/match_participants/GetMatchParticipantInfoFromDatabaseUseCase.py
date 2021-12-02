from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetMatchParticipantInfoFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, champion_id: int, team_position_id: int, individual_position_id: int, role_id: int, match_info_team_id:int, player_id: int):
        return self.repository.get_match_participant_by_relations_ids(champion_id, team_position_id, individual_position_id, role_id, match_info_team_id, player_id)


