from reactpy import html, component
from reactpy_utils import DocumentTitle

styles = html.link({"href": "static/style.css", "rel": "stylesheet"})

@component
def Root():
    return html._(
        styles,
        DocumentTitle("Forms e inputs"),
        html.form(
            {
                "action": "#",
                "method": "GET",
                "target": "_blank",
                "autocomplete": "off"
            },
            html.p("Meu formulário"),
            html.input(
                {   
                    "id": "nome",
                    "type": "text",
                    "name": "nome",
                    "placeholder": "Seu nome"
                }
            ),
            html.button(
                {"type": "reset"},
                "Reset"
            ),
            html.button(
                {"type": "submit"},
                "Enviar"
            )
        )
)