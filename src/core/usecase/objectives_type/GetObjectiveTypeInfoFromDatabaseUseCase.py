from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetObjectiveTypeInfoFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, objective: str):
        return self.repository.get_objective_type_by_name(objective)
