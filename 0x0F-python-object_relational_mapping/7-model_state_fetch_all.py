#!/usr/bin/python3
""" List all state objects from a database """

if __name__ == "__main__":

    import sqlalchemy
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker
    import model_state
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()
        for state in session.query(State).order_by(State.id):
            print("{}: {}".format(state.id, state.name))
    session.close()
