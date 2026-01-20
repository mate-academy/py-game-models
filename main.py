import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_info in data.items():
        Race.objects.get_or_create(name=player_info["race"]["name"],
                                   description=player_info["race"]["description"]) # noqa
        race_example = Race.objects.get(name=player_info["race"]["name"])
        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race_example)
        if player_info["guild"]:
            Guild.objects.get_or_create(name=player_info["guild"]["name"],
                                        description=player_info["guild"]["description"]) # noqa
        guild_example = Guild.objects.get(name=player_info["guild"]["name"]) \
            if player_info["guild"] else None
        Player.objects.get_or_create(nickname=player_name,
                                     email=player_info["email"],
                                     bio=player_info["bio"],
                                     race=race_example,
                                     guild=guild_example)


if __name__ == "__main__":
    main()
