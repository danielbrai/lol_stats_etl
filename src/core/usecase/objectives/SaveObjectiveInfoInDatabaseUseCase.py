from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.objectives.ObjectiveModel import ObjectiveModel


class SaveObjectiveInfoInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, objective: ObjectiveModel):
        return self.repository.save_objective_in_database(objective)
