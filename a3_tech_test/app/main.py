from fastapi import FastAPI
from a3_tech_test.app.routers.index import router
from a3_tech_test.__init__ import __version__

app = FastAPI(
    version=__version__
)

app.include_router(
    router=router,
    prefix=""
)