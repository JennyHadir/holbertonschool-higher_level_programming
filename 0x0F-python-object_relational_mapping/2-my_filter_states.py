#!/usr/bin/python3
""" Lists all states where name begin with specific letter from a database """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
            if row[1] == argv[4]:
                print (row)
    cur.close()
    db.close()
