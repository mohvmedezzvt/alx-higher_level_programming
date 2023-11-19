#!/usr/bin/python3
"""MySQLdb Module"""

import MySQLdb
import sys

if __name__ == '__main__':
    username, password, database, state = sys.argv[1:5]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    query = """SELECT name FROM cities
    WHERE cities.state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY cities.id ASC"""
    cursor.execute(query, (state,))

    rows = cursor.fetchall()
    flag = -1
    for row in rows:
        if flag == -1:
            print(row, end="")
            flag = 1
        else:
            print(", " + row, end="")

    print("")

    cursor.close()
    connection.close()
