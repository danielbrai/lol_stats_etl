from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.objectives_type.GetObjectiveTypeInfoFromDatabaseUseCase import \
    GetObjectiveTypeInfoFromDatabaseUseCase
from src.core.usecase.objectives_type.ObjectiveTypeModel import ObjectiveTypeModel


class SaveObjectiveTypeInfoInDatabaseUseCase:

    def __init__(self,
                 repository: DatabaseRepositoryConstraint,
                 get_role_info_from_database_use_case: GetObjectiveTypeInfoFromDatabaseUseCase):
        self.repository = repository
        self.get_role_info_from_database_use_case = get_role_info_from_database_use_case

    def execute(self, name: str):
        name = name.strip().upper()
        saved_name = self.get_role_info_from_database_use_case.execute(name)

        if saved_name:
            return saved_name.id
        else:
            objective_type = ObjectiveTypeModel(id=None, name=name)
            return self.repository.save_objective_type_in_database(objective_type)
