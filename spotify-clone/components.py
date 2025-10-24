from reactpy import html, component
from reactpy_utils import DocumentTitle
from reactpy.svg import path
from config import SpotifyConfig


# Config de customização
### colors
hoverspt = SpotifyConfig.colors.value["hoverspt"]
purple_main = SpotifyConfig.colors.value["purple-main"]
green_main = SpotifyConfig.colors.value["green-main"]

### Background size
bgs = SpotifyConfig.backgroundSize.value
bg175 = bgs["175%"]
bg195 = bgs["195%"]

### Background position
bgp = SpotifyConfig.backgroundPosition.value
banner = bgp["banner"]
banner_mobile = bgp["banner-mobile"]

### Fontsize
fs = SpotifyConfig.fontSize.value
fs9xl = fs["9xl"]

# Config tailwind
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

favicon_link = html.link(
    {
        "rel": "icon",
        "href": "https://www.spotify.com/favicon.ico",
        "type": "image/x-icon"
    }
)

#font_poppins = html.link(
#    {
#        "rel": "stylesheet",
#        "href": "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap"
#    }
#)

font_awesome = html.link(
    {
        "rel": "stylesheet",
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css",
        "integrity":"sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==",
        "crossorigin": "anonymous",
        "referrerpolicy": "no-referrer"
    }
)


spotify_logo_svg = html.svg(
    {
        "xmlns": "http://www.w3.org/2000/svg",
        "viewBox": "0 0 823 225.25",
        "class": "w-24 h-auto fill-current",
    },
    path({
        'fill-rule': 'evenodd',
        "d": "m 125.52 3.31 C 65.14 0.91 14.26 47.91 11.86 108.29 c -2.4 60.38 44.61 111.26 104.98 113.66 c 60.38 2.4 111.26 -44.6 113.66 -104.98 C 232.89 56.59 185.89 5.7 125.52 3.31 Z m 46.18 160.28 c -1.36 2.4 -4.01 3.6 -6.59 3.24 c -0.79 -0.11 -1.58 -0.37 -2.32 -0.79 c -14.46 -8.23 -30.22 -13.59 -46.84 -15.93 c -16.62 -2.34 -33.25 -1.53 -49.42 2.4 c -3.51 0.85 -7.04 -1.3 -7.89 -4.81 c -0.85 -3.51 1.3 -7.04 4.81 -7.89 c 17.78 -4.32 36.06 -5.21 54.32 -2.64 c 18.26 2.57 35.58 8.46 51.49 17.51 c 3.13 1.79 4.23 5.77 2.45 8.91 Z m 14.38 -28.72 c -2.23 4.12 -7.39 5.66 -11.51 3.43 c -16.92 -9.15 -35.24 -15.16 -54.45 -17.86 c -19.21 -2.7 -38.47 -1.97 -57.26 2.16 c -1.02 0.22 -2.03 0.26 -3.01 0.12 c -3.41 -0.48 -6.33 -3.02 -7.11 -6.59 c -1.01 -4.58 1.89 -9.11 6.47 -10.12 c 20.77 -4.57 42.06 -5.38 63.28 -2.4 c 21.21 2.98 41.46 9.62 60.16 19.74 c 4.13 2.23 5.66 7.38 3.43 11.51 Z m 15.94 -32.38 c -2.1 4.04 -6.47 6.13 -10.73 5.53 c -1.15 -0.16 -2.28 -0.52 -3.37 -1.08 c -19.7 -10.25 -40.92 -17.02 -63.07 -20.13 c -22.15 -3.11 -44.42 -2.45 -66.18 1.97 c -5.66 1.15 -11.17 -2.51 -12.32 -8.16 c -1.15 -5.66 2.51 -11.17 8.16 -12.32 c 24.1 -4.89 48.74 -5.62 73.25 -2.18 c 24.51 3.44 47.99 10.94 69.81 22.29 c 5.12 2.66 7.11 8.97 4.45 14.09 Z"
    }),
    path({
        'fill-rule': 'evenodd',
        "d": "m 318.54 169.81 c -18.87 0 -35.07 -6.53 -41.84 -13.95 c -0.64 -0.73 -0.73 -1.13 -0.73 -2.02 v -22.09 c 0 -1.05 0.89 -1.45 1.61 -0.56 c 8.14 10.16 25.48 18.46 39.67 18.46 c 11.29 0 18.87 -3.06 18.87 -13.06 c 0 -5.97 -2.82 -9.84 -18.22 -14.19 l -8.87 -2.5 c -20.56 -5.8 -33.06 -12.66 -33.06 -32.33 c 0 -17.41 16.12 -32.73 43.05 -32.73 c 13.22 0 26.36 4.11 33.94 9.76 c 0.64 0.48 0.89 0.97 0.89 1.85 v 20.08 c 0 1.37 -1.13 1.77 -2.18 0.89 c -6.13 -5.08 -17.98 -11.93 -32.01 -11.93 s -20.64 6.29 -20.64 12.09 c 0 6.13 4.27 7.82 19.51 12.34 l 7.58 2.26 c 23.46 7.01 33.06 16.85 33.06 33.14 c 0 20.96 -17.41 34.51 -40.63 34.51 Z m 164.39 -42.09 c 0 -12.82 8.87 -22.33 21.37 -22.33 s 21.28 9.51 21.28 22.33 s -8.87 22.33 -21.28 22.33 s -21.37 -9.51 -21.37 -22.33 Z m 21.28 42.09 c 26.04 0 44.18 -18.62 44.18 -42.09 s -18.14 -42.09 -44.18 -42.09 s -44.1 18.46 -44.1 42.09 s 17.98 42.09 44.1 42.09 Z m 157.22 -89.01 v 6.77 h -13.71 c -0.73 0 -1.13 0.4 -1.13 1.13 v 16.12 c 0 0.73 0.4 1.13 1.13 1.13 h 13.71 v 60.79 c 0 0.73 0.4 1.13 1.13 1.13 h 20.64 c 0.73 0 1.13 -0.4 1.13 -1.13 v -60.79 h 17.66 l 25.64 55.71 l -13.79 30.31 c -0.4 0.89 0.08 1.29 0.89 1.29 h 22.01 c 0.73 0 1.05 -0.16 1.37 -0.89 l 45.55 -103.52 c 0.32 -0.73 -0.08 -1.29 -0.89 -1.29 h -20.64 c -0.73 0 -1.05 0.16 -1.37 0.89 l -20.8 49.99 l -20.88 -49.99 c -0.32 -0.73 -0.64 -0.89 -1.37 -0.89 h -33.38 v -5.32 c 0 -8.71 5.89 -12.74 13.46 -12.74 c 4.51 0 9.43 2.34 12.9 4.43 c 0.81 0.48 1.37 -0.08 1.05 -0.81 l -7.26 -17.33 c -0.24 -0.56 -0.56 -0.89 -1.13 -1.21 c -3.55 -1.85 -9.35 -3.47 -15 -3.47 c -17.09 0 -26.93 13.06 -26.93 29.67 Z m -243 88.52 c 20.64 0 35.47 -17.82 35.47 -41.76 s -15 -41.44 -35.64 -41.44 c -15.32 0 -24.19 9.35 -29.35 18.7 v -16.12 c 0 -0.73 -0.4 -1.13 -1.13 -1.13 h -20.24 c -0.73 0 -1.13 0.4 -1.13 1.13 v 103.44 c 0 0.73 0.4 1.13 1.13 1.13 h 20.24 c 0.73 0 1.13 -0.4 1.13 -1.13 v -41.36 c 5.16 9.35 13.87 18.54 29.51 18.54 Z m 172.21 -0.32 c 6.77 0 13.3 -1.77 17.17 -4.03 c 0.56 -0.32 0.64 -0.64 0.64 -1.21 v -15.32 c 0 -0.81 -0.4 -1.05 -1.13 -0.64 c -2.34 1.29 -5.4 2.34 -9.59 2.34 c -6.61 0 -10.8 -3.87 -10.8 -12.42 v -31.77 h 20.16 c 0.73 0 1.13 -0.4 1.13 -1.13 v -16.12 c 0 -0.73 -0.4 -1.13 -1.13 -1.13 h -20.16 v -21.04 c 0 -0.89 -0.56 -1.37 -1.37 -0.73 l -36.04 28.38 c -0.48 0.4 -0.64 0.81 -0.64 1.45 v 9.19 c 0 0.73 0.4 1.13 1.13 1.13 h 14.03 v 35.15 c 0 19.03 10.96 27.9 26.61 27.9 Z m 23.3 -105.29 c 0 7.26 5.64 12.74 13.38 12.74 s 13.54 -5.48 13.54 -12.74 s -5.64 -12.74 -13.54 -12.74 s -13.38 5.48 -13.38 12.74 Z m 3.14 104.17 h 20.64 c 0.73 0 1.13 -0.4 1.13 -1.13 v -78.04 c 0 -0.73 -0.4 -1.13 -1.13 -1.13 h -20.64 c -0.73 0 -1.13 0.4 -1.13 1.13 v 78.04 c 0 0.73 0.4 1.13 1.13 1.13 Z m -228.65 -40.47 c 3.71 -12.42 12.25 -21.93 23.86 -21.93 s 18.7 8.38 18.7 22.09 s -7.66 22.25 -18.7 22.25 s -20.16 -10.64 -23.86 -22.41 Z"
    }),
    path({
        'fill-rule': 'evenodd',
        "d": "m 810.1 92.31 c -1.06 -1.83 -2.53 -3.26 -4.41 -4.3 c -1.88 -1.03 -3.98 -1.55 -6.32 -1.55 s -4.44 0.52 -6.32 1.55 c -1.88 1.04 -3.35 2.47 -4.41 4.3 c -1.06 1.83 -1.59 3.9 -1.59 6.21 s 0.53 4.34 1.59 6.17 c 1.06 1.83 2.53 3.26 4.41 4.3 c 1.88 1.04 3.98 1.55 6.32 1.55 s 4.44 -0.52 6.32 -1.55 s 3.35 -2.47 4.41 -4.3 c 1.06 -1.83 1.59 -3.88 1.59 -6.17 s -0.53 -4.38 -1.59 -6.21 Z m -1.93 11.36 c -0.86 1.52 -2.06 2.7 -3.59 3.56 c -1.53 0.85 -3.27 1.28 -5.2 1.28 s -3.72 -0.43 -5.25 -1.28 c -1.53 -0.85 -2.72 -2.04 -3.57 -3.56 c -0.85 -1.51 -1.27 -3.23 -1.27 -5.15 s 0.42 -3.63 1.27 -5.13 c 0.85 -1.5 2.04 -2.68 3.57 -3.53 c 1.53 -0.85 3.28 -1.28 5.25 -1.28 s 3.67 0.43 5.2 1.28 c 1.53 0.85 2.73 2.04 3.59 3.56 c 0.86 1.52 1.29 3.23 1.29 5.15 s -0.43 3.59 -1.29 5.11 Z"
    }),
    path({
        'fill-rule': 'evenodd',
        "d": "m 803.56 98.29 c 0.82 -0.6 1.23 -1.4 1.23 -2.39 s -0.4 -1.83 -1.2 -2.43 c -0.8 -0.6 -1.96 -0.9 -3.48 -0.9 h -5.36 v 11.2 h 2.59 v -4.45 h 1.41 l 3.41 4.45 h 3.18 l -3.73 -4.72 c 0.79 -0.15 1.46 -0.4 1.96 -0.77 Z m -3.86 -0.99 h -2.36 v -2.74 h 2.45 c 0.73 0 1.29 0.11 1.68 0.34 c 0.39 0.23 0.59 0.58 0.59 1.06 c 0 0.45 -0.21 0.79 -0.61 1.01 c -0.41 0.23 -0.99 0.34 -1.75 0.34 Z"
    })
)

@component
def NavBar():
    return html.header(
        html.div( # Div para conseguir customizar os elementos dentro da header
            {"class": "flex fixed bg-black w-full px-3 text-white md:px-20 py-4"},
            html.div( # Div que cuidará do logo 
                html.a(
                    {
                        "href": "#",
                        "class": f"hover:text-[{hoverspt}]"
                    },
                    spotify_logo_svg
                )
            ),
            html.div( # Div que cuida do botão de listagem de elementos
                {"class": "flex justify-end flex-1 md:hidden text-white text-3xl"},
                html.i(
                    {"class": "fas fa-bars"}
                )
            ),
            html.div( # Div para a nav bar
                {"class": "flex items-end flex-1 text-white font-bold hidden md:block"},
                html.nav(
                    {"class": "flex-1"},
                    html.ul(
                        {"class": "flex justify-end flex-1"},
                        html.li(
                            {"class": "px-4"},
                            html.a(
                                {
                                    "href": "#",
                                    "class": f"hover:text-[{hoverspt}] text-sm"
                                },
                                "Premium"
                            )
                        ),
                        html.li(
                            {"class": "px-4"},
                            html.a(
                                {
                                    "href": "#",
                                    "class": f"hover:text-[{hoverspt}] text-sm"
                                },
                                "Ajuda"
                            )
                        ),
                        html.li(
                            {"class": "px-4"},
                            html.a(
                                {
                                    "href": "#",
                                    "class": f"hover:text-[{hoverspt}] text-sm"
                                },
                                "Baixar"
                            )
                        ),
                        html.li(
                            {"class": "border-r border-white"},
                            html.span()
                        ),
                        html.li(
                            {"class": "px-4"},
                            html.a(
                                {
                                    "href": "#",
                                    "class": f"hover:text-[{hoverspt}] text-sm"
                                },
                                "Inscrever-se"
                            )
                        ),
                        html.li(
                            {"class": "px-4"},
                            html.a(
                                {
                                    "href": "#",
                                    "class": f"hover:text-[{hoverspt}] text-sm"
                                },
                                "Entrar"
                            )
                        ),
                    )
                )
            )
        )
    )


@component
def Main():
    return html.main(
        html.div(
            {"class": f"flex flex-col justify-center text-center py-40 px-4 text-[{green_main}] bg-[{purple_main}] bg-[{banner_mobile}] md:bg-[{banner}] bg-[{bg195}] md:bg-[{bg175}]"},
            html.h1(
                {
                    "class": f"text-5xl md:text-[{fs9xl}] mb-10 font-bold max-w-4xl mx-auto leading-none"
                },
                "Escutar muda tudo"
            ),
            html.p(
                {"class": "text-md md:text-lg mb-10"},
                "Milhões de músicas e podcasts para explorar. E nem precisa de cartão de crédito"
            ),
            html.a(
                {
                    "href": "#",
                    "class": f"bg-[{green_main}] hover:bg-white text-[{purple_main}] text-sm rounded-full px-10 py-3 uppercase font-bold max-w-xl mx-auto tracking-widest transition duration-500"
                },
                "Obtenha o Spotify Free"
            )
        )
    )


@component
def Footer():
    return html.footer(
        html.div(
            {"class": "grid grid-cols-1 md:grid-cols-6 bg-black text-white p-4 md:p-20"},
            html.div(
                {"class": "md:col-span-1 pt-10 md:pt-0"},
                html.a(
                    {"href": "#"},
                    spotify_logo_svg
                )
            ),
            html.div(
                {"class": "md:col-span-1 pt-10 md:pt-4"},
                html.h3(
                    {"class": "uppercase text-gray-500 font-bold text-xs tracking-widest mb-5"},
                    "Empresa"
                ),
                html.ul(
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Sobre"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Empregos"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "For the record"
                        )
                    )
                )
            ),
            html.div(
                {"class": "md:col-span-1 pt-10 md:pt-4"},
                html.h3(
                    {"class": "uppercase text-gray-500 font-bold text-xs tracking-widest mb-5"},
                    "Comunidades"
                ),
                html.ul(
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Para Artistas"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Desenvolvedores"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Publicidade"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Investidores"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Fornecedores"
                        )
                    )
                )
            ),
            html.div(
                {"class": "md:col-span-1 pt-10 md:pt-4"},
                html.h3(
                    {"class": "uppercase text-gray-500 font-bold text-xs tracking-widest mb-5"},
                    "Links Úteis"
                ),
                html.ul(
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Ajuda"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Player da Web"
                        )
                    ),
                    html.li(
                        {"class": "mb-5"},
                        html.a(
                            {"href": "#"},
                            "Aplicativo Móvel Grátis"
                        )
                    )
                )
            ),
            html.div(
                {"class": "md:col-span-2 pt-10 md:pt-4"},
                html.ul(
                    {"class": "flex md:justify-end"},
                    html.li(
                        {"class": f"flex items-center justify-center text-2xl bg-gray-900 w-12 h-12 rounded-full hover:text-[{green_main}] mx-2"},
                        html.a(
                            {"href": "#"},
                            html.i({"class": "fab fa-instagram"})
                        )
                    ),
                    html.li(
                        {"class": f"flex items-center justify-center text-2xl bg-gray-900 w-12 h-12 rounded-full hover:text-[{green_main}] mx-2"},
                        html.a(
                            {"href": "#"},
                            html.i({"class": "fab fa-twitter"})
                        )
                    ),
                    html.li(
                        {"class": f"flex items-center justify-center text-2xl bg-gray-900 w-12 h-12 rounded-full hover:text-[{green_main}] mx-2"},
                        html.a(
                            {"href": "#"},
                            html.i({"class": "fab fa-facebook-f"})
                        )
                    )
                )
            ),
            html.div(
                {"class": "md:col-span-4 mt-20"},
                html.ul(
                    html.li(
                        {"class": "inline-block text-xs text-gray-600 mr-4"},
                        html.a(
                            {"href": "#"},
                            "Legal"
                        )
                    ),
                    html.li(
                        {"class": "inline-block text-xs text-gray-600 mr-4"},
                        html.a(
                            {"href": "#"},
                            "Centro de Privacidade"
                        )
                    ),
                    html.li(
                        {"class": "inline-block text-xs text-gray-600 mr-4"},
                        html.a(
                            {"href": "#"},
                            "política de Privacidade"
                        )
                    ),
                    html.li(
                        {"class": "inline-block text-xs text-gray-600 mr-4"},
                        html.a(
                            {"href": "#"},
                            "Cookies"
                        )
                    ),
                    html.li(
                        {"class": "inline-block text-xs text-gray-600 mr-4"},
                        html.a(
                            {"href": "#"},
                            "Sobre Anúnicos"
                        )
                    ),
                )
            ),
            html.div(
                {"class": "md:col-span-2 mt-20"},
                html.p(
                    {"class": "flex justify-end text-gray-500 text-xs"},
                    "© 2020 Spotify AB"
                )
                )
            )
        )

@component
def Index():
    return html._(
        DocumentTitle("Clone Spotify"),
        font_awesome,
        favicon_link,
        cdn,
        # Nav Bar
        NavBar(),
        # Conteúdo
        Main(),
        # Footer
        Footer()
    )