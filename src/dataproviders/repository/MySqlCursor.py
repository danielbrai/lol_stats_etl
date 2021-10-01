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
        saved_id = cursor.lastrowid
        cursor.close()

    def single_insert(self, insert_clause: str, insert_value):
        values_to_insert = insert_value.__dict__
        cursor = self.mydb.cursor()
        cursor.execute(insert_clause, values_to_insert)
        self.mydb.commit()
        saved_id = cursor.lastrowid
        cursor.close()
        return saved_id

    def get_record(self, select_clause: str, query_params: ()):
        cursor = self.mydb.cursor()
        cursor.execute(select_clause, query_params)
        result = cursor.fetchone()
        cursor.close()
        return result
