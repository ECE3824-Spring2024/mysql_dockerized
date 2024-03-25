## 
# @brief Make various queries on a MySQL database.
#
# @section Description
# This program performs SQL queries on a remote 
# MySQL database hosted in the AWS Cloud (EC2).
# 
# @section Dependencies
# - pip install mysql-connector-python
#
# @section Usage
# $ python queries.py [CODE]
#
# @section Author
# - John Nori, Jalen Guan, Muho Ahmed (c) 2024

import configparser
import mysql.connector
from mysql.connector import connect, Error
from flask import Flask
import sys

def find_tom_hardy_movies(connection:mysql.connector, print_flag:bool=False) -> list:
    """ Finds all movies starring Tom Hardy.

    Args:
        connection (mysql.connector): connection to remote MySQL server
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database. 
    """
    query = """
            SELECT title FROM titles WHERE title_id IN 
            (SELECT title_id FROM roles WHERE name_id IN 
            (SELECT name_id FROM names WHERE name="Tom Hardy"))
            """

    with connection.cursor(buffered=True) as cursor:
        
        # execute the query
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()

        # just get the name
        result = [res[0] for res in result]

        # print results
        if print_flag:
            print("Tom Hardy has starred in the following movies:")
            for row in result:
                print(f" - {row}")

        # return the list
        return result

def find_tom_hardy_characters(connection:mysql.connector, print_flag:bool=False) -> list:
    """ Finds all characters played by Tom Hardy.

    Args:
        connection (mysql.connector): connection to remote MySQL server
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database. 
    """
    query = """
            SELECT r.characters, t.title
            FROM roles r
            JOIN names n ON r.name_id = n.name_id
            JOIN titles t ON r.title_id = t.title_id
            WHERE n.name = "Tom Hardy"
            """

    with connection.cursor(buffered=True) as cursor:
        
        # execute the query
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()

        # transform the result for return
        characters = [(row[0], row[1]) for row in result]

        if print_flag and characters:
            print("Characters played by Tom Hardy:")
            for character, title in characters:
                print(f"Character: {character}, Title: {title}")
        elif print_flag:
            print("No characters found for Tom Hardy.")

        # return the list
        return characters
    
def find_tom_hardy_worked_with(connection:mysql.connector, print_flag:bool=False) -> list:
    """ Finds all people who have worked with Tom Hardy.

    Args:
        connection (mysql.connector): connection to remote MySQL server
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database. 
    """
    query = """
            SELECT DISTINCT n.name
            FROM names n
            JOIN roles r ON n.name_id = r.name_id
            WHERE r.title_id IN (
                SELECT r.title_id
                FROM roles r
                JOIN names n ON r.name_id = n.name_id
                WHERE n.name = 'Tom Hardy'
            ) AND n.name != 'Tom Hardy'
            """

    with connection.cursor(buffered=True) as cursor:
        
        # execute the query
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()

        # just get the name
        result = [res[0] for res in result]

        # print results
        if print_flag:
            print("Tom Hardy has worked with the following people:")
            for row in result:
                print(f" - {row}")

        # return the list
        return result
    
def find_people_born_1975_1976(connection:mysql.connector, print_flag:bool=False) -> list:
    """ Finds all people born between 1975 and 1976, inclusive.

    Args:
        connection (mysql.connector): connection to remote MySQL server
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database. 
    """
    query = """
            SELECT name, yearBorn
            FROM names
            WHERE yearBorn BETWEEN 1975 AND 1976
            """

    with connection.cursor(buffered=True) as cursor:
        
        # execute the query
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()

        # just get the name
        result = [f"{res[0]} ({res[1]})" for res in result]

        # print results
        if print_flag:
            print("The following people were born between 1975 and 1976, inclusive:")
            for row in result:
                print(f" - {row}")

        # return the list
        return result
    
def find_people_born_1975_worked_with_will_ferrell(connection:mysql.connector, print_flag:bool=False) -> list:
    """ Finds all people born in 1975 who have also worked with Will Ferrell.

    Args:
        connection (mysql.connector): connection to remote MySQL server
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database. 
    """
    query = """
            SELECT DISTINCT n.name
            FROM names n
            INNER JOIN roles r ON n.name_id = r.name_id
            INNER JOIN titles t ON r.title_id = t.title_id
            WHERE n.yearBorn = 1975  
            AND t.title_id IN (
                SELECT t.title_id
                FROM titles t
                INNER JOIN roles r ON t.title_id = r.title_id
                INNER JOIN names n ON r.name_id = n.name_id
                WHERE n.name = "Will Ferrell" AND n.yearBorn = 1967
            )
            """

    with connection.cursor(buffered=True) as cursor:
        
        # execute the query
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()

        # just get the name
        result = [res[0] for res in result]

        # print results
        if print_flag:
            print("The following people were born in 1975 and also worked with Will Ferrell (1967):")
            for row in result:
                print(f" - {row}")

        # return the list
        return result
    
    
def find_unique_fantasy_characters(connection:mysql.connector, print_flag:bool=False) -> list:
    """ Finds unique directors for "Fantasy" movies.

    Args:
        connection (mysql.connector): connection to remote MySQL server
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database. 
    """
    # query = """
    #         SELECT DISTINCT name FROM names WHERE name_id IN
    #         (SELECT name_id FROM roles WHERE category = 'director' AND
    #         title_id IN (SELECT title_id FROM titles WHERE genre LIKE '%Fantasy%'))
    #         """

    query = """
            SELECT DISTINCT n.name_id, n.name AS num_unique_directors
            FROM titles t
            JOIN roles r ON t.title_id = r.title_id
            JOIN names n ON r.name_id = n.name_id
            WHERE t.genre LIKE "%Fantasy%"
            AND r.category = 'director'
            """

    with connection.cursor(buffered=True) as cursor:
        
        # execute the query
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()

        # just get the name
        result = [res[1] for res in result]

        # print results
        if print_flag:
            print("The following are directors of \"Fantasy\" movies:")
            for row in result:
                print(f" - {row}")

        # return the list
        return result

def find_tom_hardy_with_james_gandolfini(connection:mysql.connector, print_flag:bool=False) -> list:
    """ Finds movie(s) that Tom Hardy and James Gandolfini worked together on.

    Args:
        connection (mysql.connector): connection to remote MySQL server
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database. 
    """
    query = """
            SELECT DISTINCT t.title, t.year
            FROM titles t
            INNER JOIN roles r1 ON t.title_id = r1.title_id
            INNER JOIN names n1 ON r1.name_id = n1.name_id AND n1.name = 'Tom Hardy'
            INNER JOIN roles r2 ON t.title_id = r2.title_id
            INNER JOIN names n2 ON r2.name_id = n2.name_id AND n2.name = 'James Gandolfini'
            """

    with connection.cursor(buffered=True) as cursor:
        
        # execute the query
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()

        # just get the name
        result = [f"{res[0]}({res[1]})" for res in result]

        # print results
        if print_flag:
            print("Tom Hardy and James Gandolfini have worked together on the following movies:")
            for row in result:
                print(f" - {row}")

        # return the list
        return result 

def make_query(host:str, user:str, password:str, database:str, code:int=0, print_flag:bool=False) -> list | None:
    """ Perform various MySQL queries.

    Args:
        host: ip address of the EC2 instance
        user: username of MySQL account with remote access permissions
        password: password of MySQL account with remote access permissions
        database: name of the database to be searched
        code: query number to-be-run (if 0, all queries are executed)
        print_flag: if True, print results to the terminal
    Returns:
        A list of results obtained from the database (`None` is all queries executed at once).
    """

    # check input arguments
    if isinstance(code, int):
        if not (code >= 0) and (code < 8):
            raise ValueError(f"`code` argument must be between 0 and 7.\nCurrent value: {code}")
    else:
        raise TypeError(f"`code` argument must be an integer.\nCurrent type: {code} ({type(code)})")

    try:

        # make connection
        with connect(host=host, user=user, password=password, database=database) as connection:

            # inform the user that a connection has been made
            if print_flag:
                print(f"Connection to {database} at {host} established!")

            # make a query based on the input code
            if code == 1:
                return find_tom_hardy_movies(connection, print_flag=print_flag)
            elif code == 2:
                return find_tom_hardy_characters(connection, print_flag=print_flag)
            elif code == 3:
                return find_tom_hardy_worked_with(connection, print_flag=print_flag)
            elif code == 4:
                return find_people_born_1975_1976(connection, print_flag=print_flag)
            elif code == 5:
                return find_people_born_1975_worked_with_will_ferrell(connection, print_flag=print_flag)
            elif code == 6:
                return find_unique_fantasy_characters(connection, print_flag=print_flag)
            elif code == 7:
                return find_tom_hardy_with_james_gandolfini(connection, print_flag=print_flag)
            else:
                find_tom_hardy_movies(connection, print_flag=print_flag)
                find_tom_hardy_characters(connection, print_flag=print_flag)
                find_tom_hardy_worked_with(connection, print_flag=print_flag)
                find_people_born_1975_1976(connection, print_flag=print_flag)
                find_people_born_1975_worked_with_will_ferrell(connection, print_flag=print_flag)
                find_unique_fantasy_characters(connection, print_flag=print_flag)
                find_tom_hardy_with_james_gandolfini(connection, print_flag=print_flag)
            
    except Error as e:  
        print(e)

def main(argv):
    """The Main Program."""

    # ensure the user entered a digit
    code = 0
    if len(argv) > 1:
        if argv[1].isdigit():
            code = int(argv[1])
            if not ((code > 0) and (code < 8)):
                raise ValueError("Command line argument must be between 1 and 7.\nUsage: $ python queries.py [CODE]")
        else:
            raise TypeError("Command line argument must be a single digit.\nUsage: $ python queries.py [CODE]")

    # parse the config file to get the network parameters
    config   = configparser.ConfigParser()
    config.read("remote.cfg")
    host     = "mydb"
    user     = "myuser"
    password = "mypassword"
    database = "imdb_database"

    # connect to the database and make queries
    make_query(host, user, password, database, code, True)
     
if __name__ == "__main__":
    main(sys.argv)
