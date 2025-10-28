from reactpy_utils import DocumentTitle
from reactpy import component, html
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})


@component
def Root():
    return html._(
        cdn,
        # Alinhamento de containers
        html.div(
            {
                "class": "flex p-2 bg-red-300 justify-end"
            },
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "1"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "2"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "3"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "4"
            ),
        ),
        html.div(
            {
                "class": "flex p-2 bg-green-300 justify-between"
            },
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "1"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "2"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "3"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "4"
            ),
        ),
        html.div(
            {
                "class": "flex p-2 bg-blue-300 justify-center"
            },
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "1"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "2"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "3"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "4"
            ),
        ),
        html.div(
            {
                "class": "flex p-2 bg-cyan-700 justify-around"
            },
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "1"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "2"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "3"
            ),
            html.div(
                {"class": "bg-red-600 p-4 m-4"},
                "4"
            ),
        ),
        # Alinhamento de Conteúdo
        html.div(
            {
                "class": "flex bg-purple-300 h-40 flex-wrap content-center"
            },
            html.div(
                {"class": "bg-purple-600 h-10 p-2 mx-4"},
                "1"
            ),
            html.div(
                {"class": "bg-purple-600 h-10 p-2 mx-4"},
                "2"
            ),
            html.div(
                {"class": "bg-purple-600 h-10 p-2 mx-4"},
                "3"
            ),
        ),
        html.div(
            {
                "class": "flex bg-teal-300 h-40 flex-wrap content-around"
            },
            html.div(
                {"class": "bg-purple-600 h-10 p-2 w-1/3"},
                "1"
            ),
            html.div(
                {"class": "bg-purple-600 h-10 p-2 w-1/3"},
                "2"
            ),
            html.div(
                {"class": "bg-purple-600 h-10 p-2 w-1/3"},
                "3"
            ),
            html.div(
                {"class": "bg-purple-600 h-10 p-2 w-1/3"},
                "4"
            ),
            html.div(
                {"class": "bg-purple-600 h-10 p-2 w-1/3"},
                "5"
            ),
            html.div(
                {"class": "bg-purple-600 h-10 p-2 w-1/3"},
                "6"
            ),
        ),
        # Alinhamento de itens
        html.div(
            {"class": "bg-purple-500 flex h-40 items-start"}, # Pode ter -end -stretch -center
            html.div(
                {"class": "bg-teal-700 m-2 p-2"},
                "1"
            ),
            html.div(
                {"class": "bg-teal-700 m-2 p-2"},
                "2"
            ),
            html.div(
                {"class": "bg-teal-700 m-2 p-2"},
                "3"
            )
        ),
        # Alinhamento e espaçamento de grid (conteúdo)
        html.div(
            {"class": "grid bg-blue-300 grid-cols-3 h-40 place-content-center"}, # poder -end -between -start -around
            html.div(
                {"class": "bg-blue-600 p-2 m-2"},
                "1"
            ),
            html.div(
                {"class": "bg-blue-600 p-2 m-2"},
                "2"
            ),
            html.div(
                {"class": "bg-blue-600 p-2 m-2"},
                "3"
            ),
            html.div(
                {"class": "bg-blue-600 p-2 m-2"},
                "4"
            ),
            html.div(
                {"class": "bg-blue-600 p-2 m-2"},
                "5"
            ),
            html.div(
                {"class": "bg-blue-600 p-2 m-2"},
                "6"
            )
        ),
        # Alinhamento e espaçamento em grid (Itens)
        html.div(
            {"class": "grid bg-pink-300 grid-cols-3 h-40 place-items-center"}, # poder -end -between -start -around
            html.div(
                {"class": "bg-pink-600 p-2 m-2"},
                "1"
            ),
            html.div(
                {"class": "bg-pink-600 p-2 m-2"},
                "2"
            ),
            html.div(
                {"class": "bg-pink-600 p-2 m-2"},
                "3"
            ),
            html.div(
                {"class": "bg-pink-600 p-2 m-2"},
                "4"
            ),
            html.div(
                {"class": "bg-pink-600 p-2 m-2"},
                "5"
            ),
            html.div(
                {"class": "bg-pink-600 p-2 m-2"},
                "6"
            )
        ),
        # Exercício 
        # Crie um componente com aspecto de botão
        html.div(
            {"class": "bg-white m-5"},
            html.button(
                {"class": "bg-gray-300 m-5 px-4 py-2 font-bold hover:bg-gray-900 rounded"},
                "Aperte aqui"
            )
        )
    )