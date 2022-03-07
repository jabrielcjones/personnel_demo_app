
# import mysql.connector
import sqlalchemy as db

from fastapi import FastAPI

app = FastAPI()

user = "admin"
password = "admin_pass"
host = "personnel_db"
database = "personnel_db"

def get_db_engine():

    try:
        engine = db.create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}", echo=True)
    
    except Exception as err:
        print(f"Unable to get DB engine: {err}")
        engine = None
    
    return engine

def get_personnel_table():

    try:

        engine = get_db_engine()
        connection = engine.connect()
        metadata = db.MetaData()

        personnel = db.Table("PERSONNEL", metadata, autoload=True, autoload_with=engine)

    except Exception as err:
        print(f"ERROR: {err}")
        personnel = None

    return personnel

@app.get("/")
def read_root():
    return { "Personnel Demo app": "Welcome to Personnel Demo app" }

@app.get("/db")
def read_db():

    # try:
    #     mydb = mysql.connector.connect(
    #     host="personnel_db",
    #     user="admin",
    #     password="admin_pass",
    #     database="personnel_db"
    #     )

    # except Exception as err:
    #     print(f"Unable to connect: {err}")
    #     mydb = None

    # mycursor = mydb.cursor()

    # mycursor.execute("SELECT * FROM PERSONNEL LIMIT 10")

    # myresult = mycursor.fetchall()

    personnel = get_personnel_table()

    try:
        colunns = personnel.columns.keys()

    except Exception as err:
        print(f"Unable to get PERSONNEL columns: {err}")

    return { "Personnel Demo db": colunns }
