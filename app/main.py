from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers.team_router import team_router
from routers.user_router import user_router
from core.config import Config

# from loguru import logger as log
# import os

# path = os.path.dirname(__file__)
# logger_log = os.path.join(path, "logger_scraper.log")
# log.add(logger_log, format="{time} {level} {message}", level="DEBUG")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(team_router)

if __name__ == "__main__":
    uvicorn.run(
        Config.path,
        host=Config.host,
        port=Config.port,
        reload=Config.reload
    )
