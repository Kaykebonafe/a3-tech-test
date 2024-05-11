from fastapi import FastAPI
from a3_tech_test.app.routers import index, chat
from a3_tech_test.__init__ import __version__

app = FastAPI(
    version=__version__
)

app.include_router(
    router=index.router,
    prefix=""
)

app.include_router(
    router=chat.router,
    prefix="/chat"
)