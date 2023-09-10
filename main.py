import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    race_obj, guild_obj = None, None

    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    with open('players.json', 'r') as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data["race"]
        guild_data = player_data["guild"]

        if not Race.objects.filter(name=race_data["name"]).exists():
            race_obj = Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )

        for skill in race_data["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

        if guild_data is not None:
            if guild_data and not Guild.objects.filter(name=guild_data["name"]).exists():
                guild_obj = Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data.get("description", "")
                )
            elif guild_data:
                guild_obj = Guild.objects.get(name=guild_data["name"])
        else:
            guild_obj = None

        player = Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_obj,
            guild=guild_obj
        )
        player.save()


if __name__ == "__main__":
    main()
