from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.champions.ChampionModel import ChampionModel
from src.core.usecase.game_modes.GameModeModel import GameModeModel
from src.core.usecase.game_types.GameTypeModel import GameTypeModel
from src.core.usecase.items.ItemModel import ItemModel
from src.core.usecase.line_up.lineup.PlayerTeamModel import PlayerTeamModel
from src.core.usecase.line_up.player.PlayerModel import PlayerModel
from src.core.usecase.line_up.teams.TeamModel import TeamModel
from src.core.usecase.maps.MapModel import MapModel
from src.core.usecase.platforms.PlatformModel import PlatformModel
from src.core.usecase.queues.QueueModel import QueueModel
from src.dataproviders.repository.MySqlCursor import MySqlCursor


class MySqlDatabaseRepository(DatabaseRepositoryConstraint):
    def get_team_id(self, team_name: str):
        pass

    def __init__(self, cursor: MySqlCursor):
        self.cursor = cursor

    def get_map_by_name(self, map_name: str):
        select_clause = 'SELECT maps.id, maps.name, maps.notes, maps.riot_map_id FROM lol_pro_players_stats.maps WHERE maps.name = %s ORDER BY maps.id DESC LIMIT 1'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(map_name,))
        return MapModel(id=result[0], name=result[1], notes=result[2], riot_map_id=result[3]) if result else None

    def save_champions_in_database(self, champions_data: List[ChampionModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.champions(id, name) VALUES (%(id)s, %(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=champions_data)

    def save_items_in_database(self, items_data: List[ItemModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.items (id, name) VALUES (%(id)s, %(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=items_data)

    def save_maps_in_database(self, map_info_data: List[MapModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.maps (riot_map_id, name, notes) VALUES (%(riot_map_id)s, %(name)s, %(notes)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=map_info_data)

    def save_queue_in_database(self, queue_data: List[QueueModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.queues (id, map_id, description, notes) VALUES (%(id)s, %(map_id)s, %(description)s, %(notes)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=queue_data)

    def save_game_modes_in_database(self, game_modes_data: List[GameModeModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.game_modes (mode, description) VALUES (%(mode)s, %(description)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=game_modes_data)

    def save_game_types_in_database(self, game_types_data: List[GameTypeModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.game_types (type, description) VALUES (%(type)s, %(description)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=game_types_data)

    def save_platform_in_database(self, platform_data: List[PlatformModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.platforms (name) VALUES (%(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=platform_data)

    def save_team_info_in_database(self, team: TeamModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.teams (name) VALUES (%(name)s)'
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=team)

    def get_team_by_name(self, team_name: str):
        select_clause = 'SELECT teams.id, teams.name FROM lol_pro_players_stats.teams WHERE teams.name = %s ORDER BY teams.id DESC LIMIT 1'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(team_name,))
        return TeamModel(id=result[0], name=result[1]) if result else None

    def save_player(self, player: PlayerModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.players (summoner_name, puuid) VALUES (%(summoner_name)s, %(puuid)s)'
        a = self.cursor.single_insert(insert_clause=insert_clause, insert_value=player)
        return a

    def save_team_player_info_in_database(self, player_team: PlayerTeamModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.lineup (player_id, team_id, season, split) VALUES (%(player_id)s, %(team_id)s, %(season)s, %(split)s)'
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=player_team)