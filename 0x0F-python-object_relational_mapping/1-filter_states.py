#!/usr/bin/python3
"""MySQLdb Module"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY ID ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
