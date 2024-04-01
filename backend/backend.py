## 
# @brief Runs a Flask backend that queries a MySQL database.
#
# @section Description
# This program performs SQL queries on a MySQL 
# Docker container. The Flask app receives data
# via GET HTTP requests.
#
# @section Author
# - John Nori, Jalen Guan, Muho Ahmed, Jake Grinsh (c) 2024

from flask import Flask, request, jsonify
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
                SELECT r.characters, t.title FROM roles r
                JOIN names n ON r.name_id = n.name_id
                JOIN titles t ON r.title_id = t.title_id
                WHERE n.name = "%s"
                """ % (name)
        with self.connection.cursor(buffered=True) as cursor:
            cursor.execute(query)
            self.connection.commit()
            result = cursor.fetchall()

            # transform the result for return
            if result:
                characters = [(row[1], row[0].replace('"','').lstrip('[').rstrip(']').split(','))
                              if row[0] else (row[1], "N/A") for row in result]
            else:
                characters = None

        # return the list
        return characters

server = Flask(__name__)
conn = None

@server.route('/search', methods=['GET'])
def handle_get():
    global conn
    if not conn:
        mysql_manager = mysqlManager(password_file='/run/secrets/db-password')
    if request.method == 'GET':
        name = request.args['actor']
        print(name)
        rec = mysql_manager.make_actor_query(name=name)
        if rec:
            return jsonify(dict((key, value) for key, value in rec))
        else:
            return jsonify({})
    else:
        return "Invalid Name"

if __name__ == '__main__':
    server.run()
