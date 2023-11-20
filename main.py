import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for player_name, player_info in players_data.items():
        race, _ = Race.objects.get_or_create(name=player_info["race"]["name"], description=player_info["race"]["description"])
        guild, _ = Guild.objects.get_or_create(name=player_info['guild']['name'], description=player_info["guild"]["description"]) if player_info['guild'] else (None, False)

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"], bonus=skill["bonus"], race=race)

        Player.objects.create(nickname=player_name, email=player_info["email"], bio=player_info["bio"], race=race, guild=guild)


if __name__ == "__main__":
    main()
