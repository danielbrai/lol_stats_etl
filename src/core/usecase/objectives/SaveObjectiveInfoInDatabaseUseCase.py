from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.objectives.GetObjectivesInfoByObjectiveTypeIdAndMatchInfoTeamIdFromDatabaseUseCase import \
    GetObjectivesInfoByObjectiveTypeIdAndMatchInfoTeamIdFromDatabaseUseCase
from src.core.usecase.objectives.ObjectiveModel import ObjectiveModel


class SaveObjectiveInfoInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint,
                 get_objectives_by_objective_type_id_and_match_info_team_id_use_case: GetObjectivesInfoByObjectiveTypeIdAndMatchInfoTeamIdFromDatabaseUseCase):
        self.repository = repository
        self.get_objectives_by_objective_type_id_and_match_info_team_id_use_case = get_objectives_by_objective_type_id_and_match_info_team_id_use_case

    def execute(self, objective: ObjectiveModel):

        saved_objective = self.get_objectives_by_objective_type_id_and_match_info_team_id_use_case.execute(
            objective_type_id=objective.objective_type_id, match_info_team_id=objective.match_info_team_id)

        if saved_objective:
            return saved_objective.id
        else:
            return self.repository.save_objective_in_database(objective)
