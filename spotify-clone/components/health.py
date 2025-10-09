from reactpy import html, component

cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Health():
    return html.div(
        cdn,
        html.p("Health Check")
    )