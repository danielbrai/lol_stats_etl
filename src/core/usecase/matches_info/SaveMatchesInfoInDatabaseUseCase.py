from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.matches_info.MatchInfoModel import MatchInfoModel


class SaveMatchesInfoInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, match_info: MatchInfoModel):
        return self.repository.save_match_info_in_database(match_info)
