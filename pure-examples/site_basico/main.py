from reactpy import component
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from reactpy_router import browser_router, route

# My Components
from components import Root

from fastapi.staticfiles import StaticFiles
from pathlib import Path

STATIC_DIR = Path(__file__).parent / "static"

@component
def root():
    return browser_router(
        route("/", Root())
    )


app = FastAPI()
app.mount(
    "/static", 
    StaticFiles(directory=STATIC_DIR), 
    name="static"
)
configure(app, root)