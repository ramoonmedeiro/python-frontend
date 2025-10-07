from reactpy import html, component, use_state

cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})


@component
def Root():
    return html.h1(
        cdn,
        "Olá mundo"
    )

@component
def Apresentacao(nome):
    return html.h1(
        cdn,
        f"Olá, {nome}"
    )

@component
def Aumentar(index, set_index):
    def handle_event(event):
        set_index(index + 1)
    return html.button({"on_click":handle_event}, "+")

@component
def Diminuir(index, set_index):
    def handle_event(event):
        set_index(index - 1)
    return html.button({"on_click":handle_event}, "-")

@component
def Contador():
    index, set_index = use_state(0)
    return html.div(
        Aumentar(index, set_index),
        html.p(index),
        Diminuir(index, set_index)
    )