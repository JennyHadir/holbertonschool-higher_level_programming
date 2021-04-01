#!/usr/bin/python3
""" Lists all states from a database """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE %s\
                 ORDER BY id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
