from reactpy import component, html
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Home():
    return html._(
        cdn,
        # Flex directions
        ## Flex em linha
        html.div(
            {"class": "flex flex-row bg-red-400 m-4"},
            html.div(
                {"class": "bg-blue-300 p-6 m-2"},
                "1"
            ),
            html.div(
                {"class": "bg-blue-300 p-6 m-2"},
                "2"
            ),
            html.div(
                {"class": "bg-blue-300 p-6 m-2"},
                "3"
            )
        ),
        ## Flex em colunas
        html.div(
            {"class": "flex flex-col bg-blue-400 m-4 p-6"},
            html.div(
                {"class": "bg-red-400 my-2"},
                "1"
            ),
            html.div(
                {"class": "bg-red-400 my-2"},
                "2"
            ),
            html.div(
                {"class": "bg-red-400 my-2"},
                "3"
            )
        ),
        html.div(
            {"class": "flex flex-col bg-cyan-200 m-2 p-6 border-3 border-blue-400"},
            html.div(
                {"class": "bg-cyan-300 my-1"},
                "1"
            ),
            html.div(
                {"class": "bg-cyan-400 my-1"},
                "2"
            ),
            html.div(
                {"class": "bg-cyan-500 my-1"},
                "3"
            ),
            html.div(
                {"class": "bg-cyan-600 my-1"},
                "4"
            ),
            html.div(
                {"class": "bg-cyan-700 my-1"},
                "5"
            ),
            html.div(
                {"class": "bg-cyan-800 my-1"},
                "6"
            )
        ),
        # Wrap
        html.div(
            {"class": "flex flex-wrap bg-red-300"},
            html.div(
                {"class": "bg-blue-300 p-6 m-4"},
                "1"
            ),
            html.div(
                {"class": "bg-blue-300 p-6 m-4"},
                "2"
            ),
            html.div(
                {"class": "bg-blue-300 p-6 m-4"},
                "3"
            ),
            html.div(
                {"class": "bg-blue-300 p-6 m-4"},
                "4"
            ),
            html.div(
                {"class": "bg-blue-300 p-6 m-4"},
                "5"
            ),
            html.div(
                {"class": "bg-blue-300 p-6 m-4"},
                "6"
            )
        )
    )