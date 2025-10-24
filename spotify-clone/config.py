from enum import Enum
from typing import Dict

class SpotifyConfig(Enum):
    colors: Dict[str, str] = {
        "hoverspt": "#18D760",
        "purple-main": "#2D46B9",
        "green-main": "#1ED760"
    }

    backgroundSize: Dict[str, str] = {
        "175%": "175%",
        "195%": "195%"
    }

    backgroundPosition: Dict[str, str] = {
        "banner": "46\% 4\%",
        "banner-mobile": "top 25\% \center"
    }

    fontSize: Dict[str, str] = {
        "9xl": "9rem"
    }