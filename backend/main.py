from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as user_router
from routers.game import router as game_router
from routers.public import router as public_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(game_router)
app.include_router(public_router)
