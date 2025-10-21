from reactpy import html, component

cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Home():
    return html._(
        cdn,
        html.div(
            {
                "class": "container bg-red-300 mx-auto my-4 p-4 text-blue-900 border-2 border-black"
            },
            html.p("Olá")
        ),
        html.div(
            {
                "class": "container bg-green-700 md:bg-blue-900"
            },
            "OI"
        ),
        # Border Box e Border Content
        html.div(
            {"class": "container bg-purple-700 m-4 border-2 border-box p-10"},
            "Border BOX"
        ),
        html.div(
            {"class": "container bg-teal-500 m-4 border-2 border-content p-10"},
            "Box Content"
        ),
        # Blocks
        html.div(
            {"class": "container"},
            html.span(
                {"class": "block bg-red-500"},
                "Bloco 1"
            ),
            html.span(
                {"class": "block bg-red-500"},
                "Bloco 2"
            ),
            html.div(
                {"class": "bg-purple-500 inline-block"},
                "Bloco div 1"
            ),
            html.div(
                {"class": "bg-purple-500 inline-block mx-2"},
                "Bloco div 2"
            )
        ),
        # inline-block
        html.div(
            {"class": "container bg-green-700 p-4 my-4"},
            html.div(
                {"class": "bg-red-700 inline-block mx-2"},
                "div 1"
            ),
            html.div(
                {"class": "bg-blue-700 inline-block mx-2"},
                "div 2"
            ),
            html.div(
                {"class": "bg-yellow-700 inline-block mx-2"},
                "div 3"
            )
        ),
        # Positions
        html.div(
            {"class": "relative bg-green-200 p-5"},
            "AI",
            html.div(
                {"class": "absolute top-0 right-0 bg-pink-300"},
                "Absolute"
            )
        ),
        # Visibility
        html.div(
            {"class": "container bg-red-600 m-4 border-3 p-4 invisible"},
            "Estou oculto"
        )
    )