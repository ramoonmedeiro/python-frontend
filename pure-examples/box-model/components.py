from reactpy import html, component
from reactpy_utils import DocumentTitle

styles = html.link({"href": "static/style.css", "rel": "stylesheet"})

@component
def Root():
    return html._(
        styles,
        DocumentTitle("BOX Model"),
        html.section(
            {"class": "section-one"},
            """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
            when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            """
        ),
        html.section(
            {"class": "section-two"},
            "2"
        )
)