#!/usr/bin/python3
""" Lists all cities from a database """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                 INNER JOIN states ON citis.states_id = states.id\
                 ORDER BY cities.id")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
