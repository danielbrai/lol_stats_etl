import mysql


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
