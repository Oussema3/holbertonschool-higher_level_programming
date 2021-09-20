#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa where name matches the argument. 
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    pas = sys.argv[2]
    dbn = sys.argv[3]
    statex = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=pas, db=dbn)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{:s}' ORDER BY states.id"
                .format(statex))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == statex:
            print(row)
    cur.close()
    db.close()
