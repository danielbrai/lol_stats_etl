from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.roles.GetRoleInfoFromDatabaseUseCase import GetRoleInfoFromDatabaseUseCase
from src.core.usecase.roles.RoleModel import RoleModel


class SaveRoleInfoInDatabaseUseCase:

    def __init__(self,
                 repository: DatabaseRepositoryConstraint,
                 get_role_info_from_database_use_case: GetRoleInfoFromDatabaseUseCase):
        self.repository = repository
        self.get_role_info_from_database_use_case = get_role_info_from_database_use_case

    def execute(self, role: str):
        role = role.strip().upper()
        saved_position = self.get_role_info_from_database_use_case.execute(role)

        if saved_position:
            return saved_position
        else:
            position = RoleModel(id=None, role=role)
            a = self.repository.save_role_in_database(position)
            return a
