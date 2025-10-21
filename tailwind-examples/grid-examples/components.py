from reactpy import component, html
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Home():
    return html._(
        cdn,
        # Colunas no grid
        html.div(
            {"class": "grid grid-cols-3 bg-red-400 m-4"},
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
        html.div(
            {"class": "grid grid-cols-2 bg-blue-500 m-4"},
            html.div(
                "1"
            ),
            html.div(
                "2"
            )
        ),
        # Tamanho das colunas
        html.div(
            {"class": "grid grid-cols-6 m-3"},
            html.div(
                {"class": "col-span-1 bg-yellow-300"},
                html.ul(
                    html.li("Home"),
                    html.li("Produtos"),
                    html.li("Contato"),
                    html.li("Blog"),
                )
            ),
            html.div(
                {"class": "col-span-5 bg-blue-300"},
                html.p("""
                    Why do we use it?
                    It is a long established fact that 
                    a reader will be distracted by the readable content of a page when looking at its layout. 
                    The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, 
                    as opposed to using 'Content here, content here', making it look like readable English.
                """)
            )
        ),
        html.div(
            {"class": "grid grid-cols-4 m-2"},
            html.div(
                {"class": "col-span-1 m-1 bg-red-400"},
                html.p("Barra Lateral Esquerda")
            ),
            html.div(
                {"class": "col-span-2 m-1 bg-red-200"},
                html.p("""
                    Why do we use it?
                    It is a long established fact that 
                    a reader will be distracted by the readable content of a page when looking at its layout. 
                    The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, 
                    as opposed to using 'Content here, content here', making it look like readable English.
                """)
            ),
            html.div(
                {"class": "col-span-1 m-1 bg-red-400"},
                html.p("Barra Lateral Direita")
            )
        ),
        html.div(
            {"class": "grid grid-cols-4 p-2"},
            html.div(
                {"class": "col-span-4 bg-green-400 text-white"},
                html.p("Barra de Navegação")
            ),
            html.div(
                {"class": "col-span-1 bg-cyan-500"},
                html.ul(
                    html.li("Home"),
                    html.li("Perfil"),
                    html.li("API Key"),
                    html.li("Logout")
                )
            ),
            html.div(
                {"class": "col-span-3 bg-cyan-300"},
                html.p("""
                    Why do we use it?
                    It is a long established fact that 
                    a reader will be distracted by the readable content of a page when looking at its layout. 
                    The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, 
                    as opposed to using 'Content here, content here', making it look like readable English.
                """)
            )
        ),
        # Espaçamento de colunas e linhas
        html.div(
            {"class": "grid grid-cols-3 m-4 gap-2"},
            html.div(
                {"class": "bg-purple-300"},
                "1"
            ),
            html.div(
                {"class": "bg-purple-400"},
                "2"
            ),
            html.div(
                {"class": "bg-purple-500"},
                "3"
            ),
            html.div(
                {"class": "bg-purple-300"},
                "4"
            ),
            html.div(
                {"class": "bg-purple-400"},
                "5"
            ),
            html.div(
                {"class": "bg-purple-500"},
                "6"
            ),

        )
    )