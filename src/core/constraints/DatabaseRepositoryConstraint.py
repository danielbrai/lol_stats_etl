import abc
from typing import List

from src.core.usecase.bans.BanModel import BanModel
from src.core.usecase.champions.ChampionModel import ChampionModel
from src.core.usecase.game_modes.GameModeModel import GameModeModel
from src.core.usecase.game_types.GameTypeModel import GameTypeModel
from src.core.usecase.items.ItemModel import ItemModel
from src.core.usecase.line_up.lineup.PlayerTeamModel import PlayerTeamModel
from src.core.usecase.match_participants.MatchPlayerDetailsModel import MatchPlayerDetailsModel
from src.core.usecase.line_up.player.PlayerModel import PlayerModel
from src.core.usecase.maps.MapModel import MapModel
from src.core.usecase.matches_info.MatchInfoModel import MatchInfoModel
from src.core.usecase.objectives_type.ObjectiveTypeModel import ObjectiveTypeModel
from src.core.usecase.platforms.PlatformModel import PlatformModel
from src.core.usecase.positions.PositionModel import PositionModel
from src.core.usecase.queues.QueueModel import QueueModel


class DatabaseRepositoryConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_player(self, player: PlayerModel):
        pass

    @abc.abstractmethod
    def get_team_id(self, team_name: str):
        pass

    @abc.abstractmethod
    def save_champions_in_database(self, champions_data: ChampionModel):
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

    @abc.abstractmethod
    def save_team_info_in_database(self, team):
        pass

    @abc.abstractmethod
    def get_team_by_name(self, team):
        pass

    @abc.abstractmethod
    def save_team_player_info_in_database(self, player_team: PlayerTeamModel):
        pass

    @abc.abstractmethod
    def get_players_puuid(self):
        pass

    @abc.abstractmethod
    def save_match_player_details(self, match_player_details: MatchPlayerDetailsModel):
        pass

    @abc.abstractmethod
    def get_position_by_name(self, position_name: str):
        pass

    @abc.abstractmethod
    def save_position_in_database(self, position: PositionModel):
        pass

    @abc.abstractmethod
    def get_role_by_name(self, role):
        pass

    @abc.abstractmethod
    def save_role_in_database(self, position):
        pass

    @abc.abstractmethod
    def get_objective_type_by_name(self, objective_name: str):
        pass

    @abc.abstractmethod
    def save_objective_type_in_database(self, objective_type: ObjectiveTypeModel):
        pass

    @abc.abstractmethod
    def get_game_mode_type_by_name(self, game_mode: str):
        pass

    @abc.abstractmethod
    def get_game_platform_by_name(self, platform_name: str):
        pass

    @abc.abstractmethod
    def get_game_type_by_name(self, game_type: str):
        pass

    @abc.abstractmethod
    def get_queue_by_name(self, game_type: str):
        pass

    @abc.abstractmethod
    def save_match_info_in_database(self, match_info: MatchInfoModel):
        pass

    @abc.abstractmethod
    def save_match_team_info_in_database(self, match_team_info):
        pass

    @abc.abstractmethod
    def save_objective_in_database(self, objective):
        pass

    @abc.abstractmethod
    def get_match_team_info_by_match_info_id_and_team_id(self, match_info_id: int, team_id: int):
        pass

    @abc.abstractmethod
    def save_ban_in_database(self, ban: BanModel):
        pass

    @abc.abstractmethod
    def get_ban_info_by_champion_id_and_match_info_team_id(self, champion_id: int, match_info_team_id: int):
        pass

    @abc.abstractmethod
    def get_player_by_summoner_name(self, summoner_name: str):
        pass

    @abc.abstractmethod
    def get_objective_by_objective_type_id_and_match_info_team_id(self, objective_type, match_info_team_id):
        pass

    @abc.abstractmethod
    def get_match_participant_by_relations_ids(self, champion_id: int, team_position_id: int, individual_position_id: int, role_id: int, match_info_team_id:int, player_id: int):
        pass

    @abc.abstractmethod
    def get_champion_by_riot_id(self, riot_id: str):
        pass
