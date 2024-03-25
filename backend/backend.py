import os
from flask import Flask
import mysql.connector
import json

class mysqlManager:
    """The MySQL Database Manager class."""

    def __init__(self, host="mysql_db", user="root", password_file=None, database="imdb_database"):
        """ Constructor.

        Args:
            host: name of container running the database
            user: username of MySQL account with access permissions
            password: password of MySQL account with access permissions
            database: name of the database to be searched
        Returns:
            An initialized database manager.
        """
        if password_file is not None:
            with open(password_file, 'r') as fp:
                self.connection = mysql.connector.connect(
                    host=host,
                    user=user, 
                    password=fp.read().rstrip('\n'),
                    database=database,
                )
    
    def make_actor_query(self, name="Tom Hardy"):
        query = """
                SELECT r.characters, t.title
                FROM roles r
                JOIN names n ON r.name_id = n.name_id
                JOIN titles t ON r.title_id = t.title_id
                WHERE n.name = "Tom Hardy"
                """
        with self.connection.cursor(buffered=True) as cursor:
            cursor.execute(query)
            self.connection.commit()
            result = cursor.fetchall()

            # transform the result for return
            characters = [(row[0].replace('"','').lstrip('[').rstrip(']'), row[1])
                          for row in result]

            if characters:
                print("Characters played by Tom Hardy:")
                for character, title in characters:
                    print(f"Character: {character}, Title: {title}")
            else:
                print("No characters found for Tom Hardy.")

        # return the list
        return characters

server = Flask(__name__)
conn = None

@server.route('/')
def index():
    global conn
    if not conn:
        mysql_manager = mysqlManager(password_file='/run/secrets/db-password')
    rec = mysql_manager.make_actor_query()

    return json.dumps(rec)

if __name__ == '__main__':
    server.run()
