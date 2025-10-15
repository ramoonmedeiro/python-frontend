from reactpy import html, component

cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Home():
    return html.div(
        cdn,
        # Exemplo 1
        html.div(
            {"class": "container bg-red-300 mx-auto my-4 p-4 border-2"},
            html.p("O texto do container")
        ),
        # Border Box e Box content
        html.div(
            {"class": "container bg-purple-400 m-4 border-box p-10 border-4 border-red-300"},
            html.p("Border box")
        ),
        html.div(
            {"class": "container bg-teal-400 m-4 box-content p-10 border-4 border-teal-900"},
            html.p("Box content")
        ),
        # DISPLAY
        html.div(
            {"class": "container"},
            html.span(
                {"class":"block"},
                "Não são elementos de bloco"
            ),
            html.span(
                {"class":"block"},
                "Não são elementos de bloco"
            )
        ),
        # Exercício sobre display
        # Criar 3 divs, deixar as 3 inline e colocar bg distintos para cada
        html.div(
            {"class": "container bg-teal-200 p-6"},
            html.div(
                {"class": "bg-green-800 inline-block"},
                "DIV 1"
            ),
            html.div(
                {"class": "bg-blue-800 inline-block"},
                "DIV 2"
            ),
            html.div(
                {"class": "bg-red-800 inline-block"},
                "DIV 3"
            ),
        ),
        # Overflow
        html.div(
            {"class": "overflow-auto h-16 m-6 bg-red-900"},
            html.p(
                "Testando overflow"
            ),
            html.p(
                "Testando overflow"
            ),
            html.p(
                "Testando overflow"
            ),
            html.p(
                "Testando overflow"
            ),
            html.p(
                "Testando overflow"
            ),
            html.p(
                "Testando overflow"
            )
        ),
        # Positions
        html.div(
            {"class": "absolute top-0 right-0 bg-pink-900"},
            "ABSOLUTE"
        ),
        # Z-index
        html.div(
            {"class": "container relative"},
            html.div(
                {"class":"bg-red-300 h-20 w-20 p-6 absolute z-10"},
                "DIV 1"
            ),
            html.div(
                {"class": "bg-red-500 h-20 w-20 p-6 absolute m-4"},
                "DIV 2"
            )
        )
    )