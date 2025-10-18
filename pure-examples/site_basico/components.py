from reactpy import html, component
from reactpy_utils import DocumentTitle

styles = html.link({"href": "static/style.css", "rel": "stylesheet"})

@component
def Header():
    return html.header(
        html.h1(
            html.a(
                {"href": "#"},
                "Home"
            )
        ),
        html.p("Seu site sendo visitado")
    )

@component
def NavBar():
    return html.aside(
        html.nav(
            html.ul(
                html.li(html.a({"href": "#"}, "Página inicial")),
                html.li(html.a({"href": "#"}, "API Token")),
                html.li(html.a({"href": "#"}, "Config")),
                html.li(html.a({"href": "#"}, "Logout"))
            )
        )
    )

@component
def Root():
    return html._(
        styles,
        DocumentTitle("Site básico"),
        Header(),
        NavBar()
)