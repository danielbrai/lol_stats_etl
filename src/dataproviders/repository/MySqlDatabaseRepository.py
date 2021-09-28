from typing import List
import mysql.connector

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.models.Champion import Champion
from src.core.models.Item import Item
from src.core.models.Map import Map
from src.core.models.Queue import Queue
from src.core.models.Team import Team


class MySqlDatabaseRepository(DatabaseRepositoryConstraint):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="db_user_lol_pro_players_stats",
            password="M@rm1t@$101"
        )

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
        values_to_insert = list(champion.__dict__ for champion in champions_data)
        insert_clause = 'INSERT INTO lol_pro_players_stats.champions(id, name) VALUES (%(id)s, %(name)s)'
        cursor = self.mydb.cursor()
        cursor.executemany(insert_clause, values_to_insert)
        self.mydb.commit()

    def save_items_in_database(self, champions_data: List[Item]):
        values_to_insert = list(champion.__dict__ for champion in champions_data)
        insert_clause = 'INSERT INTO lol_pro_players_stats.items (id, name) VALUES (%(id)s, %(name)s)'
        cursor = self.mydb.cursor()
        cursor.executemany(insert_clause, values_to_insert)
        self.mydb.commit()

    def save_maps_in_database(self, map_info_data: List[Map]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.maps (riot_map_id, name, notes) VALUES (%(riot_map_id)s, %(name)s, %(notes)s)'
        values_to_insert = list(map_info.__dict__ for map_info in map_info_data)
        cursor = self.mydb.cursor()
        cursor.executemany(insert_clause, values_to_insert)
        self.mydb.commit()

    def save_queue_in_database(self, queue_data: List[Queue]):
        values_to_insert = list(queue.__dict__ for queue in queue_data)
        insert_clause = 'INSERT INTO lol_pro_players_stats.queues (id, map_id, description, notes) VALUES (%(id)s, %(map_id)s, %(description)s, %(notes)s)'
        cursor = self.mydb.cursor()
        cursor.executemany(insert_clause, values_to_insert)
        self.mydb.commit()

    def get_map_by_name(self, map_name):
        select_clause = 'SELECT maps.id, maps.name, maps.notes, maps.riot_map_id FROM lol_pro_players_stats.maps WHERE maps.name = %s ORDER BY maps.id DESC LIMIT 1'
        cursor = self.mydb.cursor()
        cursor.execute(select_clause, (map_name, ))
        result = cursor.fetchone()
        return Map(id=result[0], name=result[1], notes=result[2], riot_map_id=result[3]) if result else None
