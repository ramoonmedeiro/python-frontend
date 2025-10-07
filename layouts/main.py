from reactpy import html, component
from reactpy_router import route, browser_router
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components import Home

app = FastAPI()

@component
def Router():
    return browser_router(
        route("/", Home())
    )

configure(app=app, component=Router)