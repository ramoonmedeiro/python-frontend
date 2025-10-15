from reactpy import html, component
from reactpy_utils import DocumentTitle

styles = html.link({"href": "static/style.css", "rel": "stylesheet"})

@component
def Root():
    return html._(
        DocumentTitle("Meu HTML"),
        styles,
        html.h1(
            {"id": "head-1"},
            "Meu HTML"
        ),
        html.p("Olá galera"),
        html.br(),
        html.p(
            html.b(
                "Outro texto"
            )),
        html.h1(
            {"id": "head-2"},
            "Meu HTML 2"
        )
    )