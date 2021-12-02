from src.core.constraints import DatabaseRepositoryConstraint
from src.core.usecase.match_participants.GetMatchParticipantInfoFromDatabaseUseCase import GetMatchParticipantInfoFromDatabaseUseCase
from src.core.usecase.match_participants.MatchPlayerDetailsModel import MatchPlayerDetailsModel


class SaveMatchPlayerDetailsUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint, get_match_participant_info_from_database_use_case: GetMatchParticipantInfoFromDatabaseUseCase):
        self.get_match_participant_info_from_database_use_case = get_match_participant_info_from_database_use_case
        self.repository = repository

    def execute(self, match_participant: MatchPlayerDetailsModel):
        saved_match_participant = self.get_match_participant_info_from_database_use_case.execute(match_participant.champion_id, match_participant.team_position_id, match_participant.individual_position_id,
                                                                                                 match_participant.role_id, match_participant.match_info_team_id, match_participant.player_id)

        if saved_match_participant:
            return saved_match_participant.id
        else:
            return self.repository.save_match_player_details(match_participant)
