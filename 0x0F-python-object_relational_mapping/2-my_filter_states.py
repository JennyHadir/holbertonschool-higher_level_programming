#!/usr/bin/python3
""" Lists all states where name begin with specific letter from a database """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE '{}' COLLATE latin1_general_cs\
                 ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
            print(row)
    cur.close()
    db.close()
