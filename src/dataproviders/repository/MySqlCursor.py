from typing import List

import mysql.connector


class MySqlCursor:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="db_user_lol_pro_players_stats",
            password="M@rm1t@$101"
        )

    def bulk_insert(self, insert_clause: str, insert_values_list: []):
        values_to_insert = list(value.__dict__ for value in insert_values_list)
        cursor = self.mydb.cursor()
        cursor.executemany(insert_clause, values_to_insert)
        self.mydb.commit()
        cursor.close()

    def get_record(self, select_clause: str, query_params: ()):
        cursor = self.mydb.cursor()
        cursor.execute(select_clause, query_params)
        return cursor.fetchone()
