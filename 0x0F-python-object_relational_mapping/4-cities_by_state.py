#!/usr/bin/python3
"""MySQLdb Module"""

import MySQLdb
import sys

if __name__ == '__main__':
    username, password, database = sys.argv[1:4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC"""
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
