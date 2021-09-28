import abc
from typing import List

from src.core.models.Champion import Champion
from src.core.models.Item import Item
from src.core.models.Map import Map
from src.core.models.Queue import Queue
from src.core.models.Team import Team


class DatabaseRepositoryConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_teams(self, teams: List[Team]):
        return

    @abc.abstractmethod
    def save_player(self, player: str, team_id: int, season: int, split: int):
        return

    @abc.abstractmethod
    def get_team_id(self, team_name: str):
        return

    @abc.abstractmethod
    def save_champions_in_database(self, champions_data: List[Champion]):
        pass

    @abc.abstractmethod
    def save_items_in_database(self, champions_data: List[Item]):
        pass

    @abc.abstractmethod
    def save_maps_in_database(self, champions_data: List[Map]):
        pass

    @abc.abstractmethod
    def save_queue_in_database(self, champions_data: List[Queue]):
        pass

    @abc.abstractmethod
    def get_map_by_name(self, map_name):
        pass





