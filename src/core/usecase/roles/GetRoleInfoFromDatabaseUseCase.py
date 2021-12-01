from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetRoleInfoFromDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, role: str):
        return self.repository.get_role_by_name(role)
