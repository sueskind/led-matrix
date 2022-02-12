import json
import os
from dataclasses import dataclass


@dataclass
class Frame:
    pixels: list[str]


class Settings:

    def __init__(self, path: str):
        settings = dict()

        if os.path.exists(path):
            with open(path, "r") as f:
                settings = json.load(f)

        self.speed = settings.get("speed", 100)


@dataclass
class Animation:
    id: str
    name: str
    frames: list[Frame]
    settings: Settings
