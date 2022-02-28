#from functools import lru_cache
from fastapi import FastAPI
# We import this function to allow other domains conumicate with our api
from fastapi.middleware.cors import CORSMiddleware

from app.routers.vote import vote
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

#print(settings.database_password)

# This command is needed if we did not have alembic
# models.Base.metadata.create_all(bind=engine)
# Since we have alembic we do not need it anymore

app = FastAPI()

# We add this code to allow other domains conumicate with our api

# origins = ["https://www.google.com"]

# To allows all domains to acces our api

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @lru_cache
# def get_settings():
#     return Settings


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") 
def root():
    return {"message": "Hello, Juan"}



