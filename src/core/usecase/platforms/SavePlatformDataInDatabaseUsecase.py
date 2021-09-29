from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.platforms.PlatformModel import PlatformModel


class SavePlatformDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, platform_data: List[PlatformModel]):
        self.repository.save_platform_in_database(platform_data)
