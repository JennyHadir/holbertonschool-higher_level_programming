#!/usr/bin/python3
""" Lists all cities of a given state from a database """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 INNER JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id", (argv[4], ))
    cities = cur.fetchall()
    comma = 0
    for city in cities:
        if comma != 0:
            print(",", end="")
        print("%s" % city, end="")
        comma += 1
    print("")
    cur.close()
    db.close()
