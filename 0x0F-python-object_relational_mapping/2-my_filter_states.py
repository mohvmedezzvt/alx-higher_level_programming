#!/usr/bin/python3
"""MySQLdb Module"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database> <state name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name_searched = sys.argv[1:5]
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    query = """SELECT * FROM states
    WHERE BINARY name = '{}' ORDER BY ID ASC""".format(state_name_searched)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
