#!/usr/bin/python3
""" Lists all states from a database """
import MySQLdb
from sys import argv
db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
      print(row)
cur.close()
db.close()
