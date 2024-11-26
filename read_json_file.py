import json
from pathlib import Path


def read_json_file() -> dict:
    path_to_file = Path(__file__).parent.joinpath("players.json")
    with open(path_to_file, "r") as file_read_stream:
        players = json.load(file_read_stream)

    return players
