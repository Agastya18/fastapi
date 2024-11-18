from fastapi import FastAPI
from contextlib import asynccontextmanager
from pymongo import MongoClient
from dotenv import dotenv_values
from routes import router

config = dotenv_values(".env")

async def connectToDatabase():
    db = MongoClient(config["DATABASE_URL"])
    # print(db)
    return db

@asynccontextmanager
async def lifespan(app: FastAPI):
    dbHost = await connectToDatabase()
    app.players = dbHost.tournament.players
    print("startup has begun!!")
    yield
    print("shutdown has begun!!")

app = FastAPI(lifespan=lifespan)
app.include_router(router)
# @app.get("/")
# def read_root(): # function that is binded with the endpoint
#     return {"Hello": "World"}
    
