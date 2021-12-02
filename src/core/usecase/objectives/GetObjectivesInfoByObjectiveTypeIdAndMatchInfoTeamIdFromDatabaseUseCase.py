from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetObjectivesInfoByObjectiveTypeIdAndMatchInfoTeamIdFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, objective_type_id: int, match_info_team_id: int):
        return self.repository.get_objective_by_objective_type_id_and_match_info_team_id(objective_type_id,
                                                                                         match_info_team_id)
