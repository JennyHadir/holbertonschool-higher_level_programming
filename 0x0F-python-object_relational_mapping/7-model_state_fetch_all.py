#!/usr/bin/python3
""" List all state objects from a database """
import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()
        for state in session.query(State).order_by(State.id):
            print("{}: {}".format(state.id, state.name))
    session.close()
