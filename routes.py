from fastapi import APIRouter, Request, Body
from models.playerModels import Player
from bson import ObjectId
router = APIRouter(prefix="/api", tags=['players'])

@router.get("/")
async def getPlayers(request: Request)->list[Player]:
    db = request.app.players
    response = list(db.find({}))
    for item in response:
        item["_id"] = str(item["_id"])
    return response


@router.post("/")
async def addPlayer(request: Request, player: Player = Body(...)):
    db = request.app.players
    response = db.insert_one(player.model_dump())
    return {"id": str(response.inserted_id)}
