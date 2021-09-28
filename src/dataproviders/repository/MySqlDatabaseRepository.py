from typing import List
import mysql.connector

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.models.Champion import Champion
from src.core.models.GameMode import GameMode
from src.core.models.Item import Item
from src.core.models.Map import Map
from src.core.models.Queue import Queue
from src.core.models.Team import Team
from src.dataproviders.repository.MySqlCursor import MySqlCursor


class MySqlDatabaseRepository(DatabaseRepositoryConstraint):
    def __init__(self, cursor: MySqlCursor):
        self.cursor = cursor

    def get_map_by_name(self, map_name: str):
        select_clause = 'SELECT maps.id, maps.name, maps.notes, maps.riot_map_id FROM lol_pro_players_stats.maps WHERE maps.name = %s ORDER BY maps.id DESC LIMIT 1'
        cursor = self.mydb.cursor()
        cursor.execute(select_clause, (map_name, ))
        result = cursor.fetchone()
        return Map(id=result[0], name=result[1], notes=result[2], riot_map_id=result[3]) if result else None

    def save_player(self, player: str, team_id: int, season: int, split: int):
        # print(f'INSERT INTO players (summonerid) VALUES ({player})')
        print(f'INSERT INTO lineup (playerid, teamid, season, split) VALUES {1, team_id, season, split}')

    def save_teams(self, teams: List[Team]):
        print(teams)
        return

    def get_team_id(self, team_name: str):
        print(team_name)
        return 1

    def save_champions_in_database(self, champions_data: List[Champion]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.champions(id, name) VALUES (%(id)s, %(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=champions_data)

    def save_items_in_database(self, items_data: List[Item]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.items (id, name) VALUES (%(id)s, %(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=items_data)

    def save_maps_in_database(self, map_info_data: List[Map]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.maps (riot_map_id, name, notes) VALUES (%(riot_map_id)s, %(name)s, %(notes)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=map_info_data)

    def save_queue_in_database(self, queue_data: List[Queue]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.queues (id, map_id, description, notes) VALUES (%(id)s, %(map_id)s, %(description)s, %(notes)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=queue_data)

    def save_game_modes_in_database(self, game_modes_data: List[GameMode]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.game_modes (mode, description) VALUES (%(mode)s, %(description)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=game_modes_data)
