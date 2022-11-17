from fastapi import APIRouter, Request
from controllers.game_mode import GameModeController


router = APIRouter()

@router.get('/game/mode')
async def index(request: Request):
    return GameModeController.index(request)
