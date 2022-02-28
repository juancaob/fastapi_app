from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


# These imports are necessary if you want to connect directly to mysql
# import time
# import mysql.connector

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:passwor@host/database_name"
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"


#print(settings.database_name)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This code is necessary if you want to connect directly to mysql
# while True:
#     try:
#         conn = mysql.connector.connect(
#             host=f"{settings.database_hostname}", user=f"{settings.database_username}", 
#             password=f"{settings.database_password}", database=f"{settings.database_name}"
#         )
#         cursor = conn.cursor()
#         print("Connection was succsesful!")
#         break
#     except Exception as error:
#         print("Connection to database failed!")
#         print("Error: ", error)
#         time.sleep(2)
