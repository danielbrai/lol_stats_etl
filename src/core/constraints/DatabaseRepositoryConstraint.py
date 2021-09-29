import abc
from typing import List

from src.core.usecase.TeamModel import TeamModel
from src.core.usecase.champions.ChampionModel import ChampionModel
from src.core.usecase.game_modes.GameModeModel import GameModeModel
from src.core.usecase.game_types.GameTypeModel import GameTypeModel
from src.core.usecase.items.ItemModel import ItemModel
from src.core.usecase.maps.MapModel import MapModel
from src.core.usecase.platforms.PlatformModel import PlatformModel
from src.core.usecase.queues.QueueModel import QueueModel


class DatabaseRepositoryConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_teams(self, teams: List[TeamModel]):
        pass

    @abc.abstractmethod
    def save_player(self, player: str, team_id: int, season: int, split: int):
        pass

    @abc.abstractmethod
    def get_team_id(self, team_name: str):
        pass

    @abc.abstractmethod
    def save_champions_in_database(self, champions_data: List[ChampionModel]):
        pass

    @abc.abstractmethod
    def save_items_in_database(self, champions_data: List[ItemModel]):
        pass

    @abc.abstractmethod
    def save_maps_in_database(self, champions_data: List[MapModel]):
        pass

    @abc.abstractmethod
    def save_queue_in_database(self, champions_data: List[QueueModel]):
        pass

    @abc.abstractmethod
    def get_map_by_name(self, map_name: str):
        pass

    @abc.abstractmethod
    def save_game_modes_in_database(self, game_modes_data: List[GameModeModel]):
        pass

    @abc.abstractmethod
    def save_game_types_in_database(self, game_types: List[GameTypeModel]):
        pass

    @abc.abstractmethod
    def save_platform_in_database(self, platform_data: List[PlatformModel]):
        pass





