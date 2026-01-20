import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for name, player_info in players.items():
        race_dict = player_info["race"]
        if not Race.objects.filter(name=race_dict["name"]).exists():
            race = Race.objects.create(
                name=race_dict["name"],
                description=race_dict["description"])
            for skill in race_dict["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race)
        else:
            race = Race.objects.get(name=race_dict["name"])

        guild_dict = player_info["guild"]

        if guild_dict:
            if not Guild.objects.filter(name=guild_dict["name"]).exists():
                guild = Guild.objects.create(
                    name=guild_dict["name"],
                    description=guild_dict["description"])
            else:
                guild = Guild.objects.get(name=guild_dict["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
