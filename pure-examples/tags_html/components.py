from reactpy import html, component
from reactpy_utils import DocumentTitle

#styles = html.link({"href": "static/style.css", "rel": "stylesheet"})

@component
def Root():
    return html._(
        DocumentTitle("Meu HTML"),
        html.h1(
            {"style": "background: red;"},
            "Cabeçalho"
        ),
        html.a(
            {
                "href": "https://github.com/langchain-ai/deepagents",
                "target": "_blank"
            },
            "Link deep agents"
        ),
        html.p("Imagem abaixo:"),
        html.img(
            {
                "src": "data:image/png;base64,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",
                "alt": "Imagem logo langchain"
            }
        ),
        html.pre(
            html.code(
            """
import pandas as pd

df = pd.read_csv("nome-do-arquivo.csv")
            """
        )
    )
)