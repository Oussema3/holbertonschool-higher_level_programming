#!/usr/bin/python3
"""
Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
"""
import sys
import MySQLdb


def main(argv):
    """connects to a given mysql database and lists all 'states' from it"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv)
