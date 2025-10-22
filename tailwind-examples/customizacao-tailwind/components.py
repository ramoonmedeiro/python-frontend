from reactpy import html, component
from reactpy_utils import DocumentTitle

styles = html.link({"href": "static/style.css", "rel": "stylesheet"})
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Root():
    return html._(
        cdn,
        styles,
        DocumentTitle("Site básico"),
        html.p(
            {"class": "text-[#ff6347] text-base tablet:text-xl"}, 
            "Tá no ar porra"
        ),
        html.p(
            {"class": "text-cyan-900"},
            "Outro texto"
        ),
        html.p(
            {"class": "text-yellow-900 p-[20rem]"},
            "Outro texto customizado"
        )
)