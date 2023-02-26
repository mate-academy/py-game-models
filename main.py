import init_django_orm  # noqa: F401
import json
from player_moduls.race_func import race_func
from player_moduls.skill_func import skill_func
from player_moduls.guild_func import guild_func
from player_moduls.player_func import player_func
from db.models import Player, Skill, Guild, Race


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

        for player_name, player in players.items():
            player_func(players)
            race_func(player)
            skill_func(player)
            guild_func(player)


if __name__ == "__main__":
    main()
