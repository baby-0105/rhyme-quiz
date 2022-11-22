from fastapi import APIRouter, Request
from controllers.public import PublicController


router = APIRouter()

@router.get('/')
async def index(request: Request):
    return PublicController.top(request)
