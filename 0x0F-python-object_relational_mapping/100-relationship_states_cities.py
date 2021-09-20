#!/usr/bin/python3
"""
creates the  with the San 
"""
import sys
from relationship_state import Base, State, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = State(name="California")
    s.cities = [City(name="San Francisco")]
    session.add(s)
    session.commit()
    session.close()
