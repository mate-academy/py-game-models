import os
import json


config_path = os.path.join(os.path.dirname(__file__), "players.json")

with open(config_path, "r") as file:
    players_data = json.load(file)
