from reactpy import component, html
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Home():
    return html.div(
        cdn,
        # flex box em linha
        html.div(
            {"class": "flex flex-row bg-red-300"},
            html.div(
                {"class": "bg-red-600 p-6 m-2"},
                "1"
            ),
            html.div(
                {"class": "bg-red-600 p-6 m-2"},
                "2"
            ),
            html.div(
                {"class": "bg-red-600 p-6 m-2"},
                "3"
            )        
        ),
        #flex box em coluna
        html.div(
            {"class": "flex flex-col bg-blue-300"},
            html.div(
                {"class": "bg-blue-600 p-6 m-2"},
                "1"
            ),
            html.div(
                {"class": "bg-blue-600 p-6 m-2"},
                "2"
            ),
            html.div(
                {"class": "bg-blue-600 p-6 m-2"},
                "3"
            )        
        ),
        # Exercício 1 do flexbox
        # Criar container com flex col, 5 itens com cores diferentes
        html.div(
            {"class": "flex flex-col bg-teal-900"},
            html.div(
                {"class": "bg-green-400 p-3 m-2"},
                "1"
            ),
            html.div(
                {"class": "bg-red-400 p-3 m-2"},
                "2"
            ),
            html.div(
                {"class": "bg-pink-400 p-3 m-2"},
                "3"
            ),
            html.div(
                {"class": "bg-blue-400 p-3 m-2"},
                "4"
            ),
            html.div(
                {"class": "bg-purple-400 p-3 m-2"},
                "5"
            )
        ),
        # Wrap
        html.div(
            {"class": "flex flex-row flex-wrap bg-red-300"},
            html.div(
                {"class": "bg-green-400 p-3 m-2"},
                "1"
            ),
            html.div(
                {"class": "bg-red-400 p-3 m-2"},
                "2"
            ),
            html.div(
                {"class": "bg-pink-400 p-3 m-2"},
                "3"
            ),
            html.div(
                {"class": "bg-blue-400 p-3 m-2"},
                "4"
            ),
            html.div(
                {"class": "bg-purple-400 p-3 m-2"},
                "5"
            )
        ),
        # Order
        html.div(
            {"class": "flex bg-teal-300"},
            html.div(
                {"class": "bg-purple-400 p-3 m-2 order-last"},
                "1"
            ),
            html.div(
                {"class": "bg-purple-400 p-3 m-2 order-4"},
                "2"
            ),
            html.div(
                {"class": "bg-purple-400 p-3 m-2 order-3"},
                "3"
            ),
            html.div(
                {"class": "bg-purple-400 p-3 m-2 order-first"},
                "4"
            ),
            html.div(
                {"class": "bg-purple-400 p-3 m-2 order-2"},
                "5"
            )
        )
    )