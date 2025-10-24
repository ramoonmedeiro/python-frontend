# Reactpy core
from reactpy import component
from reactpy_router import browser_router, route

# fastapi config
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Components
from components import Index


STATIC_DIR = Path(__file__).parent / "static"

@component
def Route():
    return browser_router(
        route("/", Index())
    )

app = FastAPI()
app.mount(
    "/static", 
    StaticFiles(directory=STATIC_DIR), 
    name="static"
)
configure(app=app, component=Route)