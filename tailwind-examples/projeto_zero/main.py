from reactpy import component
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from reactpy_router import browser_router, route

# My Components
from components.root import Root, Apresentacao, Contador

@component
def root():
    return browser_router(
        route("/", Root()),
        route("/sobre", Apresentacao(nome="Ramonstro")),
        route("/botoes", Contador())
    )

app = FastAPI()
configure(app, root)
