
'''

GET /personnel - returns all personnel records

GET /personnel/id - returns a personnel record

PUT /personnel/id - updates a personnel record

DELETE /personnel/id - removes a personnel record

POST /personnel - adds a personnel record

'''

import sqlalchemy as db

from fastapi import FastAPI

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

Base = declarative_base()

user = "admin"
password = "admin_pass"
host = "personnel_db"
database = "personnel_db"

class Personnel(Base):
    __tablename__ = "PERSONNEL"

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    city = Column(String)
    country = Column(String)
    company = Column(String)

    def __repr__(self) -> str:
        return f"<Personnel({self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.city}, {self.country}, {self.company})"

def get_db_engine():

    try:
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}", echo=True)
    
    except Exception as err:
        print(f"Unable to get DB engine: {err}")
        engine = None
    
    return engine

def get_db_session(engine):

    try:
        Session = sessionmaker(bind=engine)

    except Exception as err:
        print(f"Unable to create DB session: {err}")
        return None

    return Session()

@app.get("/")
def read_root():
    return { "Personnel Demo app": "Welcome to Personnel Demo app" }

@app.get("/personnel/")
def get_personnel_records():

    engine = get_db_engine()
    session = get_db_session(engine)

    personnel_records = []

    try:
        for instance in session.query(Personnel).order_by(Personnel.last_name):
            personnel_records.append(instance)

    except Exception as err:
        print("ERROR: {err}")

    return { "Personnel": personnel_records }
