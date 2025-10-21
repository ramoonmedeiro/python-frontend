from enum import Enum


class TailwindConfig(Enum):
    custom_config: dict = {
        "theme": {
            "extend": {}
        },
        "plugins": [],
        "future": {},
        "variants": {},
        "purge": []
    }