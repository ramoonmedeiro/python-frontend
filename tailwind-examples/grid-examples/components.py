from reactpy import component, html
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Home():
    return html.div(
        cdn,
        html.div(
            {"class": "grid bg-red-300 grid-cols-3"},
            html.div(
                "1"
            ),
            html.div(
                "2"
            ),
            html.div(
                "3"
            )
        ),
        # Grid col-span
        html.div(
            {"class": "grid grid-cols-6 m-2"},
            html.div(
                {"class": "col-span-1 bg-yellow-500"},
                html.ul(
                    html.li("Home"),
                    html.li("Produtos"),
                    html.li("Contato"),
                    html.li("Blog")
                )
            ),
            html.div(
                {"class": "col-span-5 bg-blue-500"},
                html.p(
                    "Loremdfisdusdfhshfhsdfuihsdiufhsdifuhsdiufhdsiufhsduifhdsuif"
                )
            )
        ),
        html.div(
            {"class": "grid grid-cols-4 m-2"},
            html.div(
                {"class": "col-span-1 bg-red-700"},
                html.p("Barra lateral esquerda")
            ),
            html.div(
                {"class": "col-span-2 bg-red-300"},
                html.p("Conteúdo")
            ),
            html.div(
                {"class": "col-span-1 bg-red-700"},
                html.p("Barra lateral direita")
            )
        ),
        # Rows no grid
        html.div(
            {"class": "grid grid-rows-4 grid-flow-col"},
            html.div(
                {"class": "bg-green-400"},
                "1"
            ),
            html.div(
                {"class": "bg-green-800"},
                "2"
            ),
            html.div(
                {"class": "bg-green-400"},
                "3"
            ),
            html.div(
                {"class": "bg-green-800"},
                "4"
            ),
            html.div(
                {"class": "bg-green-400"},
                "5"
            ),
            html.div(
                {"class": "bg-green-800"},
                "6"
            ),
            html.div(
                {"class": "bg-green-400"},
                "7"
            ),
            html.div(
                {"class": "bg-green-800"},
                "8"
            ),
        ),
        # Gap
        html.div(
            {"class": "grid grid-cols-3 m-4 gap-2"},
            html.div(
                {"class": "bg-purple-300"},
                "1"
            ),
            html.div(
                {"class": "bg-purple-500"},
                "2"
            ),
            html.div(
                {"class": "bg-purple-300"},
                "3"
            ),
            html.div(
                {"class": "bg-purple-500"},
                "4"
            ),
            html.div(
                {"class": "bg-purple-300"},
                "5"
            ),
            html.div(
                {"class": "bg-purple-500"},
                "6"
            ),
            html.div(
                {"class": "bg-purple-300"},
                "7"
            ),
            html.div(
                {"class": "bg-purple-500"},
                "8"
            ),
            html.div(
                {"class": "bg-purple-300"},
                "9"
            )
        )
    )