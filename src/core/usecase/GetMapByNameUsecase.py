import os

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.constraints.JsonConsumerConstarint import JsonConsumerConstraint
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint
from src.core.models.Map import Map


class GetMapByNameUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, map_name: str):
        return self.repository.get_map_by_name(map_name)
