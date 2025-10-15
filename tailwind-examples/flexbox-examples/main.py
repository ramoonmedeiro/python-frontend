from reactpy import component
from reactpy_router import browser_router, route
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from components import Home


@component
def Router():
    return browser_router(
        route("/", Home())
    )

app = FastAPI()
configure(app=app, component=Router)