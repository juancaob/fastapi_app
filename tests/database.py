from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from app.main import app
from app.config import settings
from app.database import Base

import pytest


SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test"


#print(settings.database_name)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# scope="module" allows to create the session just once per module
# this is useful because some of our tests depend on the database not being destroyed
# BUT this is bad prectice, each of our test must run independently form one another
@pytest.fixture
def session():
    print("My session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    # Base.metadata.drop_all(bind=engine)
    # run our code before we run our test
    # Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    # run our code after our test finishes
    # to keep this code her will delete all tables after it's done
    # Base.metadata.drop_all(bind=engine)