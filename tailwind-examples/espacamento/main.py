from reactpy import component
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from reactpy_router import browser_router, route

# My Components
from components import Root

from pathlib import Path

@component
def root():
    return browser_router(
        route("/", Root())
    )


app = FastAPI()

configure(app, root)