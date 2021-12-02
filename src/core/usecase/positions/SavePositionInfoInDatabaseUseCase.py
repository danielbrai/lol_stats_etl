from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.positions import GetPositionInfoFromDatabaseUseCase
from src.core.usecase.positions.PositionModel import PositionModel


class SavePositionInfoInDatabaseUseCase:

    def __init__(self,
                 repository: DatabaseRepositoryConstraint,
                 get_position_info_from_database_use_case: GetPositionInfoFromDatabaseUseCase):
        self.repository = repository
        self.get_position_info_from_database_use_case = get_position_info_from_database_use_case

    def execute(self, position_name: str):
        position_name = position_name.strip().upper()
        saved_position = self.get_position_info_from_database_use_case.execute(position_name)

        if saved_position:
            return saved_position.id
        else:
            position = PositionModel(id=None, position=position_name)
            return self.repository.save_position_in_database(position)

