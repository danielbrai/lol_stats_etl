from typing import List
import mysql.connector

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.models.Champion import Champion
from src.core.models.Item import Item
from src.core.models.Map import Map
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
        values_to_insert = ','.join(list(f'({champion.id}, "{champion.name}")' for champion in champions_data)).replace("'", "''")
        insert_clause = f"INSERT INTO lol_pro_players_stats.champions(id, name) VALUES {values_to_insert}"
        cursor = self.mydb.cursor()
        cursor.execute(insert_clause)
        self.mydb.commit()

    def save_items_in_database(self, champions_data: List[Champion]):
        values_to_insert = ','.join(list(f'({champion.id}, "{champion.name}")' for champion in champions_data)).replace("'", "''")
        insert_clause = f'INSERT INTO lol_pro_players_stats.items (id, name) VALUES {values_to_insert}'
        cursor = self.mydb.cursor()
        cursor.execute(insert_clause)
        self.mydb.commit()

    def save_maps_in_database(self, map_info_data: List[Map]):
        values_to_insert = ','.join(list(f'({map_info.riot_id}, "{map_info.name}", "{map_info.notes}")' for map_info in map_info_data)).replace("'", "''")
        insert_clause = f'INSERT INTO lol_pro_players_stats.maps (riot_map_id, name, notes) VALUES {values_to_insert}'
        cursor = self.mydb.cursor()
        cursor.execute(insert_clause)
        self.mydb.commit()
