#!/usr/bin/python3
""" Update a name of a state where id=2 """
import sqlalchemy
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter_by(id=2).first()
        state.name = "New Mexico"
        session.commit()
        session.close()
