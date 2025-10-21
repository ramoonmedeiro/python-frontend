from reactpy import html, component
from reactpy_utils import DocumentTitle
import json
from tailwind_config import TailwindConfig


tailwind_config_json = json.dumps(TailwindConfig.custom_config.value, indent=4)
tailwind_config_script = html.script(
    {"type": "text/tailwindcss-config"},
    tailwind_config_json
)

styles = html.link({"href": "static/style.css", "rel": "stylesheet"})
cdn = html.script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"})

@component
def Root():
    return html._(
        cdn,
        styles,
        tailwind_config_script,
        DocumentTitle("Site básico"),
        html.p("Tá no ar porra")
)